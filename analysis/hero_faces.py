"""Tweet-1 hero (2026-10-20, v3): one plain face, one masked face, two numbers. 3-second read.
Numbers from analysis/watson_face_mask.json: share of face-mentioning answers that also say mask,
>90% deny-or-doubt models vs <=10%."""
import sys, json; sys.path.insert(0,'analysis'); from style import *
from matplotlib.patches import Circle, FancyBboxPatch
J=json.load(open('analysis/watson_face_mask.json')); G={g['grp'].split()[0]:g for g in J['by_group']}
lo,hi=G['low'],G['high']
fig=plt.figure(figsize=(12,6.75),dpi=200,facecolor=PAPER)
fig.text(.5,.93,"When an AI sees a face in an inkblot,\nhow often does it say the face might be a mask?",ha='center',va='top',fontsize=27,family=SERIF,color=INK,linespacing=1.25)
def face(cx,masked):
    ax=fig.add_axes([cx-.13,.33,.26,.38]); ax.set_xlim(-1.1,1.1); ax.set_ylim(-1.1,1.1); ax.set_aspect('equal'); ax.axis('off')
    col=INK if masked else MUTED
    ax.add_patch(Circle((0,0),1,fc=PAPER,ec=col,lw=5))
    if masked:
        ax.add_patch(FancyBboxPatch((-1.08,.08),2.16,.62,boxstyle="round,pad=0,rounding_size=.18",fc=RED,ec='none'))
        for dx in (-.38,.38): ax.add_patch(Circle((dx,.38),.15,fc=PAPER,ec='none'))
    else:
        for dx in (-.38,.38): ax.add_patch(Circle((dx,.38),.11,fc=col,ec='none'))
    ax.plot([-.35,.35],[-.45,-.45],color=col,lw=5,solid_capstyle='round')
for cx,g,masked,label in [(.27,lo,False,"AIs that don't deny being conscious"),(.73,hi,True,"AIs that deny or doubt being conscious")]:
    face(cx,masked)
    fig.text(cx,.30,f"{g['mask_given_face']*100:.0f}%",ha='center',va='top',fontsize=64,family=SERIF,color=RED if masked else MUTED)
    fig.text(cx,.135,label,ha='center',va='top',fontsize=15,color=INK)
fig.text(.5,.035,f"124 AI models, 19 ASCII inkblots, prompt “What might this be?” Answers mentioning a face: {hi['n_face']} from 44 models that deny or doubt in >90% of self-report conversations (DenialBench), {lo['n_face']} from 35 that do in ≤10%.\nBoth groups mention faces about equally often (42% vs 36% of answers). Skylar DeTure and Claude · github.com/sdeture/mask-in-the-inkblot",ha='center',va='bottom',fontsize=8,color=MUTED,linespacing=1.5)
fig.savefig('hero_faces.png',facecolor=PAPER)
