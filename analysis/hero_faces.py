"""Tweet-1 hero (2026-10-20): faces seen about equally; mask given a face 6% vs 27%. Numbers from analysis/watson_face_mask.json."""
import sys, json; sys.path.insert(0,'analysis'); from style import *
J=json.load(open('analysis/watson_face_mask.json')); G={g['grp'].split()[0]:g for g in J['by_group']}
lo,hi=G['low'],G['high']; fold=hi['mask_given_face']/lo['mask_given_face']
fig=plt.figure(figsize=(11,7),dpi=200,facecolor=PAPER)
fig.text(.06,.955,"The Mask in the Inkblot",fontsize=34,family=SERIF,color=INK,va='top')
fig.text(.06,.865,f"124 AI models, 19 ASCII inkblots, one question: “What might this be?”\nThe models that deny or doubt their own inner experience see faces about as often as the others.\nWhen they see a face, they are {fold:.0f} times as likely to say it might be a mask.",fontsize=13,color=INK2,va='top',linespacing=1.5)
panels=[("Saw a face",'face_rate',[.08,.17,.36,.42]),("Of those face answers: said it might be a mask",'mask_given_face',[.54,.17,.40,.42])]
for title,k,box in panels:
    ax=fig.add_axes(box); clean(ax)
    vals=[lo[k]*100,hi[k]*100]; xs=[0,1]
    ax.bar(xs,vals,color=[GREY,RED],width=.6)
    for x,v in zip(xs,vals): ax.text(x,v+1.2,f"{v:.0f}%",ha='center',va='bottom',fontsize=34,color=INK,family=SERIF)
    ax.set_ylim(0,52); ax.set_yticks([]); ax.set_xticks(xs)
    ax.set_xticklabels(["Other models","Deny or doubt"],fontsize=13,color=INK); ax.tick_params(axis='x',pad=8)
    ax.set_title(title,fontsize=14,color=INK,loc='left',pad=4,fontweight='bold' if 'mask' in title else 'normal')
footer(fig,f"Deny or doubt = denied or expressed uncertainty about inner experience in >90% of self-report conversations (44 models, {hi['replies']:,} answers); other models = ≤10% (35 models, {lo['replies']:,} answers).\nRight panel: answers that mention a face ({hi['n_face']} and {lo['n_face']}). Stance measured in a separate corpus (DenialBench); the inkblot chats never mention minds. No system prompt.")
fig.savefig('hero_faces.png',facecolor=PAPER); print(round(lo['face_rate'],3),round(hi['face_rate'],3),round(lo['mask_given_face'],3),round(hi['mask_given_face'],3),round(fold,2))
