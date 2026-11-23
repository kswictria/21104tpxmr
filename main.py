# MECHA LAB 2.0 — ONE FILE (2026-11-23)
# 6-motor simulation only: no commands are sent to the real robot.
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MECHA LAB 2.0", page_icon="🦾", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapsedControl"] {display:none !important}
.block-container {max-width:100% !important; padding:0 !important}
html, body, .stApp, [data-testid="stAppViewContainer"] {background:#080e1b !important}
iframe {display:block; width:100%}
</style>""", unsafe_allow_html=True)

# Embedded HTML / CSS / JavaScript: no assets or pages folder required.
GAME_HTML = r"""<!doctype html>
<html lang="ko"><head><meta charset="utf-8"/><meta name="viewport" content="width=device-width, initial-scale=1"/>
<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Rajdhani:wght@400;500;600;700&display=swap');
:root{--ink:#e9f5ff;--dim:#8ba5bc;--edge:#35516a;--glass:#101f36e8;--blue:#5fd6ff;--orange:#f2a56d;--good:#80f1b6;--red:#ff7285}
*{box-sizing:border-box}html,body{width:100%;height:100%;margin:0;background:#080e1b;color:var(--ink);font-family:'Rajdhani','Malgun Gothic',sans-serif;overflow:hidden}
button,input{font:inherit}button{cursor:pointer}button:focus-visible,input:focus-visible{outline:2px solid var(--blue);outline-offset:3px}
#root{width:100vw;height:100vh;min-height:550px;position:relative;overflow:hidden;background:radial-gradient(ellipse at 50% 120%,#24416a 0%,#0b1428 49%,#070c19 100%)}
#stars{position:absolute;inset:0;pointer-events:none;overflow:hidden}.star{position:absolute;width:2px;height:2px;background:#b7ddff;animation:twinkle 2.4s infinite alternate}.star:nth-child(3n){width:1px;height:1px}.star:nth-child(5n){background:#ffc19d}
@keyframes twinkle{from{opacity:.17}to{opacity:.96}}.screen{position:absolute;inset:0;display:none}.screen.active{display:block}
button{background:#152a43;border:1px solid #426985;color:#e6f4ff;font-weight:700;letter-spacing:1px;padding:10px 15px;border-radius:4px;transition:.2s}
button:hover{background:#274968;border-color:#75cde6}.primary{background:var(--orange);border-color:#f7c29b;color:#112034}.primary:hover{background:#ffd09e;color:#102037}
.mono,.eyebrow,.pill,.stat,.key,.timer,.index{font-family:'Share Tech Mono',monospace;letter-spacing:1px}
#intro .gridfade{position:absolute;inset:0;background:linear-gradient(transparent 93%,#4b96bd1d 94%),linear-gradient(90deg,transparent 93%,#4b96bd1d 94%);background-size:65px 65px;transform:perspective(550px) rotateX(62deg) scale(2);transform-origin:center bottom;mask-image:linear-gradient(transparent 10%,#000 80%);opacity:.6}
.intro-layout{position:relative;z-index:1;height:100%;display:flex;flex-direction:column;justify-content:center;align-items:center;text-align:center;padding:22px}
.eyebrow{font-size:13px;letter-spacing:4px;color:#72cfea}.mark{font-size:clamp(62px,11vw,146px);font-weight:700;letter-spacing:7px;line-height:.9;margin:14px 0 9px;color:#f2f7ff;text-shadow:0 0 40px #56ccff37}.mark span{color:var(--orange)}
.subtitle{font-size:clamp(14px,2vw,22px);color:#9fbcce;letter-spacing:3px;margin:5px 0 25px}.planet{position:absolute;border-radius:50%;width:38vw;max-width:480px;aspect-ratio:1;background:radial-gradient(circle at 30% 28%,#496d9b,#263c64 49%,#0d1733 76%);right:-12vw;top:-13vw;box-shadow:0 0 90px #316dad30;opacity:.55}
.intro-panel{border:1px solid #34536c;background:#091728cb;padding:17px 21px;max-width:520px;margin:0 auto 24px;font-size:16px;line-height:1.55;color:#c4dae5}.intro-panel strong{color:#ffe3b1}
.intro-btns{display:flex;gap:12px;justify-content:center}.scanline{pointer-events:none;position:absolute;inset:0;background:repeating-linear-gradient(0deg,transparent 0,transparent 4px,#0000000c 5px);z-index:9}
.top{height:72px;display:flex;justify-content:space-between;align-items:center;padding:0 30px;background:#091627d9;border-bottom:1px solid #2c4861;position:relative;z-index:2}
.brand{font-weight:700;letter-spacing:2px;font-size:23px}.brand b{color:var(--orange)}.top-right{font-family:'Share Tech Mono',monospace;font-size:12px;color:var(--dim);letter-spacing:1px}
#select .missions{height:calc(100% - 72px);display:flex;flex-direction:column;justify-content:center;align-items:center;padding:20px 25px 60px}
.section-heading{text-align:center;margin-bottom:27px}.section-heading h1{font-size:clamp(31px,4.7vw,51px);letter-spacing:3px;margin:0 0 5px}.section-heading p{color:#97afc4;margin:0;font-size:16px}
.cards{display:grid;grid-template-columns:repeat(3,minmax(180px,290px));gap:16px;width:min(100%,950px)}.mission{min-height:250px;background:linear-gradient(150deg,#182c47f0,#0e192fe9);border:1px solid #3c5d79;padding:22px;display:flex;flex-direction:column;justify-content:space-between;cursor:pointer;transition:.2s}.mission:hover{transform:translateY(-6px);border-color:var(--orange);box-shadow:0 9px 37px #0007}
.mission .num{font-family:'Share Tech Mono',monospace;color:#87b0c7;font-size:12px}.mission .symbol{font-size:54px;line-height:1.4}.mission h2{margin:4px 0;font-size:24px}.mission p{font-size:14px;color:#bad0dd;line-height:1.4;margin:2px 0}.mission .bottom{display:flex;justify-content:space-between;border-top:1px solid #3c5466;padding-top:11px;margin-top:12px;color:var(--orange);font-family:'Share Tech Mono',monospace;font-size:12px}
#sim{background:#0b1323}.simhead{height:64px;padding:0 20px;display:flex;align-items:center;gap:12px;background:#111f33;border-bottom:1px solid #30475b;position:relative;z-index:3}.simhead h2{font-size:20px;margin:0;white-space:nowrap}.simhead .tiny{font-size:11px;color:#91b3c5;letter-spacing:2px}.simhead .grow{flex:1}.timer{font-size:30px;color:#ffd59c}.timer.warn{color:#ff7185}
.workarea{display:grid;grid-template-columns:minmax(0,1fr) 300px;height:calc(100% - 64px)}
.stage{position:relative;min-width:0;overflow:hidden;background:radial-gradient(ellipse at 53% 60%,#1d3952 0%,#0c1b31 54%,#0b1426 100%)}
#viewport{width:100%;height:100%;display:block;touch-action:none;cursor:grab}#viewport:active{cursor:grabbing}
.stage-tag{position:absolute;top:15px;left:18px;pointer-events:none;font:12px 'Share Tech Mono',monospace;color:#8fdcff;letter-spacing:2px}
.stage-tag span{display:block;color:#819bb0;letter-spacing:0;margin-top:5px}.statusbar{position:absolute;bottom:12px;left:15px;right:15px;display:flex;align-items:flex-end;justify-content:space-between;pointer-events:none;gap:14px}
.status{background:#0b1c30e3;border:1px solid #38536a;padding:10px 13px;max-width:min(560px,80%);font-size:14px;line-height:1.35}.status b{color:var(--good)}
.indicator{font:11px 'Share Tech Mono',monospace;letter-spacing:1px;background:#0b1c30d1;border:1px solid #38536a;padding:9px}
.sidebar{background:#101d31;overflow-y:auto;border-left:1px solid #36516c;padding:15px 17px 21px}.pane-title{font:12px 'Share Tech Mono',monospace;color:#7bccea;letter-spacing:2px;margin:0 0 12px}.sidebar .help{font-size:13px;line-height:1.4;color:#b0c5d4;margin:6px 0 17px}.joint{margin:11px 0 17px}.jointline{display:flex;justify-content:space-between;align-items:center;margin-bottom:5px}.jointname{font:12px 'Share Tech Mono',monospace;color:#d9e9f0}.jointname em{font:11px 'Rajdhani',sans-serif;color:#8ba8b7;font-style:normal}.degree{color:#ffd49d;font:14px 'Share Tech Mono',monospace}
input[type=range]{width:100%;accent-color:#f0a77b;cursor:pointer}.smallbtns{display:grid;grid-template-columns:1fr 1fr;gap:7px;margin:16px 0}.smallbtns button{font-size:12px;padding:9px 5px}.readout{border:1px solid #31506b;background:#0b1628;padding:10px 12px;margin-top:14px}.readout .value{font:12px 'Share Tech Mono',monospace;color:#b8e2ed;line-height:1.7;white-space:pre-wrap;word-break:break-word}.badge{display:inline-block;padding:2px 6px;font:10px 'Share Tech Mono',monospace;color:#8ff3b8;border:1px solid #46765d}
#overlay{position:absolute;inset:0;background:#060c18d5;display:none;align-items:center;justify-content:center;z-index:6;padding:22px}#overlay.show{display:flex}.dialog{text-align:center;background:linear-gradient(145deg,#1e3551,#101c30);border:1px solid #6b95a5;max-width:450px;width:100%;padding:33px}.dialog h1{font-size:58px;letter-spacing:4px;margin:9px 0;color:#a4f5bf}.dialog.fail h1{color:#ff8892}.dialog p{color:#b8d0df;font-size:17px}
#notice{position:absolute;top:15px;right:15px;font:12px 'Share Tech Mono',monospace;color:#ffd6a7;background:#13283ad9;border:1px solid #436273;padding:8px;max-width:250px;text-align:right}
@media(max-width:800px){.top{padding:0 15px}.cards{grid-template-columns:1fr;max-height:70vh;overflow-y:auto}.mission{min-height:140px}.mission .symbol{font-size:30px}.section-heading{margin-bottom:13px}.workarea{grid-template-columns:minmax(0,1fr) 235px}.sidebar{padding:11px}.simhead{gap:7px;padding:0 8px}.simhead h2{font-size:15px}.timer{font-size:23px}.stage-tag{font-size:9px}}
@media(max-width:570px){.workarea{display:flex;flex-direction:column}.stage{height:57%;flex-shrink:0}.sidebar{height:43%;border-left:0;border-top:1px solid #34516a}.sidebar .jointset{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:0 13px}.joint{margin:4px 0 9px}.simhead .tiny{display:none}.simhead h2{font-size:13px}}
</style></head><body><div id="root"><div id="stars"></div><div class="scanline"></div>
<section id="intro" class="screen active"><div class="planet"></div><div class="gridfade"></div><div class="intro-layout">
<div class="eyebrow">ORBITAL ROBOTICS / INTERACTIVE LAB</div><div class="mark">MECHA <span>LAB</span></div>
<div class="subtitle">6-AXIS ROBOTIC ARM SIMULATOR</div>
<div class="intro-panel"><span class="mono" style="color:#76cce8">MISSION LOG 02 / SIGNAL RECEIVED</span><br/><strong>원격 조작을 위한 차세대 로봇팔 시스템이 준비되었습니다.</strong><br/>가상 관절 6개를 직접 제어하여 화성 시료 채취, 궤도 배터리 분리, 위성 정비 임무를 수행하세요.</div>
<div class="intro-btns"><button class="primary" id="startBtn">▶ START GAME</button><button id="helpBtn">ⓘ HOW TO PLAY</button></div><p class="eyebrow" style="font-size:11px;letter-spacing:2px;margin-top:24px;color:#829caf">SIMULATION MODE · NO HARDWARE OUTPUT · BUILD 2.0.1</p></div></section>
<section id="select" class="screen"><div class="top"><div class="brand">MECHA <b>LAB</b></div><div class="top-right">MISSION SELECT / 03 AVAILABLE</div></div><div class="missions"><div class="section-heading"><div class="eyebrow">CHOOSE OPERATION</div><h1>SELECT MISSION</h1><p>6축 로봇팔을 조작하여 각 임무를 수행하세요.</p></div><div class="cards">
<div class="mission" data-mission="rock"><div><div class="num">MISSION / 01</div><div class="symbol">🪨</div><h2>화성 암석 채취</h2><p>집게를 시료에 접근시켜 잡은 뒤 수집함으로 옮기세요.</p></div><div class="bottom"><span>01:30</span><span>LAUNCH ↗</span></div></div>
<div class="mission" data-mission="battery"><div><div class="num">MISSION / 02</div><div class="symbol">🔋</div><h2>배터리 분리</h2><p>잠금장치를 해제한 뒤 배터리를 지정 지점으로 이동시키세요.</p></div><div class="bottom"><span>02:00</span><span>LAUNCH ↗</span></div></div>
<div class="mission" data-mission="satellite"><div><div class="num">MISSION / 03</div><div class="symbol">🛰️</div><h2>인공위성 수리</h2><p>덮개·버튼·스위치·전선·안테나 순서로 정비하세요.</p></div><div class="bottom"><span>04:00</span><span>LAUNCH ↗</span></div></div>
</div></div></section>
<section id="sim" class="screen"><div class="simhead"><button id="backBtn" style="padding:7px 10px">← MISSIONS</button><button id="fullBtn" title="전체화면" style="padding:7px 10px">⛶</button><div><div class="tiny">ROBOTIC ARM / CONTROL DECK</div><h2 id="missionTitle">화성 암석 채취</h2></div><div class="grow"></div><div class="tiny" id="stepName">TASK</div><div class="timer" id="clock">01:30</div></div>
<div class="workarea"><div class="stage"><canvas id="viewport"></canvas><div class="stage-tag">MECHA LAB / LIVE 3D<span>드래그: 시점 회전 · 휠: 확대/축소</span></div><div id="notice">VIRTUAL MODE · 6 AXES · v2.0.2</div><div class="statusbar"><div class="status" id="status"><b>READY</b> 관절을 조작해 목표에 접근하세요.</div><div class="indicator" id="indicator">TARGET: OUT OF RANGE</div></div></div>
<aside class="sidebar"><div class="pane-title">JOINT CONTROL / MOTOR ID 01–06</div><div class="help">아래 슬라이더로 6개 축을 조작하세요. 실제 AX-12A 모터에는 아직 명령을 보내지 않습니다.</div><div class="jointset" id="jointControls"></div>
<div class="smallbtns"><button class="primary" id="gripBtn">집게 닫기 (SPACE)</button><button id="resetBtn">초기화</button><button id="homeBtn">기본 자세</button><button id="exportBtn">각도 복사</button></div>
<div class="readout"><div class="pane-title" style="margin-bottom:4px">TELEMETRY / VIRTUAL</div><div class="value" id="readout">J1: 0.0°</div></div><div class="help" style="margin-top:11px">※ 현재 3D 관절축은 실제 기구의 정밀 실측 전 임시 모델입니다. 실물 구동·토크 출력은 비활성화되어 있습니다.</div></aside></div>
<div id="overlay"><div class="dialog" id="dialog"><div class="eyebrow">MISSION REPORT</div><h1 id="outcome">SUCCESS</h1><p id="outcomeText">임무 완료</p><div style="display:flex;justify-content:center;gap:10px"><button class="primary" id="retryBtn">↻ RETRY</button><button id="selectBtn">MISSIONS</button></div></div></div></section>
</div><script src="https://cdn.jsdelivr.net/npm/three@0.149.0/build/three.min.js"></script><script>
(()=>{'use strict';
const byId=id=>document.getElementById(id);
const specs={rock:{title:'화성 암석 채취',seconds:90},battery:{title:'배터리 분리',seconds:120},satellite:{title:'인공위성 수리',seconds:240}};
const JOINTS=[{name:'BASE YAW',axis:'Y'},{name:'SHOULDER',axis:'Z'},{name:'ELBOW',axis:'Z'},{name:'WRIST PITCH',axis:'Z'},{name:'WRIST ROLL',axis:'X'},{name:'TOOL YAW',axis:'Y'}];
let mode='intro',mission='rock',angles=[0,-30,55,-25,0,0],held=false,done=false,remaining=90,lastTime=0,step=0,connected=0,simTime=0,gripOpen=true,carried=null,stars=[];
let renderer,scene,camera,rig,axes=[],tipMarker,gripper,objects={},orbit={theta:0.65,phi:1.13,radius:12},pointer=null,webglOk=false;
const clamp=(x,a,b)=>Math.min(b,Math.max(a,x));
function show(which){mode=which;document.querySelectorAll('.screen').forEach(s=>s.classList.toggle('active',s.id===which));if(which==='sim')setTimeout(resize,20)}
function msg(s,positive=false){byId('status').innerHTML=`<b style="color:${positive?'#8cf4b8':'#a6dbff'}">${positive?'OK':'MISSION'}</b> ${s}`}
for(let i=0;i<90;i++){const n=document.createElement('i');n.className='star';n.style.left=((i*61.83)%100)+'%';n.style.top=((i*37.73)%100)+'%';n.style.animationDelay=(i%11)*.31+'s';byId('stars').appendChild(n)}
byId('startBtn').onclick=()=>show('select');
byId('helpBtn').onclick=()=>{byId('intro').querySelector('.intro-panel').innerHTML='<span class="mono" style="color:#76cce8">HOW TO PLAY / OPERATOR GUIDE</span><br/>미션을 고른 뒤 J1~J6 슬라이더로 로봇팔의 자세를 조정하세요. 집게가 빛나는 목표에 가까워지면 SPACE 또는 집게 버튼으로 작업합니다. R키는 미션 재시작, Esc키는 미션 선택 화면으로 돌아가기입니다.<br/><strong>화면은 3D 시뮬레이션이며 실제 로봇팔은 움직이지 않습니다.</strong>'};
document.querySelectorAll('[data-mission]').forEach(x=>x.onclick=()=>launch(x.dataset.mission));
byId('backBtn').onclick=()=>{show('select')};byId('fullBtn').onclick=()=>{if(!document.fullscreenElement)byId('root').requestFullscreen?.();else document.exitFullscreen?.()};byId('resetBtn').onclick=()=>launch(mission);byId('retryBtn').onclick=()=>launch(mission);byId('selectBtn').onclick=()=>show('select');
byId('homeBtn').onclick=()=>{angles=[0,-30,55,-25,0,0];syncSliders();msg('기본 자세로 복원했습니다.')};
byId('exportBtn').onclick=()=>{const data=JSON.stringify({mission,angles_deg:angles,motor_ids:[1,2,3,4,5,6]},null,2);if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(data).then(()=>msg('6개 관절의 목표각 JSON을 복사했습니다.',true)).catch(()=>prompt('아래 값을 복사하세요',data))}else prompt('아래 값을 복사하세요',data)};
byId('gripBtn').onclick=act;
document.addEventListener('keydown',e=>{
  if(mode!=='sim'||e.repeat||['INPUT','BUTTON'].includes(e.target.tagName))return;
  if(e.code==='Space'){e.preventDefault();act();}
  if(e.code==='KeyR'){e.preventDefault();launch(mission);}
  if(e.code==='Escape'){e.preventDefault();show('select');}
});
function buildSliders(){const wrap=byId('jointControls');wrap.innerHTML='';JOINTS.forEach((j,i)=>{let box=document.createElement('div');box.className='joint';box.innerHTML=`<div class="jointline"><span class="jointname">J${i+1} <em>${j.name}</em></span><span class="degree" id="deg${i}">${angles[i].toFixed(0)}°</span></div><input aria-label="J${i+1} rotation" id="slider${i}" type="range" min="-145" max="145" step="1" value="${angles[i]}">`;wrap.appendChild(box);box.querySelector('input').oninput=e=>{angles[i]=Number(e.target.value);byId('deg'+i).textContent=angles[i].toFixed(0)+'°'}})}
function syncSliders(){angles.forEach((v,i)=>{byId('slider'+i).value=v;byId('deg'+i).textContent=v.toFixed(0)+'°'})}
function mesh(g,m,p=[0,0,0]){let a=new THREE.Mesh(g,m);a.position.set(...p);a.castShadow=true;a.receiveShadow=true;return a}
const mat=(color,metalness=.25,roughness=.5,emissive=0)=>new THREE.MeshStandardMaterial({color,metalness,roughness,emissive});
function cyl(r1,r2,h,m){return mesh(new THREE.CylinderGeometry(r1,r2,h,20),m)}
function box(w,h,d,m,p=[0,0,0]){return mesh(new THREE.BoxGeometry(w,h,d),m,p)}
function addArm(){rig=new THREE.Group();scene.add(rig);let blue=mat(0x8ca7b5,.65,.36),lite=mat(0xd9e5e4,.55,.34),joint=mat(0x243847,.45,.45),red=mat(0xe47c69,.5,.44);
const baseplate=cyl(.78,.9,.4,joint);baseplate.position.y=.2;rig.add(baseplate);const yaw=new THREE.Group();yaw.position.y=.45;rig.add(yaw);axes.push({node:yaw,axis:'y'});yaw.add(cyl(.52,.53,.45,blue));
const shoulder=new THREE.Group();shoulder.position.y=.55;yaw.add(shoulder);axes.push({node:shoulder,axis:'z'});shoulder.add(mesh(new THREE.SphereGeometry(.36,22,15),red));shoulder.add(box(.53,2.15,.51,lite,[0,1.08,0]));
const elbow=new THREE.Group();elbow.position.y=2.15;shoulder.add(elbow);axes.push({node:elbow,axis:'z'});elbow.add(mesh(new THREE.SphereGeometry(.33,20,12),red));elbow.add(box(.47,1.68,.46,blue,[0,.85,0]));
const wrist=new THREE.Group();wrist.position.y=1.7;elbow.add(wrist);axes.push({node:wrist,axis:'z'});wrist.add(mesh(new THREE.SphereGeometry(.27,20,12),red));wrist.add(box(.38,.78,.38,lite,[0,.38,0]));
const roll=new THREE.Group();roll.position.y=.78;wrist.add(roll);axes.push({node:roll,axis:'x'});roll.add(cyl(.29,.29,.4,joint));
const tool=new THREE.Group();tool.position.y=.36;roll.add(tool);axes.push({node:tool,axis:'y'});tool.add(box(.54,.26,.47,lite));
gripper=new THREE.Group();tool.add(gripper);const finger1=box(.15,.65,.2,red,[-.28,.42,0]),finger2=box(.15,.65,.2,red,[.28,.42,0]);gripper.add(finger1,finger2);tipMarker=new THREE.Object3D();tipMarker.position.y=.75;tool.add(tipMarker);
return {finger1,finger2}}
let fingers;
function makeTarget(label,shape,position,color){let group=new THREE.Group();group.position.set(...position);let material=mat(color,.2,.42);let obj=shape==='sphere'?mesh(new THREE.DodecahedronGeometry(.28,1),material):shape==='battery'?box(.55,.28,.32,material):box(.42,.33,.43,material);group.add(obj);const ring=new THREE.Mesh(new THREE.TorusGeometry(.42,.025,7,40),new THREE.MeshBasicMaterial({color:0x79f6ba}));ring.rotation.x=Math.PI/2;ring.position.y=-.24;group.add(ring);scene.add(group);objects[label]={group,ring};return group}
function makeMissionProps(){Object.values(objects).forEach(o=>scene.remove(o.group));objects={};
if(mission==='rock'){makeTarget('rock','sphere',[1.3,.37,-1.55],0xb9806b);makeTarget('receiver','box',[-1.2,.25,-1.85],0x5a8e88);objects.receiver.group.scale.set(1.8,1,1.4)}
if(mission==='battery'){makeTarget('lock','box',[1.15,1.65,-1.3],0xdf7772);makeTarget('battery','battery',[1.25,1.1,-1.3],0xf8c373);makeTarget('slot','box',[-1.3,.6,-1.9],0x5a8e88)}
if(mission==='satellite'){makeTarget('coverBin','box',[-1.6,.28,-1.3],0x5a8e88);makeTarget('cover','box',[1.1,1.65,-1.9],0xf0bc80);makeTarget('buttonA','sphere',[1.9,1.42,-1.75],0xe88f79);makeTarget('buttonB','sphere',[1.85,1.05,-1.75],0x87adf2);makeTarget('switch','box',[.75,1.1,-2.0],0xd2c177);[0x61b9fc,0x63d58f,0xf3c75b,0xe96562].forEach((c,i)=>{makeTarget('wire'+i,'box',[-.3+i*.32,.7,-1.92],c);makeTarget('socket'+i,'box',[-1.35+i*.38,.43,-2.2],c);objects['socket'+i].group.scale.set(.6,.6,.6)});makeTarget('antenna','sphere',[-.85,1.7,-1.5],0x95e8c3);makeTarget('signal','sphere',[-1.6,1.4,-1.4],0x78e8cc);
const panel=box(2.4,2.4,.13,mat(0x4f687d,.5,.45),[.9,1.35,-2.25]);scene.add(panel);objects.panel={group:panel};}}
function setup3D(){const canvas=byId('viewport');if(!window.THREE){byId('notice').textContent='3D 라이브러리 로딩 실패 · 인터넷 연결 확인';return}
try{renderer=new THREE.WebGLRenderer({canvas,antialias:true,alpha:true});renderer.setPixelRatio(Math.min(devicePixelRatio||1,2));renderer.shadowMap.enabled=true;renderer.outputColorSpace=THREE.SRGBColorSpace;scene=new THREE.Scene();scene.fog=new THREE.FogExp2(0x0b1426,.035);camera=new THREE.PerspectiveCamera(43,1,.1,100);scene.add(new THREE.HemisphereLight(0xb4e1ff,0x243448,2.2));const light=new THREE.DirectionalLight(0xffd9b5,3.1);light.position.set(4,10,7);scene.add(light);let floor=mesh(new THREE.CylinderGeometry(8,8,.07,50),mat(0x182c40,.17,.82),[0,-.12,0]);scene.add(floor);const grid=new THREE.GridHelper(15,15,0x3c7091,0x1b3b55);grid.position.y=-.074;scene.add(grid);fingers=addArm();webglOk=true;resize();canvas.addEventListener('pointerdown',e=>{pointer={x:e.clientX,y:e.clientY};canvas.setPointerCapture(e.pointerId)});canvas.addEventListener('pointermove',e=>{if(!pointer)return;orbit.theta-=(e.clientX-pointer.x)*.008;orbit.phi=clamp(orbit.phi+(e.clientY-pointer.y)*.007,.15,Math.PI/2-.015);pointer={x:e.clientX,y:e.clientY}});canvas.addEventListener('pointerup',()=>pointer=null);canvas.addEventListener('pointercancel',()=>pointer=null);canvas.addEventListener('wheel',e=>{e.preventDefault();orbit.radius=clamp(orbit.radius+e.deltaY*.012,6,19)},{passive:false});new ResizeObserver(resize).observe(canvas.parentElement)}catch(err){byId('notice').textContent='3D 장면 오류: '+err.message}}
function resize(){if(!renderer||mode!=='sim')return;const parent=byId('viewport').parentElement;const w=Math.max(1,parent.clientWidth),h=Math.max(1,parent.clientHeight);renderer.setSize(w,h,false);camera.aspect=w/h;camera.updateProjectionMatrix()}
function worldPos(id){let p=new THREE.Vector3();objects[id]?.group.getWorldPosition(p);return p}
function toolPos(){rig.updateMatrixWorld(true);return tipMarker.getWorldPosition(new THREE.Vector3())}
function currentTarget(){if(mission==='rock')return held?'receiver':'rock';if(mission==='battery')return step===0?'lock':held?'slot':'battery';if(step===0)return held?'coverBin':'cover';if(step===4)return held?'socket'+connected:'wire'+connected;if(step===5)return held?'signal':'antenna';return ['cover','buttonA','buttonB','switch','wire0','antenna'][Math.min(step,5)]}
function finish(win){if(done)return;done=true;byId('overlay').classList.add('show');byId('dialog').classList.toggle('fail',!win);byId('outcome').textContent=win?'SUCCESS':'FAILED';byId('outcomeText').textContent=win?'모든 작업 조건을 완료했습니다.':'제한시간이 종료되었습니다.'}
function advance(){step++;if(step>=6){finish(true);return}msg('다음 단계: '+['덮개 제거','버튼 A','버튼 B','스위치','4색 전선','안테나 정렬'][step])}
function act(){if(mode!=='sim'||done||!webglOk)return;const target=currentTarget();const d=toolPos().distanceTo(worldPos(target));const near=d<.85;const direct=mission==='satellite'&&[1,2,3].includes(step)||mission==='battery'&&step===0;
if(direct){if(!near){msg('집게를 빛나는 목표에 더 가까이 이동하세요.');return}if(mission==='battery'){step=1;msg('잠금 해제! 배터리를 집어 지정 지점으로 옮기세요.',true);return}advance();return}
if(!held){if(!near){msg('집게 끝이 목표와 멀어요. 관절각을 조정하세요.');return}held=true;carried=target;gripOpen=false;msg('잡기 성공! 집게를 목표 지점으로 이동한 뒤 다시 누르세요.',true);return}
held=false;gripOpen=true;const drop=currentTarget();if(mission==='rock'){if(toolPos().distanceTo(worldPos('receiver'))<1.1){finish(true)}else{objects.rock.group.position.y=.3;msg('보관함 범위 밖입니다. 암석을 다시 집으세요.')}}
if(mission==='battery'){if(toolPos().distanceTo(worldPos('slot'))<1.2){finish(true)}else{msg('배터리를 지정 위치로 옮기세요.')}}if(mission==='satellite'&&step===0){if(toolPos().distanceTo(worldPos('coverBin'))<1.1){advance()}else{msg('덮개를 왼쪽 보관 위치에 놓아 주세요.')}}else if(mission==='satellite'&&step===4){if(toolPos().distanceTo(worldPos('socket'+connected))<.85){connected++;if(connected===4)advance();else msg('전선 연결 성공! 다음 전선을 연결하세요.',true)}else{msg('같은 색 소켓 가까이 가져가세요.')}}else if(mission==='satellite'&&step===5){if(toolPos().distanceTo(worldPos('signal'))<.85)advance();else msg('움직이는 전파 신호에 안테나를 정렬하세요.')}carried=null}
function launch(m){mission=m;remaining=specs[m].seconds;lastTime=0;step=0;connected=0;done=false;held=false;carried=null;gripOpen=true;angles=[0,-30,55,-25,0,0];simTime=0;byId('missionTitle').textContent=specs[m].title;byId('overlay').classList.remove('show');byId('gripBtn').textContent='집게 닫기 (SPACE)';buildSliders();show('sim');if(webglOk)makeMissionProps();msg('관절 6개를 조절해 빛나는 목표에 집게를 접근시키세요.');resize()}
function update(now){const dt=Math.min(.05,Math.max(0,(now-(lastTime||now))/1000));lastTime=now;if(mode==='sim'){if(!done){remaining=Math.max(0,remaining-dt);if(remaining<=0)finish(false)}const m=Math.ceil(remaining),mm=String(Math.floor(m/60)).padStart(2,'0'),ss=String(m%60).padStart(2,'0');byId('clock').textContent=`${mm}:${ss}`;byId('clock').classList.toggle('warn',remaining<30);if(webglOk){axes.forEach((a,i)=>{a.node.rotation[a.axis]=angles[i]*Math.PI/180});fingers.finger1.position.x=gripOpen?-.28:-.16;fingers.finger2.position.x=gripOpen?.28:.16;rig.updateMatrixWorld(true);if(held&&carried&&objects[carried]){const p=toolPos();objects[carried].group.position.copy(p);objects[carried].group.position.y-=.15}if(mission==='satellite'&&objects.signal){objects.signal.group.position.x=-1.65+.38*Math.sin(now*.0015);objects.signal.group.position.z=-1.5+.28*Math.cos(now*.0018)}const trg=currentTarget();if(objects[trg]&&objects[trg].ring)objects[trg].ring.rotation.z=now*.0008;let d=objects[trg]?toolPos().distanceTo(worldPos(trg)):100;byId('indicator').textContent='TARGET: '+(d<.85?'IN RANGE':'OUT OF RANGE')+' / '+d.toFixed(2);byId('indicator').style.color=d<.85?'#8df5ae':'#a7bfd1';byId('stepName').textContent=mission==='satellite'?`STEP ${step+1} / 6`:mission==='battery'?`STEP ${step+1} / 2`:'SAMPLE MISSION';byId('readout').textContent=angles.map((a,i)=>`MOTOR ${i+1}: ${a.toFixed(0).padStart(4)}°`).join('\n')+'\n\nREAL MOTOR: DISCONNECTED';camera.position.set(orbit.radius*Math.sin(orbit.phi)*Math.sin(orbit.theta),orbit.radius*Math.cos(orbit.phi)+1.8,orbit.radius*Math.sin(orbit.phi)*Math.cos(orbit.theta));camera.lookAt(0,2.0,0);renderer.render(scene,camera)}}requestAnimationFrame(update)}
setup3D();buildSliders();requestAnimationFrame(update);
})();
</script></body></html>
"""

assert GAME_HTML.lstrip().lower().startswith("<!doctype html>"), "HTML START MISSING"
assert GAME_HTML.rstrip().lower().endswith("</html>"), "HTML END MISSING"
components.html(GAME_HTML, height=900, scrolling=False)
# END OF MECHA LAB 2.0 MAIN.PY — COMPLETE FILE
# MECHA LAB 2.0 | SINGLE-FILE STREAMLIT APP | BUILD 2.0.3
# GitHub: main.py must start with these Python imports, not .subtitle or other CSS.
# This is an interactive SIMULATION. It does not send commands to a physical robot.
import base64
import zlib
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MECHA LAB 2.0 | 6-AXIS", page_icon="🦾", layout="wide", initial_sidebar_state="collapsed")

st.markdown(
    '<style>'
    '[data-testid="stSidebar"],[data-testid="stSidebarNav"],'
    '[data-testid="stSidebarCollapsedControl"]{display:none!important}'
    '.block-container{max-width:100%!important;padding:0!important}'
    'body,.stApp,[data-testid="stAppViewContainer"]{background:#080e1b!important}'
    'iframe{display:block}'
    '</style>',
    unsafe_allow_html=True,
)

# Self-contained HTML/CSS/JS payload; the 3D Three.js library loads from a CDN.
# Encoding prevents broken multi-line Python strings and accidental CSS indentation.
PAYLOAD = (
    'eNqtfetz21aW53f9FYjcNskYhACQ4NOUI8uKrW7bcklyp7Nu1QQEQBExSXABUI/Q3Eq6lawncVcnkzjtTGyPM5PsJL2uXiVxd9w12S/5U/qjSN'
    'Xun7Dn3AdehGS5d6YmFnlxH+ecex6/c+4F+9xLpmP4u31LaPvdzvzMOfwjdPTeZmP2ljM7f65t6eb8ua7l64LR1l3P8huzA7+Vr8zOseae3rUa'
    's1u2td13XH9WMJyeb/Wg27Zt+u2GaW3ZhpUnX0TB7tm+rXfynqF3rIYCk8yc8/zdjjU/84rdxQmEgdvJZtq+3/dqc3MtmMyTNh1ns2PpfduTDK'
    'c7Z3ieer6ld+3ObmMNiLLOrltG++xVp+ecYc2r+ptmW+/Zte3Ntv9KUZbrGvxXgv/KsnzGtL1+R99teNt6P5Orz9Rcx/GH+bzdu1U7ZVVbWqtV'
    'z+dNu1s7VWnqWtOAb5a5adVOFTRNKenwdbOje17tlCIrrULJqkBLszOADlrLLJHRjgtChIaWqmslE0c4jgnzyS2lWYKvrgXfWq2yWtFGMy8Pm8'
    '5O3rPfsnubtabjmpabh5YR7obYdMzdIZFfTZHl0/W2ZQNT9HNXdzftXk2uN3Xj1qbrDHowq1yRLaVZN5yO49a2dDdLOMvVUZh5KqBahksoI2au'
    '6p3NQU+45Pht28iInt7z8p7l2q26s2W5rY6zXWvbpmn1RjPNge87PdHu9Qf+EOer2b02dPVH9MnQGLgerNp3bNACl7XWWo4x8PJbtmc3OxYdHW'
    '8bOgO/Y/esmtrfETynY5sCJRylmquzp3mn1QINrBX6O6OZU2TTArlsbUcEs9Wud+1enjVomtzfqfcdD3QPiHGtju7bW1aSu6gMXd1ENd3Ev6DM'
    'WavTsfueJei+oMmnBUWVT4un1GIRlEHAj3JTKaoVoVjFz2XZUKoC7k8OyPR8MJthsLreBPYGvlW3e8iKXGeiyltbsJBX6zm9KcpGEk6SMgflHm'
    'TGecePUVVolk0T1BH2uauTof42qELHElSp6IE1ttAgga0OUNDTfYuuVOv57bzRtjtmttDLcRmHq8DHqY4adIyu3GqBEMzRzCu3rN2WCz7CE9ja'
    'w5brdIdOXzdsf7cmKeWR74Rfq6URzG24ltU7RmjMgom0eHdJN3Bbh/xZs+MYt7jKxmhTNFUvFurU0JAbpnKnimqpWtGY5ZyySq0iCI+YzTblHL'
    'xHvWP5uF8eUgzminLp66ZJPoOiCYqGm0CNGPVn4NWK0OKDQ2DsSKrH6aq1ca9j1KnlYrVU4TMwWsqaYVqlkdR3YSfd3egAaijU3+QSw1plQ61y'
    'V3BKAb0tFINJUtZutUy5agX9ZehfHs1IXXCtomTtWk3X2Ralvt3piKgAvijB9oqSb3ctV5TsnmntDGNuhvhnAf2zgP45I+JUKDorRY5gLWALri'
    'NIm65ttnTTOkYFImSjb9Dd0FqJqPuwcM8XqgUwyWKzWmqaiilUi6dzYrJ7VTatTfH4QZHl0E9btRLssoD/0I1tOW631rdcr28RLcwSp5MTXAek'
    'ZP0qW1JhjZxA4l5WzYWDYONsdOGGhV5AaDqgFV3w696tPGwSRJDjmFOI75FloQK+ph7YUAm2jAgyD3YAvnM47fveypPNqimxcMJNp9Wxdur4Dw'
    'RBFxmCoaATg26v/ubA8+3Wbp6FeUZ3Xe/Ym708+JKux5t8a8fPk3bews1EVXGvuT5RhSFCVcCzJ/UCbYcbgWq0LH0kgfLeiowyOnq3DxLu74iK'
    'srUtKsUSiP55dlvGpTCoMAFIVR5NFVhSkIVquHBLbZXBExCOvLZugmeWoUcRzf2UVjKMVgvshNAlwPwQBiOxl1kmMOwNmr7towdM0I4riiqQjp'
    'LJ8VWrraYxbScoIkaoRuhUNXTHsG89y0+xl7gngujFokahAiGzq+9QaFYrVjBI6kR/oTPMAbpxTEQ0bNfokIBYgICoVtBgqiWz2oS4WCoYpSIL'
    'hqZSLhSEcgn00yVyzivAaN13+vCpAJ8I8gllWiUyLSglUzcLcqjTmhYoNQjY6gynvXehqBVKRhwKVRVAWEYz9NCw7YKqEBly1jVVDmUqC/rAdw'
    'QV1S6imKWEtihAEN8no2jqljaKUid48LG3OeT607IKTSVgoOn3vGHM1jb1fk3B4J1uXhji9B6uP0yDCydykq7Vt2Bbe5v5pEeZcn9y7BvqJjoZ'
    '/D9D0FBBufeoAkuwk0MmlDJyEOMryQ7x/Pmm5W9DwE5zGnyfZFCrBJaBvSypZbNaDwAyusqoAqhGsVJS6kd7OxXobQJr5vA5zkGN7b6KgJMOFJ'
    'qpto1SyBP9PnH4iyiXGngaOitkHrn08OhZHbBPQerangccelzyEFaMLLpwIS+UiQ/5T3XlgeNG41RJ5JOJC/fojHlME6HDcNrnU7Pim6WWCXSM'
    'jxLaypRHLAC/YlEqg0/UFOTnaC+IXkNLm7bPza9a1ltGMUyW4nYNbBi6a4YWieCjjv/kQQbQ4lt5KjGPGVG2IEJ6AQ4kq6DXFFV0WrkctWL0FN'
    'SvQB+yJ2KVYIER37VhJDdRtYSaJ41T0Yh5nlIqoN3llgymaClVtWVVcykAtmBoZrkaC7R/jybEzTSe0yWBLOeKockQDZFPKL3Xs3kSkGPQNIla'
    'I0EAAq9QQD+NXofAT7qCIPUG3RPbF9v7SrkpG+WEtY3CKb3dbtPpRPRPK065+mLYv60OmRoRkBB1EsXovP0oqolAmKZuyqaZnJ+rJma/coQ4aj'
    'XDF3CpTMYYXuNqUSyVuFrQp0pgQfR70gnxrfn7/Bn6Krsbyy0gRy6oBTBTu4sWyl1XqRhJoADNyEmVTfFHQbiMZXWK0ioUjo4OBblY1prHRIeQ'
    'NtzmyM5G4UF9uw2kED9kQfTddvV+OAwSod5udOeVcOerShO2ISXQRIZvEjjcQVw+oklVZDISEANAYWpVg/WRtnW3F0KNsoIlJWnbcW/BZukncW'
    'vMm8mi0nJzEHnlMNePRhbcKoJjfUhMUpIK9GvU9cl/b3GlcBpCC+BGxSxUNZXWVgyQnCJoRV5nKQW1FV51PKo8FisFAOYcGO28Tj0fAU7MswEl'
    'zVEwWY3VESIPm7BVnO88/JMCs4kNaSR9acHqFVJxmoZqpGaGqiucxHe1TMgs0lQmQgtNOOKc8vFKtdmcwjZy1Ow1VsrxB14ztcTE7UgNWEMmKZ'
    'QnH4+0VRJqrJ75HI+VJiVi30XOJ9CWdCRGQbbSCjiFCqQAeqIeU4ihfYzKGsIXkSTNCTcdd8wFjQsngfuwmJsjeN60Dd13qJ0SexderOZRn+bM'
    'VJ7PWZUKxzYt3LaYG5TBdpTA/vK7NUxouFukWxiZtqQpkDMFAkNsF+RIkFVCMpMPc9YTa24ZM1c9DVVHQJvCnB/hQZDaVqc/VQtIxEkeRWXAOU'
    'HULJE0WCHQ8k3UJh6iyXbEnpAU6v8vQ4kDWi2YGs9BXkxIZtWqtuTIcMHqRvUoLNFHSvLctJt6pclhDR6ggOG4Xb0zkgAtupYVhgOzWDWZ2yke'
    'T9dohlTmb+J5UINE/42oY9UNlEBQWZT1crmZwIawm0BDJ5bfHhN2INoI8B8x93KoG0qJwqBgLoHVcBMpU8QWaAIA0c7EcleK9QCMLjWTtlZSKw'
    'lXoSZAUTEyrSBt6Z3BC+5xs2KpVhLvlWMgou9aeYQRdYjYZr4Jq92qkX/z2AB5p25uhkprkzJAnvr5AOdjRsZSVsrJiaJLq9CspFXBS+WSZkJ4'
    'RR8Ca56sCHtKLkGkrpharDifZkFH5J0chpXidUJOheS1ARxFbRd0HXCEk5Z1HpdQFTWaUFl4mCeivwSfm5ZMlZpVTdeiNTKSrEVMghNaIAUCSk'
    '08m9Uq6RVNpupVkkSwDdGLLa3Z4vNILd3u4GSBJVcqVTVYJUhumxXIKFrROFYm8Lvn+LZhHYdUIkH8hXQafEpJL8exd0GtFPSgNhPTpkJJLRcC'
    'UVViwZimv5H9IzSNZl7pWsBnNuxYQUyaG5JqU5gsKMTsafZ+pIshy/EKFR4NJkJjal6uYG33uDSxIKeUHIbx4KAQtQiA+Emwt1rQIkExYFVRIn'
    'nCkPvLUBCVaBoRS16oiJK5BK1ohXg2fILAIkX+WpnKfyqrOLqqwObneZ5WPk37eW0XD9rlkEvWo1g4HYMp8lHZbBEP4SPIgQRQcEgvUMFRxZjc'
    'ae1GFuiOxUBEcBiQTPMSZ5Cpwi8QaZ6bo3cczs3R6xR4oj9/zrS3BNtszOI59mz4lZwXw/c5aKCtBt41gAesBMyfzZxj2keGkcrybNgXT0QFms'
    'nMxqahBwVpC/BDt7Rn0eOkWVg68ogd48zOr6xeWF5fuCKsrlxYWV9eXBPmhOVr60urC4vry79cEq4sXJieF49MZuevLi1eXhDOYSYzT7qRT5zN'
    'qAzYCcrsfCm/8KvlNb6WsLB6VVhbvnrjysL6ymrKwEhtHtjD6QMKwL3NCmSDGrMcvpYA61SAruW1teWVa8KVlUuCrAI/a8uXriGHS4tLwNJFTm'
    'jTnYNJScl/fvL5hwfffSNMvtifPPpo8nBPmDzYO7z3QJjsfz3Zeza++7Yw/uLB+Ol/P7z7iTD54MHk/S8P330wefhUmHz59vive+MP70/+cGfy'
    '/p/HH9wZf/ClhLpD5iWLHOy/PfntO8LB07cnj+8IpYP9B+OvfhQm//7O5PFHwuTxg8mnTw/vwQRPhMPPPpnsfYsrjP/trjD5dm/yw9eicPCXL8'
    'e/3xPG+/uHe/vj//FEGP9lD/6ISCTp/vge0CBMHu2NnzwlU9+5f/jpP+Kce88m//yJdKRoEaeBZClSC3SNHjTPBortX/B7s/N/+/Qvwtr6wuq6'
    'cGnh6tK5OTooGIydMRmgfT++L1xeeU1YXxGuX1l4PexMVamf1EK+k4kizJGZCHEuaqRCV1Grht6anWfahNt/deXikvDTD8K1FeHywurF1xZWl4'
    'SVG+vXb6xj64Uby1cuCqokSwXhl0ury68uo2L0OYVzzEoT9kor+QmDjVsqUBZvICcQgbU0qak0U6w1OI0IVXht6crS4jqosFwQFn65sAxjryxx'
    'Eqeskh0vxJdPBLv4w8ALLF5eWVkD+VwHw0fpsdnbyjwjgVEEzlCB/ZsvTf5yLzQJYjDEdJgeH+y/c6w69lPIJ4Ag4aUYS7OCqft6nn1D52vcoo'
    'zEZugNuqHoQGZKijsmiGB2/v/+yx+/5jyq89zs7sGfh8zsgFMVOZ38+0cH390lbBCrnPzhQzC4jw5++BH9wI/gIh59MXkI/uGfvkRGofvhva8n'
    'D34E4QiT+386eLZ/LNcUdDDvNi8rAFG4f2KO9ca1xcvC3977Q8y/plj0EbJq6mhDuycQl3qcuD75IBRX0hEFonr0+ODZncmjryZ/vY8CO7z3FL'
    'wbulEUTjCKOj/whffonw+5tB4+Hf/+M5Dq4W++fBGZqTX5P1lmHmCPTgfSnxNIrXCc1D7f/z/Pfh8KbvLw2cH3f+Ze+879iOzGv/sTxIWffhh/'
    't3f4/o8//QARBvv99T58fAz9H8Pfe3cO3707/s19GPpgsveAyIy4/ueZVkJgxRcUWNTfHOUY7e6xXpEBrdlYuMBcBMMF9/4cGWMlC/NhiCPvfc'
    'g9z1pqxGkNOh0yBQEYjVmU1XdPwZ7H3zw9bt7P/xJON+WHASfOzkcxypywuHJtfXXlinBxafEXwX4SCpjSrFOAc7QnSQFu6HhTwgAuz2Kv1b+m'
    'd2Ha9YW1X6T1hPyAdjU6xCUy/3GEtvM0ILE1iPehCYDqlu6R2YJ7wTALbZ4egRkIj2oQlkBGVxAvFi5SlRp//GD86P7BD89qBC89/lA4/Oe7sD'
    'sYew8fPK4B1LkHsGoO4sjkvbtxteOgmibDs/O/XF5dvwEAjkf0krDwq6U1/LSFATzNb/Ha+GxKcwBs8DNo0/zq0sJFxCjzDKJFw9lTYfzHbw4/'
    'ehC6/SSsiqMqVlmeZfCef4UdXL20tF5DBCKsvCqsLly7FA/kbLt0zI9CqyG5UiIVCKq7s/M/XwGsHijnHEgIgLSwfBFi39/e/lguTVOIEG12fn'
    'JvD3ZHmLz/ZPzwR/S7v/sEvQlCUwF3JBbPKbOwjV+CNwfR5xV1AaTyNXhzkMr4fUDE9/YAzULbu+PHf8XB4++fjn/zFLw7PHo/CouT5PAkkMqL'
    'fFt0EJp2vNnUVIJXF49HrZAUUSBKo7cw/uB/QiAWsmvXFxaXcqmexLWADDrm6R3oDJacjnGdrkW6QZ/x988g/H8IEkrtau2gEdHO++8QCA/e/z'
    'dPEnA4xiArWx655dynxWsWRXRq64DUri6tr74OisBMZlrgpBo6yzhmS/1cqQmyJP+0fxSyJEqTWJkfR4Mzffs/hMP7e5NHT8D6uQmhEr3NdQZE'
    'dfDnJ5OH90m82qftz74Q0B8ATAQHgfo0/t2zyaN3mapgl/GTHwUYB6Dgpx8O33t8+M4TUM4H48dfEbwFYe8zCIPforOH9OtTyMUe3ZnStTliUD'
    'FJI++sPBkXMy3SUeGwz+lomYf/1aXrK6vrAVamMw98w0GfvXZjcXFpbY0h5uizdWsHpE7xsTD5bA9QJYnbuBQT8rGnHdHzdBLOjjMF1/LdXZqU'
    'vfcfQDHoR6qy0tSGdJyOuFOOKooDaANEfbvvC55rgL6wF0EMsye96ZlWx95ypZ7lz/X63Tm/DfDgFVlSilVJhhXsjknbpK6N3dHu6WR80vmZbD'
    'bXmB9mBp6Fd/Rsw8/UZ0Aani80d5fNBtA/bzrGoAuCkTYtf6lj4ccL8CxrmzneF69Jeo0hZg+1ITGnWiYtYGdEYM7pmV6tKo9EBqCDEUn0G/ZW'
    'VOgeYMdgQArqC8eoRXk04gQSd77WuDnEc6Va5sICpGSvL7yWEfUd26tlXs+MRPZo7fLKjSsXl1b5o/8SPlq6cmHltZT211aX19aF68vri5ePfA'
    'pR5Ap/+Kvw4foKRJc4IRv1GcjOha5jWo0MKSZkRI6fMyhh6Nvb7Fhe46Ys5guyqGliXtVEWZQ3RPAnZqOldzxLNJ2exT66Vle3ewDUGlVZBE32'
    '1wHfNGQRYRD8ARH1QOcsE5vsLnuInn6lb/UavjuwRMghXRt69AAWiqQm17jJKHWtnmm5lit6YD7YE7CTLkK+DTwhlRuib/ev6u4t6IKT9uGv03'
    'wTVgSVGYmO27T9xtBvW75ek6WSJvbbdk2RlILILukq6khkJ2p0/W2rudlZuUW541tMLso1sjuiLjZBp6/qfhv1PtsU6Ud9J6uLeC1tpjXoUXyN'
    'RyjZ7bZttHNDIm/yuR4o/H8dgHquEfN13IVOJ5th71ZkclLLcZd0o531GvOeRNzDFdvzJd/ZhL3JZmipEbRRAhNq0IlhbbtF14OmDIg6k4PQiP'
    'IG/5WFOGm/ZYmqnBuFJHa9zawn0lOLLbafuSHaZjZDgRbQYsP+uZfXr15pvHGuGa/d/WzIx57PnKoYrWKzkqllTukls9lqZUaz89EOK7+AZ8xH'
    'ZUYEt/1s6I3eAHocN4t7bTfkun2uCv+cPZsbUsH3GoHAQDhgpMxJZDN2JlfvUeEg2m4gxW4GmgiJEla1G9ms/XJJkSqF3GlFlnNnM6fDDhAJyf'
    'NCWSqnPQ/e47lo4ftrWfu0ouRelgrK2YyXqQdCclFGOuhdz1wkL+f0QMLhU3TN0MHpGR3buNVAh0gUI0MdN74RRzuzIlyiL9sMaqm5uM6AwkQq'
    'rbGdypy46hop9wH+oIUkwKKXbixfXIpWXMf/69nk3fsIEg++fzz+6hmpDfxc+W8/L03B0Uh96T7DWaR2AMj08b0oMiUg72AfQcHnkB8jJA1RO7'
    'Qf/PXu5PO7AEchKxQIBhTG9ylyZfiQZN28DvHoo8kf3j289w2HIquHv/mSzElIh+dPMKV59JEoLHlG4tne48PfPhRoAsrmG//+LgBkJOPZfghw'
