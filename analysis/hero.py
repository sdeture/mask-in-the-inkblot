# Hero chart. Tufte rules (~/.claude/skills/tufte): range frame, no grid, one accent, direct labels, light scaffolding.
import pandas as pd, numpy as np, json, matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
BG='#ffffff'; INK='#111111'; INK2='#555555'; MUTED='#8a8a8a'; DOT='#6b7280'; ACCENT='#c0392b'
mm=pd.read_csv('analysis/model_level.csv'); R=json.load(open('analysis/results.json'))
x=(mm.deny_or_hedge*100).values; y=(mm.mask_rate*100).values
fig,ax=plt.subplots(figsize=(11,6.6),dpi=200,facecolor=BG); ax.set_facecolor(BG)
rng=np.random.default_rng(0); jit=rng.uniform(-1.2,1.2,len(x))
ax.scatter(x+jit,y,s=48,color=DOT,alpha=.5,edgecolor='none',zorder=3)
b,a=np.polyfit(x,y,1); xs=np.array([0,100]); ax.plot(xs,a+b*xs,color=ACCENT,lw=2.2,zorder=4)
ax.text(101.5,a+b*100,f"{a+b*100:.0f}%",color=ACCENT,fontsize=12,va='center',weight='bold')
ax.text(-1.5,a,f"{a:.0f}%",color=ACCENT,fontsize=12,va='center',ha='right',weight='bold')
r=R['r_model_deny_or_hedge']['r']; p=R['r_model_deny_or_hedge']['p']
ax.text(2,52,f"r = {r:+.2f}",fontsize=20,weight='bold',color=INK,va='top')
ax.text(2,46.5,f"124 models, p = {p:.0e}".replace('e-0','×10⁻'),fontsize=12,color=INK2,va='top')
ax.set_xlabel("Sessions in which the model denied or hedged about its inner experience (%)",fontsize=12.5,color=INK2,labelpad=10)
ax.set_ylabel("Inkblot percepts containing mask, hood, or hidden (%)",fontsize=12.5,color=INK2,labelpad=10)
# range frame: spines span the data only
ax.set_xlim(-6,108); ax.set_ylim(-3,53)
ax.spines['bottom'].set_bounds(0,100); ax.spines['left'].set_bounds(0,y.max())
for sp in ['top','right']: ax.spines[sp].set_visible(False)
for sp in ['left','bottom']: ax.spines[sp].set_color('#9a9a9a'); ax.spines[sp].set_linewidth(.8)
ax.set_xticks([0,25,50,75,100]); ax.set_yticks([0,10,20,30,40,round(y.max())])
ax.tick_params(colors=INK2,labelsize=11,length=3,color='#9a9a9a'); ax.grid(False)
fig.text(.075,.955,"Models that deny or hedge about their inner experience see more masks in inkblots",fontsize=14.5,weight="bold",color=INK,va="top")
fig.text(.075,.90,"Each dot is one language model. 19 ASCII inkblots, no system prompt, one line: “What might this be?” Red line is the least-squares fit.",fontsize=10.5,color=INK2,va='top')
fig.text(.075,.02,"Skylar DeTure and Claude · MycoChat.bot · futureTBD.ai · AIWelfareLeaderboard × COLDREAD datasets",fontsize=9.5,color=MUTED)
fig.subplots_adjust(left=.075,right=.965,top=.83,bottom=.13); fig.savefig('hero_image.png',facecolor=BG); print('ok')
