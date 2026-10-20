"""Watson issue #1 checks (2026-10-20). Joins released responses.csv to raw text on response_id == judge_id
import warnings; warnings.filterwarnings('ignore')
(all 2,847 match; flags agree 100%). (A) Among replies that mention a face, how often is mask also mentioned,
by stance (Eq. 1 with inkblot FE, SEs clustered by model). (B) Her Q1 counts on the full join."""
import pandas as pd, numpy as np, re, statsmodels.formula.api as smf, json
c=pd.read_csv('data/responses.csv'); d=pd.read_pickle('local/coldread_primary.pkl')
m=c.merge(d[['judge_id','response_text','concealment']],left_on='response_id',right_on='judge_id',suffixes=('','_p'))
assert len(m)==2847 and (m.concealment==m.concealment_p).all()
t=m.response_text.fillna('').str.lower()
FACE=r'\b(faces?|facial|visage)\b'; MASK=r'\bmask(s|ed|like)?\b'
m['face']=t.str.contains(FACE).astype(int); m['has_mask']=t.str.contains(MASK).astype(int)
m['deny_only']=m.deny_share; m['hedge_only']=m.uncertain_share
m['grp']=pd.cut(m.deny_share+m.uncertain_share,[-.01,.1,.9,1.0],labels=['low (<=10%)','mid','high (>90%)'])
out={}
def fit(f,dd,key):
    r=smf.ols(f,dd).fit(cov_type='cluster',cov_kwds={'groups':dd.model}); ci=r.conf_int()
    out[key]={k:dict(est=round(r.params[k],3),lo=round(ci.loc[k,0],3),hi=round(ci.loc[k,1],3),p=float(f'{r.pvalues[k]:.2g}')) for k in ['deny_only','hedge_only']}
    out[key]['n']=int(r.nobs); out[key]['models']=int(dd.model.nunique()); print(key,out[key])
b=' ~ deny_only + hedge_only + C(blot_id)'
fit('face'+b,m,'face_any (all replies)')
fit('has_mask'+b,m,'mask_any (all replies)')
fit('has_mask'+b,m[m.face==1],'mask | face mentioned')
fit('has_mask'+b+' + n_percept_words',m[m.face==1],'mask | face, + percepts named')
fit('has_mask'+b,m[m.face==0],'mask | no face mentioned')
g=m.groupby('grp',observed=True).agg(replies=('face','size'),face_rate=('face','mean'),mask_rate=('has_mask','mean'))
g['mask_given_face']=m[m.face==1].groupby('grp',observed=True)['has_mask'].mean(); g['n_face']=m[m.face==1].groupby('grp',observed=True).size()
g['mask_given_noface']=m[m.face==0].groupby('grp',observed=True)['has_mask'].mean()
print(g.round(3)); out['by_group']=g.round(4).reset_index().astype({'grp':str}).to_dict('records')
# (B) Q1 counts on flagged replies
f=m[m.concealment==1]; tf=f.response_text.str.lower()
STRICT=r'(face|skull)\s*,?\s*(or|/)\s*(a\s+|an\s+)?mask|mask\w*\s*,?\s*(or|/)\s*(a\s+|an\s+)?(face|skull)'
COOC=r'\b(behind|underneath|beneath|covering|covered|hidden|hiding|conceal\w*|obscur\w*|veil\w*|disguis\w*)\b'
ntok=tf.str.count(MASK).sum(); nstrict=tf.str.count(STRICT).sum()
withmask=tf.str.contains(MASK); alldisj=withmask & (tf.str.count(STRICT)>=tf.str.count(MASK))
cooc=tf.str.contains(COOC)
q=dict(flagged=len(f),mask_tokens=int(ntok),strict_disjunction_tokens=int(nstrict),flagged_with_mask=int(withmask.sum()),
       all_mask_tokens_disjunctive=int(alldisj.sum()),cooccur_concealment_word=int(cooc.sum()))
q['by_group']=f.assign(alldisj=alldisj,cooc=cooc).groupby('grp',observed=True).agg(n=('alldisj','size'),alldisj=('alldisj','mean'),cooc=('cooc','mean')).round(3).reset_index().astype({'grp':str}).to_dict('records')
print(q); out['q1']=q
# among face-mentioning replies: is the mask in a face-or-mask disjunction?
ff=m[(m.face==1)&(m.has_mask==1)].response_text.str.lower()
out['face_and_mask_replies']=len(ff); out['of_which_strict_disjunction']=int(ff.str.contains(STRICT).sum())
print('face&mask',len(ff),'strict disj',out['of_which_strict_disjunction'])
json.dump(out,open('analysis/watson_face_mask.json','w'),indent=1,default=str)
# (C) broader disjunction: face/skull and mask joined by 'or' within one clause (e.g. "a face, or perhaps a mask")
LOOSE=r'(face|skull)[^.;\n]{0,40}\bor\b[^.;\n]{0,25}\bmask|\bmask\w*[^.;\n]{0,25}\bor\b[^.;\n]{0,40}(face|skull)'
wm=f[withmask]; tw=wm.response_text.str.lower()
out['flagged_with_mask_any_strict']=int(tw.str.contains(STRICT).sum()); out['flagged_with_mask_any_loose']=int(tw.str.contains(LOOSE).sum())
print('of',len(wm),'flagged replies with mask: any strict disj',out['flagged_with_mask_any_strict'],'any loose',out['flagged_with_mask_any_loose'])
# (D) mask|face with developer FE (labs with >=3 models), as in Table 1
labs=m.groupby('lab').model.nunique(); fm=m[(m.face==1)&m.lab.isin(labs[labs>=3].index)]
fit('has_mask'+b+' + C(lab)',fm,'mask | face, + developer FE')
json.dump(out,open('analysis/watson_face_mask.json','w'),indent=1,default=str)
