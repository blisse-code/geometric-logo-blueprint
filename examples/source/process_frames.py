import math, json, sys
OUT=sys.argv[1]
BG="#16181D"; INK="#ECE7DF"; K="#FF6A3D"; G="#8A93A6"
C=256; R=120; W=48; SAFE=224
def pt(a,r=R): t=math.radians(a); return (C+r*math.cos(t), C+r*math.sin(t))
def arc(a0,a1,r=R):
    if abs(a1-a0)<0.01: return ""
    p0,p1=pt(a0,r),pt(a1,r); lg=1 if abs(a1-a0)>180 else 0; sw=1 if a1>a0 else 0
    return f"M{p0[0]:.2f} {p0[1]:.2f} A{r} {r} 0 {lg} {sw} {p1[0]:.2f} {p1[1]:.2f}"
def circ(r,p,col,sw=1.5,dash="",op=1):  # partial circle drawn from -90
    if p<=0: return ""
    if p>=1: return f'<circle cx="{C}" cy="{C}" r="{r}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-opacity="{op}" {dash}/>'
    return f'<path d="{arc(-90,-90+360*p,r)}" fill="none" stroke="{col}" stroke-width="{sw}" stroke-opacity="{op}" {dash}/>'
def line(x1,y1,x2,y2,p,col,sw=1.5,op=1,dash=""):
    if p<=0: return ""
    return f'<line x1="{x1:.2f}" y1="{y1:.2f}" x2="{x1+(x2-x1)*p:.2f}" y2="{y1+(y2-y1)*p:.2f}" stroke="{col}" stroke-width="{sw}" stroke-opacity="{op}" stroke-linecap="round" {dash}/>'
def text(x,y,s,col=K,size=13,op=1): return f'<text x="{x}" y="{y}" font-family="Roboto Mono" font-size="{size}" fill="{col}" fill-opacity="{op}">{s}</text>'
TAIL0=pt(math.degrees(math.atan2(-160,-120))); TAIL1=(136,96)
def mark(p_ring,p_tail,p_dot,op=1,col=INK):
    s=""
    if p_ring>0: s+=f'<path d="{arc(0,0+315*p_ring)}" fill="none" stroke="{col}" stroke-width="{W}" stroke-linecap="round" opacity="{op}"/>'
    if p_tail>0: s+=line(TAIL0[0],TAIL0[1],TAIL1[0],TAIL1[1],p_tail,col,W,op)
    if p_dot>0: s+=f'<circle cx="{C}" cy="{C}" r="{24*p_dot:.2f}" fill="{col}" opacity="{op}"/>'
    return s
STEPS=[("1","Fix the frame: crop circle + safe circle (7/8)",10),
       ("2","Pick a module: 8px unit, 32px grid",6),
       ("3","One primitive: circle R120, stroke 48",12),
       ("4","Angles by halving only: 90° and 45°",8),
       ("5","Place by rule: 3:4:5 triangle lands on the safe circle",12),
       ("6","Draw only what the rules give you",14),
       ("7","Remove the scaffolding",10),
       ("8","Crop test: nothing touches the edge",12)]
frames=[]
def ease(x): x=max(0,min(1,x)); return x*x*(3-2*x)
for si,(num,label,n) in enumerate(STEPS):
    for f in range(n):
        p=ease((f+1)/n*1.15)
        st={i:(1 if i<si else (p if i==si else 0)) for i in range(len(STEPS))}
        cons_op=1-st[6]
        s=[f'<rect width="512" height="576" fill="{BG}"/>']
        # grid
        go=0.16*st[1]*cons_op
        if go>0: s+=[f'<path d="M{i} 0V512M0 {i}H512" stroke="{G}" stroke-opacity="{go:.3f}"/>' for i in range(32,512,32)]
        # crop + safe
        if cons_op>0 or si==7:
            s.append(circ(256,st[0],G,1.5,op=max(cons_op,0)))
            s.append(circ(SAFE,st[0],G,1.5,'stroke-dasharray="6 5"',op=max(cons_op,0)))
        if st[0]>0.6 and si<6: s.append(text(372,40,"crop r256",G,12)); s.append(text(372,58,"safe r224",G,12))
        # primitive
        if cons_op>0:
            s.append(circ(R,st[2],K,1.5,op=cons_op))
            e=max(0,(st[2]-0.6)/0.4) if si==2 else st[2]
            if e>0:
                s.append(circ(R-W/2,e,K,1,'stroke-dasharray="3 4"',op=cons_op)); s.append(circ(R+W/2,e,K,1,'stroke-dasharray="3 4"',op=cons_op))
            for k,a in enumerate(range(0,360,45)):
                q=max(0,min(1,st[3]*8-k)) if si==3 else st[3]
                o=pt(a,SAFE); s.append(line(C,C,o[0],o[1],q,G,1,0.7*cons_op))
            if st[4]>0:
                q=st[4]*3
                s.append(line(C,C,136,256,min(1,q),K,2,cons_op)); s.append(line(136,256,136,96,max(0,min(1,q-1)),K,2,cons_op)); s.append(line(136,96,C,C,max(0,min(1,q-2)),K,2,cons_op))
                if st[4]>0.7:
                    s.append(text(186,276,"3",K,14,cons_op)); s.append(text(116,184,"4",K,14,cons_op)); s.append(text(196,170,"5",K,14,cons_op))
                    s.append(f'<circle cx="136" cy="96" r="24" fill="none" stroke="{K}" stroke-width="1" stroke-opacity="{cons_op}"/>')
        # mark
        if st[5]>0:
            pr=min(1,st[5]*1.6); pt_=max(0,min(1,st[5]*2.5-1.2)); pd=max(0,min(1,st[5]*3-2))
            s.append(mark(pr,pt_,pd,0.35+0.65*st[6]))
        # crop mask
        if st[7]>0:
            rr=256+(1-st[7])*120
            s.append(f'<circle cx="{C}" cy="{C}" r="{rr+300:.1f}" fill="none" stroke="#000" stroke-opacity=".55" stroke-width="600"/>')
            s.append(circ(SAFE,1,INK,1,'stroke-dasharray="4 6"',op=0.35*st[7]))
        # caption band
        s.append(f'<rect y="512" width="512" height="64" fill="#0E0F13"/>')
        s.append(text(20,550,f"{num}/8",K,15)); s.append(text(64,550,label,INK,13))
        frames.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 576" width="512" height="576">{"".join(s)}</svg>')
json.dump(frames,open(OUT,"w"))
# final mark alone for scale test
open(OUT.replace(".json","_mark.svg"),"w").write(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512"><rect width="512" height="512" fill="{BG}"/>{mark(1,1,1)}</svg>')
print(len(frames))
