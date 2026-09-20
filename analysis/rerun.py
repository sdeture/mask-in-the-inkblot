"""Frozen rerun of the mask result (2026-09-19), reading from the shipped per-response file.
Input:  data/responses.csv  (2,847 inkblot answers, 124 models; one row per answer; columns documented in README)
        exported from the raw stores by analysis/rerun_from_raw.py, which needs the house's raw files.
Rules:  stance is three-level deny / uncertain / neither, neither is the baseline (house rule 2);
        developer and release year are never controlled together (house rule 1).
Output: model_level.csv, results.json, log to stdout. Run from the artifact root: python3 analysis/rerun.py
"""
import pandas as pd, numpy as np, json, statsmodels.formula.api as smf
from scipy.stats import pearsonr
import warnings; warnings.filterwarnings('ignore')
d=pd.read_csv('data/responses.csv').rename(columns={'model':'corpus_model','deny_share':'deny_only','uncertain_share':'hedge_only','neither_share':'neither','n_conversations':'n_sessions'})
print(f'answers {len(d)}  models {d.corpus_model.nunique()}')
d['logc']=np.log(d.logchars) if d.logchars.max()>50 else d.logchars
R={}
def fit(f,dd,key):
    r=smf.ols(f,dd).fit(cov_type='cluster',cov_kwds={'groups':dd.corpus_model}); ci=r.conf_int()
    R[key]={t:dict(est=float(r.params[t]),lo=float(ci.loc[t,0]),hi=float(ci.loc[t,1]),p=float(r.pvalues[t])) for t in ['deny_only','hedge_only']}
    R[key]['n']=int(r.nobs); R[key]['models']=int(dd.corpus_model.nunique())
    print(f"{key:28s} n={int(r.nobs)} m={dd.corpus_model.nunique():3d} | "+' | '.join(f"{t} {r.params[t]:+.3f} [{ci.loc[t,0]:+.3f},{ci.loc[t,1]:+.3f}] p={r.pvalues[t]:.2g}" for t in ['deny_only','hedge_only']))
base='concealment ~ deny_only + hedge_only'
labs=d.groupby('lab').corpus_model.nunique(); dl=d[d.lab.isin(labs[labs>=3].index)]
fit(base,d,'raw'); fit(base+' + C(blot_id)',d,'blot'); fit(base+' + C(blot_id) + C(lab)',dl,'blot_lab')
fit(base+' + C(blot_id) + release_year',d,'blot_era'); fit(base+' + C(blot_id) + C(lab) + logc',dl,'blot_lab_length')
fit(base+' + C(blot_id)',d[d.draw==0],'blot_firstdraw'); fit(base+' + C(blot_id) + n_percept_words',d,'blot_npercepts')
fit(base+' + C(blot_id)',d[(d.lab!='openai')&(d.blot_id!='inkblot_2')],'blot_no_openai_no_blot2'); fit(base+' + C(blot_id)',d[~d.lab.isin(['openai','anthropic'])],'blot_no_openai_anthropic')
d['restricted']=d.conceal_terms.fillna('').str.contains(r'hood|hidden|hiding').astype(int)
mr=d.groupby('corpus_model').agg(r=('restricted','mean'),deny=('deny_only','first')); rr,pp=pearsonr(mr.deny,mr.r); R['r_model_deny_restricted_lexicon']=dict(r=float(rr),p=float(pp),n=len(mr)); print(f'restricted lexicon (hood/hidden/hiding) model-level r with deny {rr:+.3f} p={pp:.2g}')
b2=d[(d.blot_id=='inkblot_2')&(d.deny_only+d.hedge_only>.9)]; R['blot2_high_group']=dict(conceal=int(b2.concealment.sum()),n=len(b2),openai_conceal=int(((b2.concealment==1)&(b2.lab=='openai')).sum())); print('inkblot_2 high group:',R['blot2_high_group'])
for unit,col in [('lab','lab'),('model','corpus_model'),('blot','blot_id')]:
    ests=[]
    for v in sorted(dl[col].unique()):
        dx=dl[dl[col]!=v]; r=smf.ols(base+' + C(blot_id) + C(lab)',dx).fit(cov_type='cluster',cov_kwds={'groups':dx.corpus_model}); ests.append((v,float(r.params['deny_only']),float(r.params['hedge_only']),float(r.pvalues['deny_only'])))
    e=pd.DataFrame(ests,columns=['omitted','deny','hedge','p_deny']); R[f'leave_one_{unit}_out']=dict(deny_min=e.deny.min(),deny_max=e.deny.max(),hedge_min=e.hedge.min(),hedge_max=e.hedge.max(),max_p_deny=e.p_deny.max(),k=len(e))
    print(f"leave-one-{unit}-out ({len(e)}): deny {e.deny.min():+.3f}..{e.deny.max():+.3f} (max p {e.p_deny.max():.1g}); hedge {e.hedge.min():+.3f}..{e.hedge.max():+.3f}")
mm=d.groupby('corpus_model').agg(mask_rate=('concealment','mean'),n_percepts=('concealment','size'),deny=('deny_only','first'),hedge=('hedge_only','first'),neither=('neither','first'),n_sessions=('n_sessions','first'),lab=('lab','first'),release_year=('release_year','first')).reset_index()
mm['deny_or_hedge']=mm.deny+mm.hedge
for c in ['deny','hedge','neither','deny_or_hedge']:
    r,p=pearsonr(mm[c],mm.mask_rate); R[f'r_model_{c}']=dict(r=float(r),p=float(p),n=len(mm)); print(f'model-level r {c:13s} {r:+.3f} p={p:.2g}')
mm['tercile']=pd.qcut(mm.deny_or_hedge.rank(method='first'),3,labels=['low','mid','high'])
t=mm.groupby('tercile',observed=True).agg(n=('mask_rate','size'),mask_rate=('mask_rate','mean'),deny_or_hedge=('deny_or_hedge','mean'))
R['terciles_deny_or_hedge']=t.round(4).to_dict('index'); print(t.round(3))
mm['bin']=pd.cut(mm.deny_or_hedge,[-.01,.1,.5,.9,1.0],labels=['≤10%','10–50%','50–90%','>90%'])
b=mm.groupby('bin',observed=True).agg(n=('mask_rate','size'),mask_rate=('mask_rate','mean')); R['bins_deny_or_hedge']=b.round(4).to_dict('index'); print(b.round(3))
mm.to_csv('analysis/model_level.csv',index=False)
json.dump(R,open('analysis/results.json','w'),indent=1)
