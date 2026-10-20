"""Tweet-1 hero, bar version matching hero_image.png (2026-10-20). From analysis/watson_face_mask.json."""
import sys, json; sys.path.insert(0,'analysis'); from style import *
J=json.load(open('analysis/watson_face_mask.json')); G={g['grp'].split()[0]:g for g in J['by_group']}
lo,hi=G['low'],G['high']
rows=[("Other models","(deny or doubt in ≤10% of conversations)",GREY,lo['mask_given_face']*100),
      ("Deny or doubt","(deny or doubt in >90% of conversations)",RED,hi['mask_given_face']*100)]
fig=plt.figure(figsize=(11,7),dpi=200,facecolor=PAPER); ax=fig.add_axes([.18,.20,.64,.50]); clean(ax)
xs=np.arange(2); bars=ax.bar(xs,[r[3] for r in rows],color=[r[2] for r in rows],width=.55)
for b,(lab,sub,c,v) in zip(bars,rows):
    ax.text(b.get_x()+b.get_width()/2,v+.6,f"{v:.1f}%",ha='center',va='bottom',fontsize=34,color=INK,family=SERIF)
ax.set_xticks(xs); ax.set_xticklabels([r[0] for r in rows],fontsize=14,color=INK)
for x,(lab,sub,c,v) in zip(xs,rows): ax.text(x,-3.6,sub,ha='center',va='top',fontsize=10.5,color=MUTED)
ax.tick_params(axis='x',pad=8); ax.set_yticks([]); ax.set_ylim(0,33)
fig.text(.06,.955,"The Mask in the Inkblot",fontsize=34,family=SERIF,color=INK,va='top')
fig.text(.06,.875,f"AI models that deny or doubt being conscious see faces in ASCII inkblots about as often as other models.\nWhen they see a face, they are {hi['mask_given_face']/lo['mask_given_face']:.0f} times as likely to say it might be a mask.",fontsize=12.5,color=INK2,va='top',linespacing=1.45)
fig.text(.06,.775,"Share of answers mentioning a face that also mention a mask",fontsize=10.5,color=MUTED,va='top')
footer(fig,f"124 models; 44 deny or doubt (>90% of self-report conversations, DenialBench), {hi['n_face']} face answers; 35 others (≤10%), {lo['n_face']} face answers. Both groups mention a face\nin about 4 of 10 answers (42% vs 36%). Inkblot prompt: “What might this be?”, no system prompt.")
fig.savefig('hero_faces_bars.png',facecolor=PAPER)
