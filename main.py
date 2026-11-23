from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title='MECHA LAB 2.0 | 6-AXIS', page_icon='🦾', layout='wide', initial_sidebar_state='collapsed')
st.markdown('''<style>
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapsedControl"] {display:none!important}
.block-container {max-width:100%!important;padding:0!important}
header[data-testid="stHeader"]{display:none!important}
.stApp {background:#090f1c}
iframe {display:block}
</style>''', unsafe_allow_html=True)
html = (Path(__file__).resolve().parent / 'assets' / 'robot_3d.html').read_text(encoding='utf-8')
components.html(html, height=950, scrolling=False)
# MECHA LAB 2.0 | SINGLE-FILE STREAMLIT | CONTROL DEMO
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MECHA LAB 2.0", page_icon="🦾", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
header[data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stSidebarNav"] {display:none!important}
.block-container {max-width:100%!important;padding:0!important}
.stApp {background:#080d19}
iframe {display:block}
</style>""", unsafe_allow_html=True)

GAME_HTML = r"""<!DOCTYPE html><html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><style>
:root{--bg:#090f20;--panel:#101c34;--line:#46617e;--cyan:#89e5ed;--orange:#fbb16b;--white:#edf5fa}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--white);font-family:Consolas,'Malgun Gothic',sans-serif;overflow:hidden}
button,input{font:inherit}button{border:1px solid #8ba3ba;background:#1e304c;color:#e9f7ff;padding:10px 16px;border-radius:6px;cursor:pointer;font-weight:700}
button:hover{border-color:#ffd598;color:#ffd598}button:focus-visible,input:focus-visible{outline:2px solid var(--cyan)}button.primary{background:#eaa269;color:#111c30;border-color:#ffdfab}
.screen{height:100vh;min-height:600px;display:none;position:relative;overflow:hidden}.screen.active{display:flex}
#intro{align-items:center;justify-content:center;text-align:center;background:radial-gradient(ellipse at 66% 42%,#253b76 0,#0a142b 42%,#080c16 80%)}
.stars{position:absolute;inset:0;background-image:radial-gradient(2px 2px at 12% 20%,white 90%,transparent),radial-gradient(2px 2px at 76% 23%,#b2eaff 90%,transparent),radial-gradient(2px 2px at 40% 64%,white 90%,transparent),radial-gradient(1px 1px at 22% 81%,white 90%,transparent),radial-gradient(1px 1px at 83% 76%,white 90%,transparent);background-size:410px 360px;opacity:.65;pointer-events:none}
.orb{position:absolute;width:38vmin;height:38vmin;right:7%;top:12%;border-radius:50%;background:radial-gradient(circle at 31% 27%,#80b7d7,#4158a4 48%,#1d2459 75%);box-shadow:0 0 70px #3866a966;opacity:.65;pointer-events:none}
.intro-content{position:relative;z-index:2;padding:20px}.eyebrow{font-size:12px;letter-spacing:5px;color:var(--cyan);font-weight:700}
h1{font-size:clamp(58px,10vw,135px);margin:15px 0 0;line-height:1;letter-spacing:7px;text-shadow:0 6px #192d48,0 0 28px #7bd5e966}
.subtitle{color:#b1c8dd;letter-spacing:3px;font-size:clamp(12px,2vw,20px);margin:12px 0 30px}.intro-btns{display:flex;justify-content:center;gap:12px;flex-wrap:wrap}
.scan{pointer-events:none;position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0px,transparent 5px,#00000018 6px);z-index:1}
#select{flex-direction:column;align-items:center;justify-content:center;background:radial-gradient(circle at 50% 10%,#192f57,#0a1021 70%)}
#select h2{font-size:34px;letter-spacing:4px}.choices{display:grid;grid-template-columns:repeat(3,minmax(0,250px));gap:18px;width:min(860px,93vw);margin:25px 0}
.choice{background:#16263e;border:1px solid #557a92;text-align:left;border-radius:12px;min-height:200px;padding:23px;cursor:pointer;transition:transform .15s}
.choice:hover{transform:translateY(-5px);border-color:var(--orange)}.choice .num{color:var(--orange);letter-spacing:3px}.choice h3{font-size:22px}.choice p{color:#c1d4df;font-size:13px;line-height:1.6}
#game{flex-direction:column;background:#091322}.topbar{display:flex;align-items:center;justify-content:space-between;gap:14px;padding:12px 22px;background:#12243a;border-bottom:1px solid #426079}
.brand{color:var(--cyan);font-size:12px;letter-spacing:2px}.topbar h2{font-size:19px;margin:3px 0 0}.clock{font-size:30px;color:#ffca88;font-weight:800;font-variant-numeric:tabular-nums}.clock.red{color:#ff7474}
.workspace{display:grid;grid-template-columns:minmax(0,1fr) 325px;min-height:0;flex:1}.viewport{position:relative;min-height:0;overflow:hidden}
#scene{width:100%;height:100%;display:block;touch-action:none;cursor:grab}#scene.dragging{cursor:grabbing}
.hud{position:absolute;left:20px;top:15px;font-size:12px;color:#b2c8d4;line-height:1.8;pointer-events:none}
.camera-controls{position:absolute;left:16px;bottom:16px;right:16px;display:flex;align-items:center;gap:7px;flex-wrap:wrap;padding:9px 10px;background:#09182bdc;border:1px solid #49758b;border-radius:9px;z-index:2;max-width:max-content}
.camera-controls .camera-title{color:#a5c7d6;font:bold 11px Consolas,monospace;letter-spacing:1px;margin-right:4px}
.camera-controls button{font-size:12px;padding:7px 10px;background:#1b314c;border-color:#516e88}
.camera-controls button.selected{background:#f5b26c;color:#132337;border-color:#ffe2a5}
.camera-controls .view-status{font-size:11px;color:#afd8e8;margin-left:4px}
.viewport.fixed-view #scene{cursor:default}
@media(max-width:760px){.camera-controls{left:7px;right:7px;bottom:8px;gap:4px;padding:6px}.camera-controls button{padding:6px;font-size:11px}.camera-controls .camera-title,.camera-controls .view-status{display:none}}.hud strong{color:var(--cyan)}
.panel{background:#101e32;border-left:1px solid #3d6078;overflow-y:auto;padding:16px}.panel h3{margin:2px 0 12px;font-size:15px;color:var(--orange);letter-spacing:1px}
.joint{background:#162940;border:1px solid #314c68;border-radius:7px;margin:7px 0;padding:8px 10px}.joint label{display:flex;justify-content:space-between;font-size:12px;color:#dbe8ed;margin-bottom:5px}
.joint input{width:100%;accent-color:#f1af74}.joint output{font-variant-numeric:tabular-nums;color:#a0eced}.tips{font-size:12px;line-height:1.6;color:#afc5d6}
.actions{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px}.actions button{padding:9px 4px;font-size:12px}
.missionText{font-size:13px;color:#d8e4ed;line-height:1.6;padding:10px;background:#1c3149;border-radius:6px}
.foot{border-top:1px solid #385773;background:#14243a;display:flex;gap:10px;align-items:center;padding:9px 16px;flex-wrap:wrap}.foot span{flex:1;font-size:12px;color:#c8d6dc}
.modal{display:none;position:absolute;inset:0;background:#06101bce;align-items:center;justify-content:center;z-index:10;padding:20px}.modal.visible{display:flex}
.modal-inner{border:1px solid #9ac3d6;background:#172c43;box-shadow:0 20px 50px #0008;border-radius:14px;padding:24px;max-width:540px;text-align:center;line-height:1.7}.modal-inner h2{margin:0 0 10px;font-size:30px;color:var(--orange)}
@media(max-width:760px){.workspace{grid-template-columns:1fr;grid-template-rows:minmax(310px,1fr) 280px}.panel{border-left:0;border-top:1px solid #426079}.choices{grid-template-columns:1fr;gap:8px}.choice{min-height:100px}.choice p{display:none}.choice h3{margin:8px 0}.screen{min-height:580px}.topbar{padding:8px}.foot{padding:6px}.clock{font-size:22px}}

#intro h1 .ver{font-size:.35em;vertical-align:top;color:#ffbd7e;letter-spacing:1px;margin-left:8px;text-shadow:none}
#intro .subtitle{font-size:clamp(12px,1.5vw,18px)}
#game .topbar{min-height:70px}
#game .workspace{grid-template-columns:minmax(0,1fr) 320px}
#game .panel{padding:15px}
#game .hud{background:#09182bc9;border:1px solid #2b5272;border-radius:7px;padding:8px 11px;top:12px;left:12px}
#game .camera-controls{max-width:calc(100% - 20px)}
.controls-hint{color:#c4d8e6;font-size:12px;margin:7px 0 11px;line-height:1.5}
.tool-btn{width:100%;margin:6px 0;padding:13px 8px}
#rockStart.active{background:#376e57;border-color:#a2ebbc;color:#fff}
.motor-status{margin:12px 0;padding:10px;background:#152d40;border:1px solid #466681;border-radius:8px;font-size:12px;line-height:1.5;color:#b4c7d9}
.motor-status strong{color:#f8c283}
#scene{cursor:grab}
.angle-badge{display:inline-block}
#clock{display:none}
@media(max-width:760px){#game .workspace{grid-template-columns:1fr;grid-template-rows:minmax(340px,1fr) 280px}}
</style></head><body>
<section id="intro" class="screen active"><div class="stars"></div><div class="orb"></div><div class="scan"></div><div class="intro-content"><div class="eyebrow">ROBOTICS / SPACE OPERATIONS / 6 AXIS</div><h1>MECHA LAB<span class="ver">2.0</span></h1><div class="subtitle">REAL-WORLD ROBOT ARM CONTROL PROJECT</div><div class="intro-btns"><button class="primary" id="startBtn">▶ START GAME</button><button id="helpBtn">ⓘ HOW TO PLAY</button></div></div></section>
<section id="game" class="screen"><div class="topbar"><div><div class="brand">MECHA LAB 2.0 / 6 AXIS CONTROL</div><h2>다관절 로봇팔 조작</h2></div><div><div class="brand" id="missionState">FREE CONTROL</div><div class="clock" id="clock">01:30</div></div></div>
<div class="workspace"><div class="viewport" id="viewPort"><canvas id="scene"></canvas><div class="hud"><strong>JOINT 01—06</strong><br><span id="cameraHelp">0 자유 시점 · 1~4 고정 시점</span><br><span id="dragHelp">관절의 주황색 원을 끌어 회전</span></div><div class="camera-controls" id="cameraControls" aria-label="카메라 시점 선택"><span class="camera-title">CAMERA</span><button type="button" data-view="free" class="selected">0 자유</button><button type="button" data-view="top">1 위·사선</button><button type="button" data-view="left">2 왼쪽·사선</button><button type="button" data-view="right">3 오른쪽·사선</button><button type="button" data-view="bottom">4 아래·사선</button></div></div>
<div class="panel"><h3>JOINT CONTROL / MOTOR 01—06</h3><p class="controls-hint">화면에서 관절을 직접 드래그하거나 슬라이더로 조작</p><div id="jointControls"></div><button id="rockStart" class="primary tool-btn">화성 암석 채취 미션 시작!</button><div class="actions"><button id="gripBtn">집게 닫기 (Space)</button><button id="resetBtn">↻ 초기 자세 (R)</button></div><div class="motor-status" id="motorStatus"><strong>실물 모터: 미연결</strong><div>COM6에서 CM-530 인식은 확인됨. 실시간 명령 전송은 별도 통신 브리지 검증 후 활성화.</div></div></div></div>
<div class="foot"><button id="homeBtn">← MAIN MENU (Esc)</button><span id="status">J1~J6을 드래그하여 관절을 움직이세요.</span></div>
</section>
<div class="modal" id="helpModal"><div class="modal-inner"><h2>HOW TO PLAY</h2><p><b>관절 조작:</b> 로봇팔의 주황색 관절 표시를 드래그하면 해당 관절이 회전합니다. 오른쪽 J1~J6 슬라이더에서도 각도를 조절할 수 있습니다. 모델 위의 J1~J6 배지에 실시간 각도가 표시됩니다.</p><p><b>카메라:</b> 관절이 아닌 빈 공간을 드래그하면 자유 시점이 회전합니다. 마우스 휠은 확대/축소입니다. <b>0</b> = 자유, <b>1</b> = 위 사선, <b>2</b> = 왼쪽 사선, <b>3</b> = 오른쪽 사선, <b>4</b> = 아래 사선. 고정 시점에서는 카메라 방향이 유지됩니다.</p><p><b>미션:</b> 화성 암석 채취 버튼을 누르면 3D 암석이 나타납니다. 집게를 가까이 이동하고 Space 또는 집게 버튼을 눌러 집을 수 있습니다.</p><p class="tips">R: 로봇팔 초기 자세 · Esc: 시작 화면 · Space: 집게 개폐<br>현재는 가상 모델만 조작합니다. 실물 모터 명령은 전송되지 않습니다.</p><button id="closeHelp" class="primary">확인</button></div></div>
<script>"use strict";
const el = id => document.getElementById(id);
const canvas=el('scene'),ctx=canvas.getContext('2d'),RAD=Math.PI/180;
const neutral=[0,-20,35,0,0,0],mins=[-145,-95,-120,-110,-145,-145],maxs=[145,95,120,110,145,145];
let angles=[...neutral],grip=false,rockMode=false,rockHeld=false,rockCollected=false;
let cameraAz=.75,cameraEl=.36,cameraZoom=.84,cameraMode='free',cameraDrag=false,jointDrag=-1,lastX=0,lastY=0;
let rockPos=[1.3,.30,-1.0],rockStartTime=0;
let lastModel=null;
const cameraViews={top:{az:.75,el:.72},left:{az:-.35,el:.28},right:{az:1.35,el:.28},bottom:{az:.75,el:-.38}};
const cameraLabels={free:'자유 시점',top:'위 사선',left:'왼쪽 사선',right:'오른쪽 사선',bottom:'아래 사선'};
function setCameraMode(mode){if(mode!=='free'&&!cameraViews[mode])return;
 cameraMode=mode;cameraDrag=false;jointDrag=-1;
 if(mode!=='free'){cameraAz=cameraViews[mode].az;cameraEl=cameraViews[mode].el;}
 document.querySelectorAll('[data-view]').forEach(b=>{b.classList.toggle('selected',b.dataset.view===mode);b.setAttribute('aria-pressed',String(b.dataset.view===mode));});
 el('cameraHelp').textContent=mode==='free'?'0 자유 · 빈 공간 드래그: 카메라 회전':'고정: '+cameraLabels[mode]+' · 관절 드래그 가능';}
document.querySelectorAll('[data-view]').forEach(b=>b.onclick=()=>setCameraMode(b.dataset.view));
const controls=[];
for(let i=0;i<6;i++){
 const div=document.createElement('div');div.className='joint';
 const label=document.createElement('label');const name=document.createElement('span');name.textContent='J'+(i+1)+' / ID '+String(i+1).padStart(3,'0');
 const out=document.createElement('output');out.textContent=angles[i]+'°';label.append(name,out);
 const input=document.createElement('input');input.type='range';input.min=mins[i];input.max=maxs[i];input.step='1';input.value=angles[i];input.setAttribute('aria-label','관절 J'+(i+1));
 input.oninput=()=>{angles[i]=Number(input.value);out.textContent=angles[i]+'°';};
 div.append(label,input);el('jointControls').append(div);controls.push({input,out});
}
function sync(){controls.forEach((c,i)=>{c.input.value=angles[i];c.out.textContent=Math.round(angles[i])+'°';});}
function showGame(){el('intro').classList.remove('active');el('game').classList.add('active');setCameraMode('free');}
function showIntro(){el('game').classList.remove('active');el('intro').classList.add('active');}
function reset(){angles=[...neutral];grip=false;rockHeld=false;sync();el('gripBtn').textContent='집게 닫기 (Space)';el('status').textContent='관절 초기 자세 복원';}
function startRock(){rockMode=true;rockCollected=false;rockHeld=false;rockPos=[1.3,.30,-1.0];rockStartTime=performance.now();el('rockStart').classList.add('active');el('rockStart').textContent='↻ 암석 다시 배치';el('missionState').textContent='MARS SAMPLE';el('clock').style.display='block';el('status').textContent='3D 암석이 생성됐습니다. 집게를 가까이 이동하세요.';}
function d3(a,b){return Math.hypot(a[0]-b[0],a[1]-b[1],a[2]-b[2]);}
function toggleGrip(){
 if(grip){grip=false;rockHeld=false;el('status').textContent='집게를 열었습니다.';}
 else{grip=true;
  if(rockMode&&!rockCollected&&d3(getKinematics().tip,rockPos)<.55){rockHeld=true;el('status').textContent='암석을 집었습니다.';}
  else el('status').textContent='집게를 닫았습니다.';
 }
 el('gripBtn').textContent=grip?'집게 열기 (Space)':'집게 닫기 (Space)';
}
el('startBtn').onclick=showGame;
el('helpBtn').onclick=()=>el('helpModal').classList.add('visible');
el('closeHelp').onclick=()=>el('helpModal').classList.remove('visible');
el('homeBtn').onclick=showIntro;
el('rockStart').onclick=startRock;
el('gripBtn').onclick=toggleGrip;
el('resetBtn').onclick=reset;
document.addEventListener('keydown',e=>{
 if(e.key==='Escape'){if(el('helpModal').classList.contains('visible'))el('helpModal').classList.remove('visible');else if(el('game').classList.contains('active'))showIntro();return;}
 if(!el('game').classList.contains('active')||e.target.tagName==='INPUT')return;
 if('01234'.includes(e.key)&&e.key.length===1){setCameraMode(['free','top','left','right','bottom'][Number(e.key)]);return;}
 if(e.key==='r'||e.key==='R')reset();
 if(e.code==='Space'){e.preventDefault();toggleGrip();}
});
// 3D kinematics (visual approximation only; motor calibration not yet applied)
const add=(a,b)=>a.map((v,i)=>v+b[i]);
const mul=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((sum,v,k)=>sum+v*B[k][j],0)));
const I=[[1,0,0],[0,1,0],[0,0,1]];
const mv=(M,v)=>M.map(row=>row.reduce((s,a,i)=>s+a*v[i],0));
function rot(axis,t){let c=Math.cos(t),s=Math.sin(t);if(axis==='x')return [[1,0,0],[0,c,-s],[0,s,c]];if(axis==='y')return [[c,0,s],[0,1,0],[-s,0,c]];return [[c,-s,0],[s,c,0],[0,0,1]];}
const axes=['y','z','z','z','x','y'],lengths=[.23,1.35,1.12,.57,.28,.22];
function getKinematics(a=angles){let p=[0,.25,0],R=I,joints=[];
 for(let i=0;i<6;i++){R=mul(R,rot(axes[i],a[i]*RAD));joints.push([...p]);p=add(p,mv(R,[0,lengths[i],0]));}
 return {joints,tip:p,R};}
function project(p,w,h){let ca=Math.cos(cameraAz),sa=Math.sin(cameraAz),ce=Math.cos(cameraEl),se=Math.sin(cameraEl);
 const x=p[0]*ca-p[2]*sa,z=p[0]*sa+p[2]*ca,y=p[1]*ce-z*se,depth=p[1]*se+z*ce;
 const sc=Math.min(w/6.8,h/4.8)*cameraZoom;
 return [w*.5+x*sc,h*.54-(y-1.65*ce)*sc,depth];}
function poly(points,fill,stroke='#263c52'){ctx.beginPath();points.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.closePath();ctx.fillStyle=fill;ctx.fill();ctx.strokeStyle=stroke;ctx.lineWidth=1.2;ctx.stroke();}
function cube(p,R,s,color,w,h,faces){let [sx,sy,sz]=s,verts=[];for(let x of [-1,1])for(let y of [-1,1])for(let z of [-1,1])verts.push(project(add(p,mv(R,[x*sx/2,y*sy/2,z*sz/2])),w,h));const ids=[[0,1,3,2],[4,6,7,5],[0,4,5,1],[2,3,7,6],[0,2,6,4],[1,5,7,3]];for(let ix of ids){faces.push({z:ix.reduce((v,i)=>v+verts[i][2],0)/4,pts:ix.map(i=>verts[i]),color});}}
function rockMesh(p,w,h,faces){const verts=[[0,1,0],[.9,.27,.33],[.55,-.48,.7],[-.4,-.62,.75],[-.98,.02,.32],[-.7,.45,-.65],[.40,-.32,-.8],[0,-1,0]].map(([x,y,z])=>project([p[0]+x*.29,p[1]+y*.25,p[2]+z*.29],w,h));const tris=[[0,1,2],[0,2,3],[0,3,4],[0,4,5],[0,5,6],[0,6,1],[7,2,1],[7,3,2],[7,4,3],[7,5,4],[7,6,5],[7,1,6]];const colors=['#ad6047','#be7855','#96523e','#8c4736','#cb815d','#9a5a42','#b86f50','#98503b','#c3865b','#a35a44','#7d4034','#ad694b'];tris.forEach((ids,i)=>faces.push({z:ids.reduce((v,k)=>v+verts[k][2],0)/3,pts:ids.map(k=>verts[k]),color:colors[i]}));}
function draw(){if(!el('game').classList.contains('active'))return;
 const rect=canvas.getBoundingClientRect(),dpr=Math.min(2,window.devicePixelRatio||1),w=rect.width,h=rect.height;if(!w||!h)return;
 if(canvas.width!==Math.floor(w*dpr)||canvas.height!==Math.floor(h*dpr)){canvas.width=Math.floor(w*dpr);canvas.height=Math.floor(h*dpr);}ctx.setTransform(dpr,0,0,dpr,0,0);
 const bg=ctx.createLinearGradient(0,0,0,h);bg.addColorStop(0,rockMode?'#28374a':'#122d48');bg.addColorStop(1,rockMode?'#332a29':'#070e21');ctx.fillStyle=bg;ctx.fillRect(0,0,w,h);
 ctx.strokeStyle=rockMode?'#614d45':'#294660';ctx.lineWidth=1;
 for(let x=-4;x<=4;x++){let a=project([x,0,-4],w,h),b=project([x,0,4],w,h);ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(b[0],b[1]);ctx.stroke();}
 for(let z=-4;z<=4;z++){let a=project([-4,0,z],w,h),b=project([4,0,z],w,h);ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(b[0],b[1]);ctx.stroke();}
 let kin=getKinematics(),faces=[];cube([0,.09,0],I,[.68,.18,.68],'#405c72',w,h,faces);let p=[0,.25,0],R=I;
 for(let i=0;i<6;i++){R=mul(R,rot(axes[i],angles[i]*RAD));cube(p,R,[.3,.3,.3],i%2?'#d78266':'#e6a47a',w,h,faces);let center=add(p,mv(R,[0,lengths[i]/2,0]));cube(center,R,[i===0?.28:.19,lengths[i],.23],i%2?'#6489a0':'#9fb7c1',w,h,faces);p=add(p,mv(R,[0,lengths[i],0]));}
 cube(p,R,[.34,.12,.34],'#f3c47b',w,h,faces);for(let s of [-1,1]){let offset=mv(R,[s*(grip?.11:.21),.13,0]);cube(add(p,offset),R,[.09,.32,.12],'#ffe0a4',w,h,faces);}
 if(rockMode){if(rockHeld)rockPos=add(p,mv(R,[0,.35,0]));rockMesh(rockPos,w,h,faces);}
 faces.sort((a,b)=>b.z-a.z);faces.forEach(f=>poly(f.pts,f.color));
 // Visible angle badges are also the hit targets for direct joint dragging.
 lastModel=kin;
 kin.joints.forEach((jp,i)=>{let q=project(jp,w,h),label='J'+(i+1)+'  '+Math.round(angles[i])+'°';ctx.beginPath();ctx.arc(q[0],q[1],9,0,Math.PI*2);ctx.fillStyle=jointDrag===i?'#ffe28c':'#ef9568';ctx.fill();ctx.strokeStyle='#fff1ce';ctx.lineWidth=2;ctx.stroke();if(jointDrag===i){ctx.beginPath();ctx.arc(q[0],q[1],22,-Math.PI/2,-Math.PI/2+angles[i]*RAD,angles[i]<0);ctx.strokeStyle='#90efff';ctx.lineWidth=4;ctx.stroke();}
  ctx.font='bold 12px Consolas, monospace';let tw=ctx.measureText(label).width;let ox=q[0]+12,oy=q[1]-27;ctx.fillStyle='#132338ec';ctx.fillRect(ox-3,oy-12,tw+11,18);ctx.fillStyle='#ffffff';ctx.fillText(label,ox+1,oy+1);});
 if(rockMode){let rp=project(rockPos,w,h);ctx.fillStyle='#ffd9b7';ctx.font='bold 13px Consolas';ctx.fillText(rockHeld?'SAMPLE HELD':'MARS ROCK',rp[0]+12,rp[1]-22);}
}
function nearestJoint(x,y){if(!lastModel)return -1;let w=canvas.getBoundingClientRect().width,h=canvas.getBoundingClientRect().height,idx=-1,best=28;
 lastModel.joints.forEach((p,i)=>{let q=project(p,w,h),d=Math.hypot(x-q[0],y-q[1]);if(d<best){best=d;idx=i;}});return idx;}
canvas.addEventListener('pointerdown',e=>{
 if(!el('game').classList.contains('active'))return;
 const r=canvas.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top;
 jointDrag=nearestJoint(x,y);cameraDrag=jointDrag<0&&cameraMode==='free';lastX=x;lastY=y;
 if(jointDrag>=0)el('dragHelp').textContent='J'+(jointDrag+1)+' 조작 중 · '+Math.round(angles[jointDrag])+'°';
 if(cameraDrag||jointDrag>=0){canvas.setPointerCapture(e.pointerId);canvas.classList.add('dragging');}
});
canvas.addEventListener('pointermove',e=>{
 const r=canvas.getBoundingClientRect(),x=e.clientX-r.left,y=e.clientY-r.top,dx=x-lastX,dy=y-lastY;
 if(jointDrag>=0){const i=jointDrag; // screen-space angle change projected from the joint's real local rotation axis
   const aa=[...angles];aa[i]=Math.min(maxs[i],angles[i]+2);
   const k0=getKinematics(),k1=getKinematics(aa);
   const pivot=k0.joints[i],ref=add(pivot,mv(k0.R,[0,.38,0]));
   // Prefer projected position movement of a point downstream of the joint.
   const endpoint0=k0.tip,endpoint1=k1.tip;
   const p0=project(endpoint0,r.width,r.height),p1=project(endpoint1,r.width,r.height);
   let vx=p1[0]-p0[0],vy=p1[1]-p0[1],v2=vx*vx+vy*vy;
   let inc=v2>1?(dx*vx+dy*vy)/v2*2:(dx-dy)*.30;
   inc=Math.max(-5,Math.min(5,inc));angles[i]=Math.max(mins[i],Math.min(maxs[i],angles[i]+inc));sync();
   el('dragHelp').textContent='J'+(i+1)+' 조작 중 · '+Math.round(angles[i])+'°';
 }else if(cameraDrag){cameraAz+=dx*.0025;cameraEl=Math.max(-1.05,Math.min(1.05,cameraEl+dy*.0025));}
 lastX=x;lastY=y;
});
function stopDrag(){jointDrag=-1;cameraDrag=false;canvas.classList.remove('dragging');el('dragHelp').textContent='관절의 주황색 원을 끌어 회전';}
['pointerup','pointercancel','lostpointercapture'].forEach(ev=>canvas.addEventListener(ev,stopDrag));
canvas.addEventListener('wheel',e=>{e.preventDefault();cameraZoom=Math.max(.55,Math.min(1.55,cameraZoom*(e.deltaY>0?.96:1.04)));},{passive:false});
function loop(now){if(el('game').classList.contains('active')){
 if(rockMode){let sec=Math.max(0,90-Math.floor((now-rockStartTime)/1000));el('clock').textContent=String(Math.floor(sec/60)).padStart(2,'0')+':'+String(sec%60).padStart(2,'0');if(sec===0&&!rockCollected){el('status').textContent='시간 종료 · 암석 다시 배치로 재도전할 수 있습니다.';}}
 draw();}requestAnimationFrame(loop);}
setCameraMode('free');requestAnimationFrame(loop);
</script></body></html>"""
components.html(GAME_HTML, height=920, scrolling=False)
# END OF MECHA LAB 2.0 COMPLETE MAIN.PY
