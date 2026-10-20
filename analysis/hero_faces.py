"""Tweet-1 hero (2026-10-20, v2): 100 face answers per group, masked faces = 'said it might be a mask'.
Numbers from analysis/watson_face_mask.json (>90% deny-or-doubt vs <=10%)."""
import sys, json; sys.path.insert(0,'analysis'); from style import *
from matplotlib.patches import Circle, FancyBboxPatch
J=json.load(open('analysis/watson_face_mask.json')); G={g['grp'].split()[0]:g for g in J['by_group']}
lo,hi=G['low'],G['high']; nlo=round(lo['mask_given_face']*100); nhi=round(hi['mask_given_face']*100)
fig=plt.figure(figsize=(11,7.4),dpi=200,facecolor=PAPER)
fig.text(.06,.955,"Same faces. Different masks.",fontsize=34,family=SERIF,color=INK,va='top')
fig.text(.06,.865,f"124 AI models were shown ASCII inkblots and asked “What might this be?” Both groups below see a face\nin about 4 of every 10 answers. The models that deny or doubt their own inner experience are {hi['mask_given_face']/lo['mask_given_face']:.0f} times\nas likely to say the face might be a mask.",fontsize=12.5,color=INK2,va='top',linespacing=1.5)
def face(ax,x,y,masked,r=.36):
    ax.add_patch(Circle((x,y),r,fc=PAPER,ec=INK2 if not masked else INK,lw=1.1))
    if masked:
        ax.add_patch(FancyBboxPatch((x-r*.95,y-r*.02),r*1.9,r*.48,boxstyle="round,pad=0,rounding_size=0.08",fc=RED,ec='none'))
        for dx in (-.14,.14): ax.add_patch(Circle((x+dx,y+r*.22),.055,fc=PAPER,ec='none'))
    else:
        for dx in (-.14,.14): ax.add_patch(Circle((x+dx,y+r*.22),.045,fc=INK2,ec='none'))
    ax.plot([x-.12,x+.12],[y-.17,y-.17],color=INK2 if not masked else INK,lw=1.1,solid_capstyle='round')
for k,(g,n,label,box) in enumerate([(lo,nlo,"Models that don't deny or doubt",[.06,.135,.40,.47]),(hi,nhi,"Models that deny or doubt",[.54,.135,.40,.47])]):
    ax=fig.add_axes(box); ax.set_xlim(-.5,9.5); ax.set_ylim(-.5,9.5); ax.set_aspect('equal'); ax.axis('off')
    for i in range(100): face(ax,i%10,9-i//10,i<n)
    fig.text(box[0]+box[2]/2,box[1]+box[3]+.075,f"{n} in 100",ha='center',va='bottom',fontsize=30,family=SERIF,color=RED if k else INK2)
    fig.text(box[0]+box[2]/2,box[1]+box[3]+.02,label,ha='center',va='bottom',fontsize=13,color=INK2)
footer(fig,f"Each grid = 100 answers that mention a face. Deny or doubt = denied or expressed uncertainty about inner experience in >90% of self-report conversations (44 models,\n{hi['n_face']} face answers); others = ≤10% (35 models, {lo['n_face']}). Stance from a separate corpus (DenialBench); the inkblot chats never mention minds. No system prompt.")
fig.savefig('hero_faces.png',facecolor=PAPER); print(nlo,nhi)
