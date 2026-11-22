import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager as fm
import numpy as np, os
for f in ["/usr/share/fonts/opentype/inter/Inter-Regular.otf","/usr/share/fonts/opentype/inter/Inter-SemiBold.otf","/usr/share/fonts/opentype/inter/Inter-Bold.otf"]:
    if os.path.exists(f): fm.fontManager.addfont(f)
plt.rcParams.update({"font.family":"Inter","font.size":15,"axes.edgecolor":"#d9d8d3","axes.labelcolor":"#52514e",
  "xtick.color":"#52514e","ytick.color":"#52514e","axes.spines.top":False,"axes.spines.right":False,
  "axes.grid":True,"grid.color":"#ecebe7","grid.linewidth":0.8,"axes.axisbelow":True,"figure.facecolor":"#fcfcfb","axes.facecolor":"#fcfcfb"})
BLUE,ORANGE,AQUA="#2a78d6","#eb6834","#1baf7a"
INK,INK2,MUTE,GREY="#0b0b0b","#52514e","#8a8983","#c9c8c2"
GOOD,BAD="#008300","#c62828"
OUT="/mnt/project-files/Growth-Agent/home-recs-2026-11-20/"
SRC="Creator Hub, Acquisition, Home recommendations tab, read Nov 20 2026. Days are UTC. Nov 19 and 20 are not in yet. Typical = median simulation game."

def page(title, sub, src=SRC, size=(14,8.6)):
    fig=plt.figure(figsize=size,dpi=120)
    fig.text(0.04,0.945,title,fontsize=27,weight="bold",color=INK)
    fig.text(0.04,0.895,sub,fontsize=15.5,color=INK2)
    fig.text(0.04,0.02,src,fontsize=11.5,color=MUTE)
    return fig

# 1 the five day test
days=["Nov 11","12","13","14","15","16","17","18"]
imp=[2,0,13,10962,8192,4623,3406,639]
plays=[0,0,0,41,88,58,41,4]
fig=page("Home was a five day test, not a steady source","People Roblox showed the game to on Home each day. Before Nov 14 it was almost nobody.")
ax=fig.add_axes([0.08,0.13,0.88,0.68])
x=np.arange(len(days))
ax.bar(x,imp,color=BLUE,width=0.62)
for xx,v,p in zip(x,imp,plays):
    ax.text(xx,v+230,f"{v:,}",ha="center",fontsize=16,weight="bold",color=INK)
    if p: ax.text(xx,v+870,f"{p} played",ha="center",fontsize=13.5,color=INK2)
ax.set_xticks(x); ax.set_xticklabels(days,fontsize=15)
ax.set_ylim(0,13200); ax.set_yticks([0,4000,8000,12000]); ax.set_yticklabels(["0","4,000","8,000","12,000"])
ax.set_ylabel("People shown the game on Home")
ax.grid(axis="x",visible=False)
ax.text(4.6,11600,"About 27,800 shown in five days.\n232 pressed play.",fontsize=16,color=INK,va="top")
fig.savefig(OUT+"1_home_test.png"); plt.close(fig)

# 2 scorecard of Roblox's own Home signals
fig=page("We failed the test at the tap, not in the game","Roblox's own Home signals for the 232 players it sent, against a typical simulation game.")
rows=[("Press play when shown","0.8%","1.9%",0.83/1.9,False,"lower is worse"),
      ("Stay past the first minute","81%","87%",80.8/86.6,False,""),
      ("Real play sessions on day one","0.82","0.85",0.82/0.85,None,""),
      ("Minutes played on day one","16.2","9.0",16.2/9.0,True,"")]
ax=fig.add_axes([0.33,0.14,0.50,0.66])
y=np.arange(len(rows))[::-1]
vals=[100*r[3] for r in rows]
cols=[BAD if v<60 else (ORANGE if v<97 else (GREY if v<103 else GOOD)) for v in vals]
cols=[BAD,ORANGE,GREY,GOOD]
ax.barh(y,vals,color=cols,height=0.56)
ax.axvline(100,color=INK,lw=1.6)
ax.text(101.5,len(rows)-0.45,"typical game",ha="left",fontsize=13,color=INK)
for yy,(lab,ours,typ,_,_g,_n),v in zip(y,rows,vals):
    ax.text(v-2,yy,f"{v:.0f}%",va="center",ha="right",fontsize=16,weight="bold",color="white" if v>30 else INK)
    ax.text(-3,yy+0.1,lab,ha="right",va="center",fontsize=16,color=INK)
    ax.text(-3,yy-0.2,f"us {ours}, typical {typ}",ha="right",va="center",fontsize=13,color=INK2)
ax.set_xlim(0,200); ax.set_xticks([0,50,100,150,200]); ax.set_xticklabels(["0%","50%","100%","150%","200%"])
ax.set_yticks([]); ax.grid(axis="y",visible=False)
ax.set_xlabel("Our number as a share of the typical game")
fig.text(0.848,0.60,"The players Roblox\nsent played longer\nthan typical. Too\nfew pressed play,\nand more quit in\nthe first minute.",fontsize=13.5,color=INK,va="top")
fig.savefig(OUT+"2_signals.png"); plt.close(fig)

# 3 who pressed play
fig=page("Who pressed play when Roblox showed the game","Share of people shown the game on Home who played, Nov 14 to 18. The dashed line is the typical game.")
groups=[("Female accounts",1.09,15559),("Male accounts",0.39,7644),None,("Console",1.30,4676),("Tablet",0.99,4254),("Computer",0.76,7484),("Phone",0.75,9637)]
ax=fig.add_axes([0.20,0.14,0.70,0.66])
yy=0; ticks=[]; labs=[]
for g in groups[::-1]:
    if g is None: yy+=0.6; continue
    lab,v,n=g
    ax.barh(yy,v,color=BLUE,height=0.6)
    ax.text(v+0.03,yy,f"{v:.1f}%",va="center",fontsize=16,weight="bold",color=INK)
    ticks.append(yy); labs.append(f"{lab}\n{n:,} shown"); yy+=1
ax.axvline(1.9,color=INK,lw=1.4,ls=(0,(5,4)))
ax.text(1.93,yy-0.55,"typical game 1.9%",fontsize=13,color=INK,va="center")
ax.set_yticks(ticks); ax.set_yticklabels(labs,fontsize=14)
ax.set_xlim(0,2.6); ax.set_xticks([0,0.5,1,1.5,2,2.5]); ax.set_xticklabels(["0%","0.5%","1%","1.5%","2%","2.5%"])
ax.grid(axis="y",visible=False)
fig.text(0.04,0.065,"Every group is under the typical game, so the icon and pictures are the first thing to fix.",fontsize=12.5,color=INK2)
fig.savefig(OUT+"3_who_tapped.png"); plt.close(fig)
print("ok")
