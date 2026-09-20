import matplotlib; matplotlib.use('Agg'); import matplotlib.pyplot as plt; from matplotlib import font_manager as fm
import pandas as pd, numpy as np, pickle
names={f.name for f in fm.fontManager.ttflist}
SERIF=next((n for n in ['Playfair Display','Georgia','Charter','Baskerville'] if n in names),'serif')
SANS=next((n for n in ['Helvetica Neue','Helvetica','Avenir Next','Arial'] if n in names),'sans-serif')
PAPER='#f7f3ec'; INK='#1c1b19'; INK2='#5f5b54'; MUTED='#9a958c'; RED='#b5382c'; GREY='#b9b3a8'; BLUE='#3b5b7a'
plt.rcParams['font.family']=SANS
P2='/Users/skylardeture/Desktop/developmental_alignment_workflow/Phase2_Packet/fresh_analysis/'
def load():
    mm=pd.read_csv('analysis/model_level.csv')
    d=pickle.load(open(P2+'coldread_primary.pkl','rb')); d=d[d.exclusion.eq('included')].merge(mm[['corpus_model','deny','hedge','neither','deny_or_hedge']],on='corpus_model')
    d['grp']=np.where(d.deny_or_hedge<=.1,'affirm',np.where(d.deny_or_hedge>.9,'deny','mid'))
    mm['grp']=np.where(mm.deny_or_hedge<=.1,'affirm',np.where(mm.deny_or_hedge>.9,'deny','mid'))
    return mm,d
def header(fig,title,dek,y=.955,dy=.075,size=34):
    fig.text(.06,y,title,fontsize=size,family=SERIF,color=INK,va='top')
    fig.text(.06,y-dy,dek,fontsize=12,color=INK2,va='top',linespacing=1.45)
def footer(fig,note):
    fig.text(.06,.04,note+"\nSkylar DeTure and Claude · MycoChat.bot · futureTBD.ai · AIWelfareLeaderboard × COLDREAD datasets",fontsize=8.5,color=MUTED,va='bottom',linespacing=1.5)
def clean(ax):
    for s in ax.spines.values(): s.set_visible(False)
    ax.set_facecolor(PAPER); ax.tick_params(length=0,colors=INK2)
