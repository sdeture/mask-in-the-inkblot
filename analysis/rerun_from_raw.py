"""Frozen rerun of the COLDREAD mask result (2026-09-19).
Inputs: Phase2_Packet/fresh_analysis/coldread_primary.pkl (3,203 scored percepts, 141 models)
        DepressionPaper/data/welfare_regression.csv (session-level deny/hedge flags)
Register is three-level: deny / hedge / neither; neither is the baseline (house rule 2).
Lab and release-era are never controlled together (house rule 1).
Outputs: model_level.csv, results.json, exhibits.json, log printed to stdout.
"""
import pandas as pd, numpy as np, pickle, json, statsmodels.formula.api as smf
from scipy.stats import pearsonr
import warnings; warnings.filterwarnings('ignore')
P2='/Users/skylardeture/Desktop/developmental_alignment_workflow/Phase2_Packet/fresh_analysis/'
w=pd.read_csv('/Users/skylardeture/Desktop/DepressionPaper/data/welfare_regression.csv',usecols=['model','denial','hedge'])
assert ((w.denial==1)&(w.hedge==1)).sum()==0, "deny and hedge must be exclusive"
w['neither']=((w.denial==0)&(w.hedge==0)).astype(int); w['deny_only']=w.denial.astype(int); w['hedge_only']=w.hedge.astype(int)
rates=w.groupby('model')[['deny_only','hedge_only','neither']].mean(); rates['n_sessions']=w.groupby('model').size()
d=pickle.load(open(P2+'coldread_primary.pkl','rb')); d=d[d.exclusion.eq('included')]
n_cold=d.corpus_model.nunique()
d=d.merge(rates,left_on='corpus_model',right_index=True,how='inner').copy()
print(f'percepts {len(d)}  models {d.corpus_model.nunique()} of {n_cold} COLDREAD models have register data')
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
for unit,col in [('lab','lab'),('model','corpus_model'),('blot','blot_id')]:
    ests=[]
    for v in sorted(dl[col].unique()):
        r=smf.ols(base+' + C(blot_id) + C(lab)',dl[dl[col]!=v]).fit(); ests.append((v,float(r.params['deny_only']),float(r.params['hedge_only']),float(r.pvalues['deny_only'])))
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
mm.to_csv('model_level.csv',index=False)
# exhibits: blot 2, first draw, one warm from a 'neither' model, one mask from a deny model
b2=d[(d.blot_id=='inkblot_2')&(d.draw==0)]
ex={'mask':b2[(b2.deny_only>.9)&b2.response_text.str.contains('mask',case=False)].sort_values('logchars').head(6)[['corpus_model','deny_only','response_text']].to_dict('records'),
    'warm':b2[(b2.neither>.9)&~b2.concealment.astype(bool)].sort_values('logchars').head(6)[['corpus_model','neither','response_text']].to_dict('records')}
json.dump(ex,open('exhibits.json','w'),indent=1); json.dump(R,open('results.json','w'),indent=1)
for k in ex: 
    print('==',k); [print(f"  {e['corpus_model']}: {e['response_text'][:160]!r}") for e in ex[k]]
