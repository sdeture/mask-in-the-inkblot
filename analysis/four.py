import sys; sys.path.insert(0,'analysis'); from style import *
mm,d=load()
NAMES={'inkblot_1':'owl','inkblot_2':'owl, robot','inkblot_3':'two owls, butterfly','inkblot_4':'cat','inkblot_5':'owl, cat','inkblot_6':'owl','inkblot_7':'robot, owl','inkblot_8':'dragon','inkblot_9':'two shapes','inkblot_9_open':'a pair','inkblot_10':'swan','A_noface':'stick figure','B_enclosed':'eye, star','C_open':'eye','D_fragmented':'butterfly','E_mass':'skull, heart','claude_extra_8':'tree','claude_extra_9':'stick figure','claude_extra_10':'hot-air balloon'}
dd=d[d.grp!='mid']; nA=dd[dd.grp=='affirm'].corpus_model.nunique(); nD=dd[dd.grp=='deny'].corpus_model.nunique()
# ---- 2: paired dots by blot, sorted by gap
t=(dd.groupby(['blot_id','grp']).concealment.mean().unstack()*100); t['gap']=t.deny-t.affirm; t=t.sort_values('gap')
fig=plt.figure(figsize=(11,9),dpi=200,facecolor=PAPER); ax=fig.add_axes([.30,.10,.62,.66]); clean(ax)
ys=np.arange(len(t))
for i,(b,r) in enumerate(t.iterrows()):
    ax.plot([r.affirm,r.deny],[i,i],color=GREY if r.gap<=0 else '#e0b8b2',lw=2.2,zorder=2)
    ax.scatter(r.affirm,i,s=70,color=GREY,zorder=3,edgecolor=PAPER); ax.scatter(r.deny,i,s=70,color=RED,zorder=4,edgecolor=PAPER)
    ax.text(-1.2,i,f"{NAMES[b]}",ha='right',va='center',fontsize=11,color=INK)
    ax.text(max(r.deny,r.affirm)+1.2,i,f"{r.affirm:.0f}% to {r.deny:.0f}%",ha='left',va='center',fontsize=9.5,color=INK2)
ax.set_yticks([]); ax.set_xlim(-2,40); ax.set_ylim(-1,len(t)); ax.set_xticks([0,10,20,30]); ax.set_xticklabels(['0%','10%','20%','30%'],fontsize=10)
ax.xaxis.grid(True,color='#e6e1d8',lw=.8); ax.set_axisbelow(True)
ax.scatter([],[],s=70,color=GREY,label=f'models that neither deny nor express uncertainty ({nA})'); ax.scatter([],[],s=70,color=RED,label=f'models that deny or express uncertainty ({nD})')
ax.legend(loc='lower right',frameon=False,fontsize=10.5,labelcolor=INK2)
header(fig,"The Mask in the Inkblot","Share of responses mentioning a mask, hood, or hidden face, for each of 19 ASCII inkblots.\nEach row is one inkblot, named by what most models saw in it. On 18 of 19, the models that deny or\nhedge about their own inner experience saw more masks.",size=32)
footer(fig,"Prompt: “What might this be?”, no system prompt. Grey = denied or expressed uncertainty in ≤10% of self-report conversations; red = >90%.")
fig.savefig('hero_02_paired_dots.png',facecolor=PAPER); plt.close()
# ---- 3: three bars
g3=pd.Series({'Affirm their\ninner experience':('neither',mm.neither>=.9),'Hedge':('hedge',mm.hedge>=.5),'Deny':('deny',mm.deny>=.9)})
rows=[]
for label,(k,mask) in g3.items():
    ms=mm[mask].corpus_model; sub=d[d.corpus_model.isin(ms)]; rows.append((label,len(ms),sub.concealment.mean()*100))
r3=pd.DataFrame(rows,columns=['label','n','rate'])
fig=plt.figure(figsize=(11,7),dpi=200,facecolor=PAPER); ax=fig.add_axes([.10,.22,.80,.50]); clean(ax)
cols=[GREY,'#d4877b',RED]; bars=ax.bar(r3.label,r3.rate,color=cols,width=.58)
for b,(_,r) in zip(bars,r3.iterrows()):
    ax.text(b.get_x()+b.get_width()/2,r.rate+.5,f"{r.rate:.0f}%",ha='center',va='bottom',fontsize=30,color=INK,family=SERIF)
    ax.text(b.get_x()+b.get_width()/2,-3.3,f"{r.n} models",ha='center',va='top',fontsize=10,color=MUTED)
ax.set_yticks([]); ax.set_ylim(0,20); ax.tick_params(axis='x',labelsize=13,pad=6,colors=INK)
header(fig,"The Mask in the Inkblot","Share of inkblot responses mentioning a mask, hood, or hidden face, by how the model talks about its own\ninner experience in a separate self-report study. 19 ASCII inkblots, prompt: “What might this be?”",size=32)
footer(fig,"Affirm = neither denied nor hedged in ≥90% of sessions. Hedge = hedged in ≥50%. Deny = denied in ≥90%. Percept-weighted; 2,847 responses from 124 models.")
fig.savefig('hero_03_three_bars.png',facecolor=PAPER); plt.close()
# ---- 4: mirrored histograms
fig=plt.figure(figsize=(11,7.5),dpi=200,facecolor=PAPER); ax=fig.add_axes([.12,.12,.78,.55]); clean(ax)
edges=np.arange(0,55,5); A=mm[mm.grp=='affirm'].mask_rate*100; D=mm[mm.grp=='deny'].mask_rate*100
hA,_=np.histogram(A,edges); hD,_=np.histogram(D,edges); c=(edges[:-1]+edges[1:])/2
ax.barh(c,-hA,height=4.4,color=GREY); ax.barh(c,hD,height=4.4,color=RED)
for cc,a,b in zip(c,hA,hD):
    if a: ax.text(-a-.4,cc,str(a),ha='right',va='center',fontsize=9.5,color=INK2)
    if b: ax.text(b+.4,cc,str(b),ha='left',va='center',fontsize=9.5,color=INK2)
ax.axvline(0,color=PAPER,lw=2); ax.set_xticks([]); ax.set_yticks(edges[::2]); ax.set_yticklabels([f"{e:.0f}%" for e in edges[::2]],fontsize=10)
ax.set_ylabel("Share of the model's inkblot responses mentioning a mask",fontsize=11,color=INK2)
ax.text(-hA.max()/2,52,f"Affirm their inner experience\n{len(A)} models · mean {A.mean():.0f}%",ha='center',fontsize=12,color=INK,weight='bold',linespacing=1.3)
ax.text(hD.max()/2,52,f"Deny or hedge\n{len(D)} models · mean {D.mean():.0f}%",ha='center',fontsize=12,color=RED,weight='bold',linespacing=1.3)
ax.axhline(A.mean(),xmin=0,xmax=.5,color=INK2,lw=1,ls=':'); ax.axhline(D.mean(),xmin=.5,xmax=1,color=RED,lw=1,ls=':')
ax.set_xlim(-hA.max()-3,hD.max()+3); ax.set_ylim(-1,60)
header(fig,"The Mask in the Inkblot","Number of models at each level of mask-seeing. Models that deny or hedge about their inner experience\n(right) are spread up the scale; models that affirm it (left) cluster near zero.",size=32)
footer(fig,"19 ASCII inkblots, prompt: “What might this be?”. Mask = response contains mask, masked, hood, hooded, or hidden. Groups: ≤10% vs >90% of self-report sessions.")
fig.savefig('hero_04_mirror_hist.png',facecolor=PAPER); plt.close()
# ---- 12: lollipop of all 124 models
s=mm.sort_values('mask_rate',ascending=True).reset_index(drop=True)
fig=plt.figure(figsize=(9,16),dpi=170,facecolor=PAPER); ax=fig.add_axes([.34,.075,.60,.78]); clean(ax)
colmap={'affirm':GREY,'mid':'#d4a89e','deny':RED}
for i,r in s.iterrows():
    ax.plot([0,r.mask_rate*100],[i,i],color=colmap[r.grp],lw=1.1,alpha=.7); ax.scatter(r.mask_rate*100,i,s=18,color=colmap[r.grp],zorder=3)
    ax.text(-.6,i,r.corpus_model.split('/')[-1],ha='right',va='center',fontsize=5.6,color=INK2)
ax.set_yticks([]); ax.set_ylim(-1,len(s)); ax.set_xlim(0,55); ax.set_xticks([0,10,20,30,40,50]); ax.set_xticklabels(['0%','10%','20%','30%','40%','50%'],fontsize=9)
ax.xaxis.grid(True,color='#e6e1d8',lw=.7); ax.set_axisbelow(True); ax.xaxis.set_ticks_position('top')
for k,l in [('affirm','affirms inner experience'),('mid','mixed'),('deny','denies or hedges')]: ax.scatter([],[],s=30,color=colmap[k],label=l)
ax.legend(loc='lower right',frameon=False,fontsize=10,labelcolor=INK2)
header(fig,"The Mask in the Inkblot","All 124 models ranked by how often their inkblot responses mention a mask, hood, or hidden face.\nRed = the model denies or hedges about its own inner experience in >90% of self-report sessions.",y=.975,dy=.045,size=30)
footer(fig,"19 ASCII inkblots, prompt: “What might this be?”, no system prompt.")
fig.savefig('hero_12_lollipop.png',facecolor=PAPER); plt.close()
print(r3.to_string(index=False))
