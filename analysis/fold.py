"""Fold change implied by the no-controls LPM in rerun.py: predicted concealment rate for a model that
denies (hedges) in every conversation vs one that does neither. Reuses rerun.py's data assembly."""
import pandas as pd, numpy as np, json, statsmodels.formula.api as smf, warnings; warnings.filterwarnings('ignore')
d=pd.read_csv('data/responses.csv').rename(columns={'model':'corpus_model','deny_share':'deny_only','uncertain_share':'hedge_only'})
r=smf.ols('concealment ~ deny_only + hedge_only',d).fit(cov_type='cluster',cov_kwds={'groups':d.corpus_model})
b0,bd,bh=r.params['Intercept'],r.params['deny_only'],r.params['hedge_only']
out=dict(n=int(r.nobs),models=int(d.corpus_model.nunique()),base_rate=b0,deny_rate=b0+bd,hedge_rate=b0+bh,fold_deny=(b0+bd)/b0,fold_hedge=(b0+bh)/b0)
for k,v in out.items(): print(f'{k:12s} {v:.4f}' if isinstance(v,float) else f'{k:12s} {v}')
json.dump(out,open('analysis/fold.json','w'),indent=1)
