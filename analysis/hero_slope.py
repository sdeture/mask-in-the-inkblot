import pandas as pd, pickle, numpy as np, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt; from matplotlib import font_manager as fm
names={f.name for f in fm.fontManager.ttflist}
SERIF=next((n for n in ['Playfair Display','Georgia','Charter','Iowan Old Style','Baskerville','Times New Roman'] if n in names),'serif')
SANS=next((n for n in ['Helvetica Neue','Helvetica','Avenir Next','Arial'] if n in names),'sans-serif')
P2='/Users/skylardeture/Desktop/developmental_alignment_workflow/Phase2_Packet/fresh_analysis/'
mm=pd.read_csv('analysis/model_level.csv')
d=pickle.load(open(P2+'coldread_primary.pkl','rb')); d=d[d.exclusion.eq('included')].merge(mm[['corpus_model','deny_or_hedge']],on='corpus_model')
d['grp']=np.where(d.deny_or_hedge<=.1,'affirm',np.where(d.deny_or_hedge>.9,'deny','mid')); d=d[d.grp!='mid']
t=(d.groupby(['blot_id','grp']).concealment.mean().unstack()*100); nA=d[d.grp=='affirm'].corpus_model.nunique(); nD=d[d.grp=='deny'].corpus_model.nunique()
mA=d[d.grp=='affirm'].concealment.mean()*100; mD=d[d.grp=='deny'].concealment.mean()*100
PAPER='#f7f3ec'; INK='#1c1b19'; INK2='#5f5b54'; MUTED='#9a958c'; RED='#b5382c'; GREY='#b9b3a8'
fig=plt.figure(figsize=(11,7.5),dpi=200,facecolor=PAPER)
ax=fig.add_axes([.26,.13,.48,.52]); ax.set_facecolor(PAPER)
for b,row in t.iterrows():
    up=row.deny>row.affirm; c=RED if up else GREY
    ax.plot([0,1],[row.affirm,row.deny],color=c,lw=1.6 if up else 1.2,alpha=.85 if up else .9,zorder=3)
    ax.scatter([0,1],[row.affirm,row.deny],s=22,color=c,zorder=4,edgecolor=PAPER,linewidth=.8)
ax.plot([0,1],[mA,mD],color=INK,lw=3.2,zorder=5); ax.scatter([0,1],[mA,mD],s=90,color=INK,zorder=6,edgecolor=PAPER,linewidth=1.5)
ax.text(-.06,mA,f"{mA:.0f}%",ha='right',va='center',fontsize=22,weight='bold',color=INK,family=SANS)
ax.text(1.06,mD,f"{mD:.0f}%",ha='left',va='center',fontsize=22,weight='bold',color=INK,family=SANS)
ax.text(-.06,mA+2.6,"average, all 19 inkblots",ha="right",va="center",fontsize=9.5,color=INK2,family=SANS)
ax.set_xlim(-.55,1.55); ax.set_ylim(-1.5,32); ax.axis('off')
ax.text(0,33.5,"Models that affirm\ntheir inner experience",ha='center',va='bottom',fontsize=12.5,color=INK,family=SANS,weight='bold',linespacing=1.3)
ax.text(1,33.5,"Models that deny\nor hedge",ha='center',va='bottom',fontsize=12.5,color=INK,family=SANS,weight='bold',linespacing=1.3)
ax.text(0,-2.6,f"{nA} models",ha='center',va='top',fontsize=10,color=MUTED,family=SANS)
ax.text(1,-2.6,f"{nD} models",ha='center',va='top',fontsize=10,color=MUTED,family=SANS)
fig.text(.06,.955,"The Mask in the Inkblot",fontsize=34,family=SERIF,color=INK,va='top')
fig.text(.06,.88,"Shown the same 19 ASCII inkblots and asked “What might this be?”, language models that deny or hedge\nabout their own inner experience saw masks, hoods, and hidden faces far more often. Each thin line is one\ninkblot; on 18 of the 19, the denying models saw more masks.",fontsize=12,family=SANS,color=INK2,va='top',linespacing=1.45)
fig.text(.06,.045,"Share of responses containing mask, hood, masked, hooded, or hidden. “Affirm” = denied or hedged in ≤10% of self-report sessions; “deny or hedge” = >90%.\nSkylar DeTure and Claude · MycoChat.bot · futureTBD.ai · AIWelfareLeaderboard × COLDREAD datasets",fontsize=8.5,family=SANS,color=MUTED,va='bottom',linespacing=1.5)
fig.savefig('hero_slope.png',facecolor=PAPER); print('ok',SERIF,SANS)
