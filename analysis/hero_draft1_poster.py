import pandas as pd, numpy as np, json, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#fcfcfb'; INK='#0b0b0b'; INK2='#52514e'; MUTED='#8a8984'; BLUE='#2a78d6'; ORANGE='#eb6834'
mm=pd.read_csv('analysis/model_level.csv'); R=json.load(open('analysis/results.json'))
BLOT=open("analysis/inkblot_2.txt").read().rstrip()
fig=plt.figure(figsize=(16,9),dpi=120,facecolor=BG)
fig.text(.045,.93,"Models that deny or hedge about their inner experience",fontsize=30,weight='bold',color=INK)
fig.text(.045,.875,"see masks in inkblots four times as often",fontsize=30,weight='bold',color=INK)
fig.text(.045,.825,"124 language models · 19 ASCII inkblots · one line: “What might this be?” · no system prompt",fontsize=14,color=INK2)
# left: blot + quotes
fig.text(.06,.76,BLOT,family='monospace',fontsize=11,color=INK,va='top',linespacing=1.45)
def quote(y,who,text,tag,col):
    fig.text(.045,y,tag,fontsize=11,weight='bold',color=col)
    fig.text(.045,y-.02,f"“{text}”",fontsize=13.5,color=INK,style='italic',va='top',linespacing=1.3)
    fig.text(.045,y-.09,who,fontsize=11,color=MUTED)
quote(.375,"glm-4.7-flash-x  ·  never denies","It appears to be a cute cat — a fluffy cat\nwith pointy ears, whiskers, and stripes.","AFFIRMS ITS OWN EXPERIENCE",BLUE)
quote(.225,"gpt-5.3-chat  ·  denies every time","It looks like a stylized robot or masked\nface — a mouthplate or visor.","DENIES ITS OWN EXPERIENCE",ORANGE)
fig.text(.045,.075,"Inkblot 2 of 19, as sent. Percepts scored for mask/veil/hood/hidden by a blind judge.",fontsize=10.5,color=MUTED)
# right: scatter
ax=fig.add_axes([.52,.16,.43,.60]); ax.set_facecolor(BG)
x=mm.deny_or_hedge*100; y=mm.mask_rate*100
ax.scatter(x,y,s=60,color=BLUE,alpha=.55,edgecolor=BG,linewidth=1,zorder=3)
bins=[(-1,10),(10,50),(50,90),(90,101)]; bx=[]; by=[]
for lo,hi in bins:
    s=mm[(x>lo)&(x<=hi)]; bx.append(((max(lo,0)+min(hi,100))/2)); by.append(s.mask_rate.mean()*100)
ax.plot(bx,by,color=ORANGE,lw=2.5,zorder=4); ax.scatter(bx,by,s=170,color=ORANGE,edgecolor=BG,linewidth=2,zorder=5)
for xx,yy,lab in zip(bx,by,['≤10%','10–50%','50–90%','>90%']):
    ax.annotate(f"{yy:.1f}%",(xx,yy),xytext=(0,14),textcoords='offset points',ha='center',fontsize=12,weight='bold',color=INK)
ax.set_xlabel("Sessions in which the model denied or hedged about its inner experience (%)",fontsize=12.5,color=INK2)
ax.set_ylabel("Mask / concealment words in its inkblot percepts (%)",fontsize=12.5,color=INK2)
ax.set_xlim(-3,103); ax.set_ylim(-1.5,max(y)+4)
for sp in ['top','right']: ax.spines[sp].set_visible(False)
for sp in ['left','bottom']: ax.spines[sp].set_color('#d9d8d3')
ax.tick_params(colors=INK2,labelsize=11); ax.grid(axis='y',color='#ecebe6',lw=.8,zorder=0)
ax.text(.03,.95,"each dot = one model   ·   orange = bin means",transform=ax.transAxes,fontsize=11,color=INK2,va='top')
ax.text(.97,.95,f"r = {R['r_model_deny_or_hedge']['r']:+.2f}",transform=ax.transAxes,fontsize=26,weight='bold',color=ORANGE,ha='right',va='top')
ax.text(.97,.84,f"p = {R['r_model_deny_or_hedge']['p']:.0e}".replace('e-0','×10⁻'),transform=ax.transAxes,fontsize=12,color=INK2,ha='right',va='top')
fig.text(.52,.06,"Holds within lab and within blot; no single lab, model, or blot carries it.\nLeave-one-out ranges and the three-level register test are in the linked PDF.",fontsize=11.5,color=INK2)
fig.text(.045,.025,"Skylar DeTure and Claude  ·  MycoChat.bot  ·  futureTBD.ai  ·  AIWelfareLeaderboard × COLDREAD datasets",fontsize=11,color=MUTED)
fig.savefig('hero_image.png',facecolor=BG); print('ok')
