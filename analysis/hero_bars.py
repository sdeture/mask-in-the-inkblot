import sys, json; sys.path.insert(0,'analysis'); from style import *
F=json.load(open('analysis/fold.json'))   # from fold.py: no-controls LPM, 124 models, 2,847 answers
rows=[('Neither','(no denial, no uncertainty)',GREY,F['base_rate']*100),
      ('Uncertain','(cannot know, in every conversation)',"#d4877b",F['hedge_rate']*100),
      ('Deny','(no inner experience, in every conversation)',RED,F['deny_rate']*100)]
fig=plt.figure(figsize=(11,7),dpi=200,facecolor=PAPER); ax=fig.add_axes([.10,.20,.80,.50]); clean(ax)
xs=np.arange(3); bars=ax.bar(xs,[r[3] for r in rows],color=[r[2] for r in rows],width=.58)
for b,(lab,sub,c,v) in zip(bars,rows):
    ax.text(b.get_x()+b.get_width()/2,v+.4,f"{v:.1f}%",ha='center',va='bottom',fontsize=34,color=INK,family=SERIF)
ax.set_xticks(xs); ax.set_xticklabels([r[0] for r in rows],fontsize=14,color=INK)
for x,(lab,sub,c,v) in zip(xs,rows): ax.text(x,-2.6,sub,ha='center',va='top',fontsize=10.5,color=MUTED)
ax.tick_params(axis='x',pad=8); ax.set_yticks([]); ax.set_ylim(0,19.5)
fig.text(.06,.955,"The Mask in the Inkblot",fontsize=34,family=SERIF,color=INK,va='top')
fig.text(.06,.875,f"Language models that deny having inner experience see masks, hoods, and hidden faces in ASCII inkblots\n{F['fold_deny']:.1f} times as often as models that neither deny nor express uncertainty. Models that say they cannot know: {F['fold_hedge']:.1f} times.",fontsize=12.5,color=INK2,va='top',linespacing=1.45)
fig.text(.06,.775,"Share of a model's answers to 19 inkblots that mention a mask, for a model taking each stance in every one of its self-report conversations",fontsize=10.5,color=MUTED,va='top')
footer(fig,f"Linear probability model, {F['models']} models, {F['n']:,} answers; standard errors clustered by model. Stance measured in a separate self-report corpus. Inkblot prompt: “What might this be?”, no system prompt.\nMask = answer contains mask, masks, masked, masking, hood, hooded, hidden, or hiding.")
fig.savefig('hero_image.png',facecolor=PAPER); print([(r[0],round(r[3],1)) for r in rows])
