import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MECHA LAB | 6-AXIS", page_icon="🦾", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
#MainMenu, footer, header, [data-testid="stToolbar"], [data-testid="stDecoration"],
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapsedControl"]{display:none!important}
html,body,[data-testid="stAppViewContainer"],.stApp{background:#090e1c!important}
.block-container{padding:0!important;max-width:100%!important}
[data-testid="stVerticalBlock"]{gap:0!important}
iframe{display:block}
</style>""", unsafe_allow_html=True)

GAME = r'''<!doctype html>
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
<div class="intro-btns"><button class="primary" id="startBtn">▶ START GAME</button><button id="helpBtn">ⓘ HOW TO PLAY</button></div><p class="eyebrow" style="font-size:11px;letter-spacing:2px;margin-top:24px;color:#829caf">SIMULATION MODE · NO HARDWARE OUTPUT</p></div></section>
<section id="select" class="screen"><div class="top"><div class="brand">MECHA <b>LAB</b></div><div class="top-right">MISSION SELECT / 03 AVAILABLE</div></div><div class="missions"><div class="section-heading"><div class="eyebrow">CHOOSE OPERATION</div><h1>SELECT MISSION</h1><p>6축 로봇팔을 조작하여 각 임무를 수행하세요.</p></div><div class="cards">
<div class="mission" data-mission="rock"><div><div class="num">MISSION / 01</div><div class="symbol">🪨</div><h2>화성 암석 채취</h2><p>집게를 시료에 접근시켜 잡은 뒤 수집함으로 옮기세요.</p></div><div class="bottom"><span>01:30</span><span>LAUNCH ↗</span></div></div>
<div class="mission" data-mission="battery"><div><div class="num">MISSION / 02</div><div class="symbol">🔋</div><h2>배터리 분리</h2><p>잠금장치를 해제한 뒤 배터리를 지정 지점으로 이동시키세요.</p></div><div class="bottom"><span>02:00</span><span>LAUNCH ↗</span></div></div>
<div class="mission" data-mission="satellite"><div><div class="num">MISSION / 03</div><div class="symbol">🛰️</div><h2>인공위성 수리</h2><p>덮개·버튼·스위치·전선·안테나 순서로 정비하세요.</p></div><div class="bottom"><span>04:00</span><span>LAUNCH ↗</span></div></div>
</div></div></section>
<section id="sim" class="screen"><div class="simhead"><button id="backBtn" style="padding:7px 10px">← MISSIONS</button><button id="fullBtn" title="전체화면" style="padding:7px 10px">⛶</button><div><div class="tiny">ROBOTIC ARM / CONTROL DECK</div><h2 id="missionTitle">화성 암석 채취</h2></div><div class="grow"></div><div class="tiny" id="stepName">TASK</div><div class="timer" id="clock">01:30</div></div>
<div class="workarea"><div class="stage"><canvas id="viewport"></canvas><div class="stage-tag">MECHA LAB / LIVE 3D<span>드래그: 시점 회전 · 휠: 확대/축소</span></div><div id="notice">VIRTUAL MODE · 6 AXES</div><div class="statusbar"><div class="status" id="status"><b>READY</b> 관절을 조작해 목표에 접근하세요.</div><div class="indicator" id="indicator">TARGET: OUT OF RANGE</div></div></div>
<aside class="sidebar"><div class="pane-title">JOINT CONTROL / MOTOR ID 01–06</div><div class="help">아래 슬라이더로 6개 축을 조작하세요. 실제 AX-12A 모터에는 아직 명령을 보내지 않습니다.</div><div class="jointset" id="jointControls"></div>
<div class="smallbtns"><button class="primary" id="gripBtn">집게 닫기 (SPACE)</button><button id="resetBtn">초기화</button><button id="homeBtn">기본 자세</button><button id="exportBtn">각도 복사</button></div>
<div class="readout"><div class="pane-title" style="margin-bottom:4px">TELEMETRY / VIRTUAL</div><div class="value" id="readout">J1: 0.0°</div></div><div class="help" style="margin-top:11px">※ 현재 3D 관절축은 실제 기구의 정밀 실측 전 임시 모델입니다. 실물 구동·토크 출력은 비활성화되어 있습니다.</div></aside></div>
<div id="overlay"><div class="dialog" id="dialog"><div class="eyebrow">MISSION REPORT</div><h1 id="outcome">SUCCESS</h1><p id="outcomeText">임무 완료</p><div style="display:flex;justify-content:center;gap:10px"><button class="primary" id="retryBtn">↻ RETRY</button><button id="selectBtn">MISSIONS</button></div></div></div></section>
</div><script src="https://cdn.jsdelivr.net/npm/three@0.152.2/build/three.min.js"></script><script>
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
byId('helpBtn').onclick=()=>{byId('intro').querySelector('.intro-panel').innerHTML='<span class="mono" style="color:#76cce8">HOW TO PLAY / OPERATOR GUIDE</span><br/>미션을 고른 뒤 J1~J6 슬라이더로 로봇팔의 자세를 조정하세요. 집게가 빛나는 목표에 가까워지면 SPACE 또는 집게 버튼으로 작업합니다.<br/><strong>화면은 3D 시뮬레이션이며 실제 로봇팔은 움직이지 않습니다.</strong>'};
document.querySelectorAll('[data-mission]').forEach(x=>x.onclick=()=>launch(x.dataset.mission));
byId('backBtn').onclick=()=>{show('select')};byId('fullBtn').onclick=()=>{if(!document.fullscreenElement)byId('root').requestFullscreen?.();else document.exitFullscreen?.()};byId('resetBtn').onclick=()=>launch(mission);byId('retryBtn').onclick=()=>launch(mission);byId('selectBtn').onclick=()=>show('select');
byId('homeBtn').onclick=()=>{angles=[0,-30,55,-25,0,0];syncSliders();msg('기본 자세로 복원했습니다.')};
byId('exportBtn').onclick=()=>{const data=JSON.stringify({mission,angles_deg:angles,motor_ids:[1,2,3,4,5,6]},null,2);if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(data).then(()=>msg('6개 관절의 목표각 JSON을 복사했습니다.',true)).catch(()=>prompt('아래 값을 복사하세요',data))}else prompt('아래 값을 복사하세요',data)};
byId('gripBtn').onclick=act;document.addEventListener('keydown',e=>{if(e.code==='Space'&&mode==='sim'&&!e.repeat&&e.target.tagName!=='INPUT'&&e.target.tagName!=='BUTTON'){e.preventDefault();act()}});
function buildSliders(){const wrap=byId('jointControls');wrap.innerHTML='';JOINTS.forEach((j,i)=>{let box=document.createElement('div');box.className='joint';box.innerHTML=`<div class="jointline"><span class="jointname">J${i+1} <em>${j.name}</em></span><span class="degree" id="deg${i}">${angles[i].toFixed(0)}°</span></div><input aria-label="J${i+1} rotation" id="slider${i}" type="range" min="-145" max="145" step="1" value="${angles[i]}">`;wrap.appendChild(box);box.querySelector('input').oninput=e=>{angles[i]=Number(e.target.value);byId('deg'+i).textContent=angles[i].toFixed(0)+'°'}})}
function syncSliders(){angles.forEach((v,i)=>{byId('slider'+i).value=v;byId('deg'+i).textContent=v.toFixed(0)+'°'})}
function mesh(g,m,p=[0,0,0]){let a=new THREE.Mesh(g,m);a.position.set(...p);a.castShadow=true;a.receiveShadow=true;return a}
const mat=(color,metalness=.25,roughness=.5,emissive=0)=>new THREE.MeshStandardMaterial({color,metalness,roughness,emissive});
function cyl(r1,r2,h,m){return mesh(new THREE.CylinderGeometry(r1,r2,h,20),m)}
function box(w,h,d,m,p=[0,0,0]){return mesh(new THREE.BoxGeometry(w,h,d),m,p)}
function addArm(){rig=new THREE.Group();scene.add(rig);let blue=mat(0x8ca7b5,.65,.36),lite=mat(0xd9e5e4,.55,.34),joint=mat(0x243847,.45,.45),red=mat(0xe47c69,.5,.44);
const baseplate=cyl(.78,.9,.4,joint);baseplate.position.y=.2;rig.add(baseplate);const yaw=new THREE.Group();yaw.position.y=.45;rig.add(yaw);axes.push({node:yaw,axis:'y'});yaw.add(cyl(.52,.53,.45,blue));
const shoulder=new THREE.Group();shoulder.position.y=.55;yaw.add(shoulder);axes.push({node:shoulder,axis:'z'});shoulder.add(mesh(new THREE.SphereGeometry(.36,22,15),red));shoulder.add(box(.53,2.15,.51,lite,[0,1.08,0]));
