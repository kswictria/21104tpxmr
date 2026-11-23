# MECHA LAB 2.0 | STANDALONE STREAMLIT | 2026-11-23
# Single-file simulation. No motor commands are sent.
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MECHA LAB 2.0", page_icon="🦾", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
header[data-testid="stHeader"], [data-testid="stSidebar"], [data-testid="stSidebarNav"] {display:none !important;}
.block-container {max-width:100% !important; padding:0 !important;}
.stApp {background:#080d19;}
[data-testid="stAppViewContainer"] {padding:0 !important;}
iframe {display:block;}
</style>""", unsafe_allow_html=True)

GAME_HTML = r"""<!DOCTYPE html>
<html lang="ko"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<style>
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
.hud{position:absolute;left:20px;top:15px;font-size:12px;color:#b2c8d4;line-height:1.8;pointer-events:none}.hud strong{color:var(--cyan)}
.panel{background:#101e32;border-left:1px solid #3d6078;overflow-y:auto;padding:16px}.panel h3{margin:2px 0 12px;font-size:15px;color:var(--orange);letter-spacing:1px}
.joint{background:#162940;border:1px solid #314c68;border-radius:7px;margin:7px 0;padding:8px 10px}.joint label{display:flex;justify-content:space-between;font-size:12px;color:#dbe8ed;margin-bottom:5px}
.joint input{width:100%;accent-color:#f1af74}.joint output{font-variant-numeric:tabular-nums;color:#a0eced}.tips{font-size:12px;line-height:1.6;color:#afc5d6}
.actions{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin-top:12px}.actions button{padding:9px 4px;font-size:12px}
.missionText{font-size:13px;color:#d8e4ed;line-height:1.6;padding:10px;background:#1c3149;border-radius:6px}
.foot{border-top:1px solid #385773;background:#14243a;display:flex;gap:10px;align-items:center;padding:9px 16px;flex-wrap:wrap}.foot span{flex:1;font-size:12px;color:#c8d6dc}
.modal{display:none;position:absolute;inset:0;background:#06101bce;align-items:center;justify-content:center;z-index:10;padding:20px}.modal.visible{display:flex}
.modal-inner{border:1px solid #9ac3d6;background:#172c43;box-shadow:0 20px 50px #0008;border-radius:14px;padding:24px;max-width:540px;text-align:center;line-height:1.7}.modal-inner h2{margin:0 0 10px;font-size:30px;color:var(--orange)}
@media(max-width:760px){.workspace{grid-template-columns:1fr;grid-template-rows:minmax(310px,1fr) 280px}.panel{border-left:0;border-top:1px solid #426079}.choices{grid-template-columns:1fr;gap:8px}.choice{min-height:100px}.choice p{display:none}.choice h3{margin:8px 0}.screen{min-height:580px}.topbar{padding:8px}.foot{padding:6px}.clock{font-size:22px}}
</style></head>
<body>
<section id="intro" class="screen active"><div class="stars"></div><div class="orb"></div><div class="scan"></div><div class="intro-content"><div class="eyebrow">ROBOTICS / SPACE OPERATIONS / 6 AXIS</div><h1>MECHA LAB</h1><div class="subtitle">VIRTUAL ROBOT ARM CONTROL SYSTEM</div><div class="intro-btns"><button class="primary" id="startBtn">▶ START GAME</button><button id="helpBtn">ⓘ HOW TO PLAY</button></div><p class="tips">6-MOTOR SIMULATION · BIOLOID PREMIUM EXPERIMENT</p></div></section>
<section id="select" class="screen"><div class="stars"></div><div style="z-index:2;text-align:center"><div class="eyebrow">MISSION SELECT</div><h2>SELECT OPERATION</h2><div class="choices"><div class="choice" data-mission="rock"><div class="num">01 / 01:30</div><h3>화성 암석 채취</h3><p>6개 관절을 조작해 암석 샘플 지점으로 말단을 이동시켜 보세요.</p></div><div class="choice" data-mission="battery"><div class="num">02 / 02:00</div><h3>배터리 분리</h3><p>목표 자세로 이동해 궤도 장치의 배터리를 분리하세요.</p></div><div class="choice" data-mission="satellite"><div class="num">03 / 04:00</div><h3>인공위성 수리</h3><p>여러 단계의 목표 자세를 달성해 정비 작업을 완료하세요.</p></div></div><button id="backIntro">← BACK</button></div></section>
<section id="game" class="screen"><div class="topbar"><div><div class="brand">MECHA LAB / 3D MISSION CONTROL</div><h2 id="missionTitle">화성 암석 채취</h2></div><div><div class="brand">TIME REMAINING</div><div class="clock" id="clock">01:30</div></div></div>
<div class="workspace"><div class="viewport"><canvas id="scene"></canvas><div class="hud"><strong>6 AXIS / DIGITAL SIMULATION</strong><br>드래그: 시점 회전 · 휠: 확대/축소<br>J1~J6 슬라이더: 관절 회전<br>실제 모터로 명령을 전송하지 않습니다.</div></div><div class="panel"><h3>JOINT CONTROL / MOTOR 01—06</h3><div id="jointControls"></div><div class="missionText" id="objective"></div><div class="actions"><button id="gripBtn">집게 열기/닫기</button><button id="checkBtn" class="primary">목표 자세 판정</button><button id="resetBtn">↻ 다시 시작 (R)</button><button id="jsonBtn">각도 JSON 복사</button></div><p class="tips">※ 실제 로봇팔의 정확한 링크 길이·회전축·영점이 확인되기 전의 3D 근사 모델입니다. 슬라이더 각도는 실제 모터 위치값이 아닙니다.</p></div></div><div class="foot"><button id="missionBack">← MISSION SELECT (Esc)</button><span id="status">관절 슬라이더로 로봇팔을 움직이세요.</span></div>
<div class="modal" id="resultModal"><div class="modal-inner"><div class="eyebrow">MISSION REPORT</div><h2 id="resultTitle">SUCCESS</h2><p id="resultText"></p><button id="retryBtn" class="primary">다시 도전</button><button id="selectBtn">미션 선택</button></div></div></section>
<div class="modal" id="helpModal"><div class="modal-inner"><h2>HOW TO PLAY</h2><p>미션을 선택한 뒤 J1~J6의 슬라이더로 3D 로봇팔을 움직여 주세요. 화면을 드래그하면 로봇팔을 다른 방향에서 관찰할 수 있습니다. 미션별 목표 관절각에 접근해 판정 버튼을 누르면 됩니다.</p><p class="tips">R = 재시작 / Esc = 미션 선택 / Space = 집게 개폐<br>실물 로봇팔과의 USB 제어는 아직 연결하지 않은 시뮬레이션 버전입니다.</p><button id="closeHelp">확인</button></div></div>
<script>
'use strict';
const el = id => document.getElementById(id);
const canvas = el('scene');
const ctx = canvas.getContext('2d');
const missionConfig = {
  rock:{title:'화성 암석 채취',time:90,goals:[[10,-35,55,5,0,0]],text:'암석 수집 자세에 접근하세요. 목표 관절각과의 오차가 각 관절 ±12° 이내면 성공합니다.'},
  battery:{title:'배터리 분리',time:120,goals:[[0,-15,40,20,0,0]],text:'배터리 분리 자세에 접근하세요. 모든 관절을 목표각 ±12° 이내로 맞춰주세요.'},
  satellite:{title:'인공위성 수리',time:240,goals:[[15,-25,50,10,25,0],[-15,-10,30,0,-20,35],[0,-35,55,5,0,-20]],text:'위성 정비 3단계입니다. 목표 자세를 차례로 달성하세요.'}
};
const neutral=[0,-20,35,0,0,0];
const mins=[-145,-95,-120,-110,-145,-145];
const maxs=[145,95,120,110,145,145];
let angles=[...neutral], grip=false, currentMission=null, stage=0, duration=90, startTime=0, finished=false, frameId=0;
let cameraAz=.75,cameraEl=.36,cameraZoom=.72,mouseDown=false,lastX=0,lastY=0;
const RAD=Math.PI/180;
const controls=[];
for(let i=0;i<6;i++){
 const div=document.createElement('div');div.className='joint';
 const label=document.createElement('label');const name=document.createElement('span');name.textContent='J'+(i+1)+' / ID '+String(i+1).padStart(3,'0');
 const out=document.createElement('output');out.textContent=angles[i]+'°';label.append(name,out);
 const input=document.createElement('input');input.type='range';input.min=mins[i];input.max=maxs[i];input.step='1';input.value=angles[i];input.setAttribute('aria-label','관절 '+(i+1)+' 각도');
 input.addEventListener('input',()=>{angles[i]=Number(input.value);out.textContent=angles[i]+'°';});
 div.append(label,input);el('jointControls').append(div);controls.push({input,out});
}
function sync(){controls.forEach((c,i)=>{c.input.value=angles[i];c.out.textContent=angles[i]+'°';});}
function show(id){document.querySelectorAll('.screen').forEach(e=>e.classList.remove('active'));el(id).classList.add('active');}
function closeResult(){el('resultModal').classList.remove('visible');}
function startMission(id){currentMission=id;stage=0;duration=missionConfig[id].time;show('game');resetGame();}
function resetGame(){if(!currentMission)return;angles=[...neutral];sync();grip=false;finished=false;stage=0;startTime=performance.now();closeResult();el('missionTitle').textContent=missionConfig[currentMission].title;el('gripBtn').textContent='집게 닫기 (Space)';updateObjective();el('status').textContent='목표 자세로 관절을 조절하세요.';}
function updateObjective(){let cfg=missionConfig[currentMission];let g=cfg.goals[stage];el('objective').textContent=(cfg.goals.length>1?('STEP '+(stage+1)+'/'+cfg.goals.length+' · '):'')+cfg.text+'\n 목표각: '+g.map((v,i)=>'J'+(i+1)+':'+v+'°').join('  ');}
function endMission(ok){if(finished)return;finished=true;el('resultTitle').textContent=ok?'SUCCESS':'FAILED';el('resultTitle').style.color=ok?'#a9f5bd':'#ff8d85';el('resultText').textContent=ok?'모든 목표 자세를 완료했습니다.':'제한시간이 종료되었습니다.';el('resultModal').classList.add('visible');}
function checkGoal(){if(finished||!currentMission)return;let g=missionConfig[currentMission].goals[stage];let errors=g.map((v,i)=>Math.abs(v-angles[i]));if(errors.every(e=>e<=12)){stage++;if(stage>=missionConfig[currentMission].goals.length){endMission(true);}else{updateObjective();el('status').textContent='단계 완료! 다음 목표 자세로 이동하세요.';}}else{el('status').textContent='목표각 오차 확인: 최대 '+Math.max(...errors).toFixed(0)+'° / 허용 12°';}}
function toggleGrip(){grip=!grip;el('gripBtn').textContent=grip?'집게 열기 (Space)':'집게 닫기 (Space)';}
el('startBtn').onclick=()=>show('select');el('helpBtn').onclick=()=>el('helpModal').classList.add('visible');el('closeHelp').onclick=()=>el('helpModal').classList.remove('visible');
el('backIntro').onclick=()=>show('intro');document.querySelectorAll('[data-mission]').forEach(e=>e.onclick=()=>startMission(e.dataset.mission));
el('resetBtn').onclick=resetGame;el('retryBtn').onclick=resetGame;el('checkBtn').onclick=checkGoal;el('gripBtn').onclick=toggleGrip;
el('missionBack').onclick=()=>{closeResult();show('select');currentMission=null;};el('selectBtn').onclick=el('missionBack').onclick;
el('jsonBtn').onclick=async()=>{let json=JSON.stringify({source:'MECHA LAB SIMULATION ONLY',motor_ids:[1,2,3,4,5,6],joint_degrees:angles},null,2);try{await navigator.clipboard.writeText(json);el('status').textContent='각도 JSON을 복사했습니다.';}catch(e){el('status').textContent='복사 권한이 제한됩니다. '+json.replace(/\s+/g,' ');}};
document.addEventListener('keydown',e=>{if(e.key==='Escape'){if(el('helpModal').classList.contains('visible')){el('helpModal').classList.remove('visible');return;}if(el('game').classList.contains('active'))el('missionBack').click();}if(!el('game').classList.contains('active')||e.target.tagName==='INPUT')return;if(e.key==='r'||e.key==='R')resetGame();if(e.code==='Space'){e.preventDefault();toggleGrip();}});
canvas.addEventListener('pointerdown',e=>{mouseDown=true;lastX=e.clientX;lastY=e.clientY;canvas.classList.add('dragging');canvas.setPointerCapture(e.pointerId);});
canvas.addEventListener('pointermove',e=>{if(!mouseDown)return;cameraAz+=(e.clientX-lastX)*.007;cameraEl=Math.max(-.1,Math.min(1.25,cameraEl+(e.clientY-lastY)*.007));lastX=e.clientX;lastY=e.clientY;});
function stopDrag(){mouseDown=false;canvas.classList.remove('dragging');}canvas.addEventListener('pointerup',stopDrag);canvas.addEventListener('pointercancel',stopDrag);
canvas.addEventListener('wheel',e=>{e.preventDefault();cameraZoom=Math.max(.5,Math.min(2.1,cameraZoom*(e.deltaY>0?.91:1.09)));},{passive:false});
// Minimal self-contained 3D renderer: no CDN and no external files.
const V=(x,y,z)=>[x,y,z],add=(a,b)=>a.map((v,i)=>v+b[i]),scale=(a,s)=>a.map(v=>v*s),mul=(A,B)=>A.map(row=>B[0].map((_,j)=>row.reduce((sum,v,k)=>sum+v*B[k][j],0)));
const I=[[1,0,0],[0,1,0],[0,0,1]];
const mv=(M,v)=>M.map(row=>row.reduce((s,a,i)=>s+a*v[i],0));
function rot(axis,t){let c=Math.cos(t),s=Math.sin(t);if(axis==='x')return [[1,0,0],[0,c,-s],[0,s,c]];if(axis==='y')return [[c,0,s],[0,1,0],[-s,0,c]];return [[c,-s,0],[s,c,0],[0,0,1]];}
function getKinematics(){let p=[0,.25,0],R=I,objs=[],joints=[];const axes=['y','z','z','z','x','y'],lengths=[.23,1.35,1.12,.57,.28,.22];
 for(let i=0;i<6;i++){R=mul(R,rot(axes[i],angles[i]*RAD));joints.push([...p]);let next=add(p,mv(R,[0,lengths[i],0]));objs.push({a:p,b:next,width:i===0?.28:.17,color:i%2?'#95aebb':'#ccdde2'});p=next;}
 return {objs,joints,tip:p,R};}
function project(p,w,h){let ca=Math.cos(cameraAz),sa=Math.sin(cameraAz),ce=Math.cos(cameraEl),se=Math.sin(cameraEl);
 let x=p[0]*ca-p[2]*sa, z=p[0]*sa+p[2]*ca, y=p[1]*ce-z*se, depth=p[1]*se+z*ce;
 let sc=Math.min(w/6.8,h/4.8)*cameraZoom;return [w*.48+x*sc,h*.72-y*sc,depth];}
function poly(points,fill,stroke='#263c52'){ctx.beginPath();points.forEach((p,i)=>i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1]));ctx.closePath();ctx.fillStyle=fill;ctx.fill();ctx.strokeStyle=stroke;ctx.lineWidth=1.4;ctx.stroke();}
function cube(p,R,s,color,w,h,depth,faces){let [sx,sy,sz]=s,verts=[];for(let x of [-1,1])for(let y of [-1,1])for(let z of [-1,1])verts.push(project(add(p,mv(R,[x*sx/2,y*sy/2,z*sz/2])),w,h));let ids=[[0,1,3,2],[4,6,7,5],[0,4,5,1],[2,3,7,6],[0,2,6,4],[1,5,7,3]];for(let ix of ids){faces.push({z:ix.reduce((v,i)=>v+verts[i][2],0)/4,pts:ix.map(i=>verts[i]),color});}}
function draw3D(){if(!el('game').classList.contains('active'))return;let rect=canvas.getBoundingClientRect(),dpr=Math.min(2,window.devicePixelRatio||1),w=rect.width,h=rect.height;if(!w||!h)return;if(canvas.width!==Math.floor(w*dpr)||canvas.height!==Math.floor(h*dpr)){canvas.width=Math.floor(w*dpr);canvas.height=Math.floor(h*dpr);}ctx.setTransform(dpr,0,0,dpr,0,0);
 const grad=ctx.createLinearGradient(0,0,0,h);grad.addColorStop(0,'#122d48');grad.addColorStop(1,'#070e21');ctx.fillStyle=grad;ctx.fillRect(0,0,w,h);
 ctx.strokeStyle='#294660';ctx.lineWidth=1;for(let x=-4;x<=4;x++){let a=project([x,0,-4],w,h),b=project([x,0,4],w,h);ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(b[0],b[1]);ctx.stroke();}for(let z=-4;z<=4;z++){let a=project([-4,0,z],w,h),b=project([4,0,z],w,h);ctx.beginPath();ctx.moveTo(a[0],a[1]);ctx.lineTo(b[0],b[1]);ctx.stroke();}
 const kin=getKinematics(),faces=[];cube([0,.09,0],I,[.68,.18,.68],'#405c72',w,h,0,faces);let p=[0,.25,0],R=I;let axes=['y','z','z','z','x','y'],ls=[.23,1.35,1.12,.57,.28,.22];
 for(let i=0;i<6;i++){R=mul(R,rot(axes[i],angles[i]*RAD));cube(p,R,[.3,.3,.3],i%2?'#d78266':'#e6a47a',w,h,0,faces);let center=add(p,mv(R,[0,ls[i]/2,0]));cube(center,R,[i===0?.28:.19,ls[i],.23],i%2?'#6489a0':'#9fb7c1',w,h,0,faces);p=add(p,mv(R,[0,ls[i],0]));}
 cube(p,R,[.34,.12,.34],'#f3c47b',w,h,0,faces);for(let s of [-1,1]){let offset=mv(R,[s*(grip?.11:.21),.13,0]);cube(add(p,offset),R,[.09,.32,.12],'#ffe0a4',w,h,0,faces);}
 faces.sort((a,b)=>b.z-a.z);faces.forEach(f=>poly(f.pts,f.color));
 for(let i=0;i<kin.joints.length;i++){let q=project(kin.joints[i],w,h);ctx.beginPath();ctx.arc(q[0],q[1],6,0,Math.PI*2);ctx.fillStyle='#f39c6a';ctx.fill();ctx.font='bold 12px Consolas';ctx.fillStyle='#ffffff';ctx.fillText('J'+(i+1),q[0]+9,q[1]-7);}
 let t=project(p,w,h);ctx.fillStyle='#9af5cd';ctx.beginPath();ctx.arc(t[0],t[1],4,0,Math.PI*2);ctx.fill();}
function loop(now){if(el('game').classList.contains('active')){if(!finished){let remaining=Math.max(0,Math.ceil(duration-(now-startTime)/1000));el('clock').textContent=String(Math.floor(remaining/60)).padStart(2,'0')+':'+String(remaining%60).padStart(2,'0');el('clock').classList.toggle('red',remaining<=30);if(remaining===0)endMission(false);}draw3D();}frameId=requestAnimationFrame(loop);}
requestAnimationFrame(loop);
</script></body></html>"""

components.html(GAME_HTML, height=920, scrolling=False)
# END OF COMPLETE MECHA LAB 2.0 SINGLE-FILE APP
