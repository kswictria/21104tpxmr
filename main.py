# MECHA LAB 2.0 - 단일 파일 Streamlit 앱
# GitHub에 main.py와 requirements.txt만 올리면 됩니다.
# 실제 모터 제어 기능은 아직 없으며 6관절 시뮬레이션만 실행합니다.
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="MECHA LAB 2.0", page_icon="🦾", layout="wide", initial_sidebar_state="collapsed")
st.markdown("""<style>
[data-testid="stSidebar"], [data-testid="stSidebarNav"], [data-testid="stSidebarCollapsedControl"]{display:none!important}
.block-container {max-width:100%!important; padding:0!important}
header[data-testid="stHeader"] {display:none!important}
.stApp {background:#090f1c}
iframe {display:block}
</style>""", unsafe_allow_html=True)

# HTML + CSS + JavaScript 코드도 이 Python 파일 안에 들어 있습니다.
# assets 폴더나 외부 사이트에서 불러오지 않습니다.
GAME_HTML = r'''
<!doctype html>
<html lang="ko">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>MECHA LAB 2.0</title>
<style>
:root {color-scheme:dark;--ink:#e9f1ff;--muted:#91a6bd;--orange:#f1a675;--line:#34465d;--panel:#111e30;--panel2:#17273b}
* {box-sizing:border-box} body {background:#09111f;margin:0;color:var(--ink);font:14px/1.45 system-ui,'Malgun Gothic',sans-serif}
.shell{width:min(1600px,100%);margin:auto;padding:22px 22px 35px}
.top{display:flex;justify-content:space-between;align-items:flex-start;gap:18px;margin-bottom:16px;flex-wrap:wrap}
.kicker{font:700 11px/1.5 monospace;letter-spacing:2.3px;color:#7fc5d4}
h1{font-size:clamp(27px,3.2vw,44px);line-height:1.1;margin:5px 0 8px;letter-spacing:-1.3px}
.subtitle{color:var(--muted);font-size:13px}.tag{border:1px solid #4c5b6c;border-radius:30px;padding:7px 11px;font:700 11px monospace;letter-spacing:1px;color:#ffc49e}
.layout{display:grid;grid-template-columns:minmax(0,1fr) 345px;gap:16px}
.stage,.panel{border:1px solid var(--line);border-radius:16px;background:var(--panel);overflow:hidden}
.stagebar{display:flex;align-items:center;justify-content:space-between;gap:8px;flex-wrap:wrap;padding:12px 16px;background:#15243a;border-bottom:1px solid var(--line)}
.stagebar strong{letter-spacing:1px;font-size:12px}.subtle{font:11px monospace;color:var(--muted)}
#scene{height:620px;width:100%;position:relative;background:radial-gradient(circle at 55% 45%,#1c3551 0,#0b1728 58%,#08121f 100%);touch-action:none}
#scene canvas{display:block;width:100%;height:100%}
.corner-label{position:absolute;pointer-events:none;bottom:15px;left:17px;color:#98bbcd;font:11px monospace;letter-spacing:1px}
.corner-top{position:absolute;pointer-events:none;top:14px;left:17px;color:#ffc18b;font:11px monospace;letter-spacing:1px}
.floor{display:flex;gap:16px;align-items:center;justify-content:space-between;flex-wrap:wrap;padding:12px 16px;background:#122034;border-top:1px solid var(--line)}
.status{font-size:12px;color:#adc9dc}.numbers{display:flex;gap:18px;flex-wrap:wrap}
.numbers b{font:600 13px monospace;color:#f9c394}
.paneltop{background:#17283e;padding:17px 17px 14px;border-bottom:1px solid var(--line)}
.paneltop h2{margin:5px 0;font-size:19px}.paneltop p{margin:5px 0 0;font-size:12px;color:#9bb4c8}
.reference{margin:12px 15px 0;padding:12px;border:1px solid #516c84;background:#20344b;border-radius:10px;display:grid;gap:5px;font-size:11px;color:#cde7f2}.reference strong{color:#ffc698;font-size:12px}.reference b{color:#ffffff;font:700 12px monospace}.reference small{color:#93afc5;line-height:1.5}.controls{padding:13px 15px;display:grid;gap:10px}
.joint{padding:10px 12px;border:1px solid #30455d;background:#152438;border-radius:11px;transition:border-color .2s}
.joint.active{border-color:#f0ae77;background:#1e3041}
.jrow{display:flex;align-items:center;justify-content:space-between;margin-bottom:7px}
.jname{appearance:none;background:none;border:none;color:#e8f3fc;cursor:pointer;font-weight:800;letter-spacing:.6px;padding:0}
.jname span{font:11px monospace;color:#9bb7ce;margin-left:6px}
.jvalue{font:700 14px monospace;color:#ffd2a8}
input[type=range]{width:100%;accent-color:#eca278;cursor:pointer}
.scale{display:flex;justify-content:space-between;font:10px monospace;color:#7290a9}.rawrow{font-size:10px;color:#a7c3d1;margin:0 0 5px}.rawrow b{color:#e0eef8}
.actions{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:0 15px 15px}
button.action{cursor:pointer;border-radius:9px;border:1px solid #52647a;background:#263b52;color:#f0f5ff;font-weight:700;padding:11px 9px;font-size:12px}
button.action.main{background:#da926d;color:#101c2e;border:0}
.warning{padding:12px 16px 15px;background:#101c2c;border-top:1px solid var(--line);color:#acc2d2;font-size:12px}
.warnstrong{font-weight:800;color:#f3bd90} .legend{display:flex;gap:13px;flex-wrap:wrap;margin-top:8px;color:#9eb3c7;font-size:11px}
.dot{height:8px;width:8px;border-radius:50%;display:inline-block;margin-right:4px}
@media(max-width:950px){.layout{grid-template-columns:1fr}#scene{height:500px}.panel{max-width:none}.shell{padding:15px}}
@media(max-width:500px){#scene{height:390px}h1{font-size:28px}.numbers{gap:8px}}
</style>
</head>
<body>
<main class="shell">
  <header class="top">
    <div><div class="kicker">MECHA LAB  /  ENGINEERING SIMULATOR</div><h1>6-MOTOR ROBOT ARM</h1><div class="subtitle">ROBOTIS CM-530 · DYNAMIXEL AX-12A · 3D Kinematics Lab</div></div>
    <div class="tag">● SIMULATION ONLY · NO MOTOR OUTPUT</div>
  </header>
  <div class="layout">
    <section class="stage">
      <div class="stagebar"><strong>3D WORKSPACE / MOTOR ID 01—06</strong><span class="subtle">DRAG: ORBIT &nbsp;·&nbsp; SCROLL: ZOOM</span></div>
      <div id="scene"><div class="corner-top">PHOTO-BASED APPROXIMATION / 6 MOTOR IDS</div><div class="corner-label">REFERENCE MODEL / NOT YET CALIBRATED TO HARDWARE</div></div>
      <div class="floor"><div class="status" id="status">3D 도면 준비 중…</div><div class="numbers"><span>JOINTS <b>06</b></span><span>MODE <b>VIRTUAL</b></span><span>H/W <b>OFFLINE</b></span></div></div>
    </section>
    <aside class="panel">
      <div class="paneltop"><div class="kicker">JOINT CONTROLLER</div><h2>관절별 상대 회전각</h2><p>실측 모터값 935 · 500 · 413 · 482 · 736 · 396 기록됨 · 가상 관절 편차 ±80°</p></div>
      <div class="reference" id="reference"><strong>실측 기준 자세 / 2026.11.23</strong><span>모터 ID 1→6: <b>935 / 500 / 413 / 482 / 736 / 396</b></span><small>기준 자세에서 상대 회전각 0°. 모터 원시값은 실측 데이터이며 슬라이더로 보내는 명령이 아닙니다.</small></div><div class="controls" id="controls"></div>
      <div class="actions"><button class="action main" id="home">초기 자세</button><button class="action" id="pose">예시 자세</button><button class="action" id="copy">측정값+각도 JSON</button><button class="action" id="resetCam">카메라 초기화</button><button class="action" id="grip">집게 열기/닫기</button><button class="action" id="axes">회전축 표시/숨김</button></div>
      <div class="warning"><span class="warnstrong">⚠ 실물 모터는 움직이지 않습니다.</span> 6개의 모터 ID와 실측 원시 위치값만 반영되었습니다. 실제 링크 길이·회전축·영점이 확정되지 않아 현재 외형은 근사 모델입니다. 모터 구동 명령은 포함되어 있지 않습니다.<div class="legend"><span><i class="dot" style="background:#f0a96f"></i>선택된 관절</span><span><i class="dot" style="background:#76c9d2"></i>기타 관절</span></div></div>
    </aside>
  </div>
</main>
<script>
'use strict';
// Offline 3D software renderer: no external scripts, libraries, CDNs, or network requests.
const sceneEl=document.getElementById('scene');
const status=document.getElementById('status');
const cv=document.createElement('canvas');
cv.setAttribute('aria-label','오프라인 6관절 3D 로봇팔');
sceneEl.prepend(cv);
const ctx=cv.getContext('2d');
const measuredReference=[935,500,413,482,736,396];
const angles=[0,0,0,0,0,0];
const limits=Array(6).fill(80);
const specs=[
 {name:'J1',label:'베이스 회전',axis:'y',len:.26},
 {name:'J2',label:'하부 굽힘',axis:'z',len:.51},
 {name:'J3',label:'하부 관절',axis:'z',len:.43},
 {name:'J4',label:'중간 관절',axis:'x',len:.41},
 {name:'J5',label:'상부 관절',axis:'z',len:.38},
 {name:'J6',label:'손목 회전',axis:'y',len:.27}
];
let selected=0,gripOpen=true,axisVisible=false;
let yaw=.68,pitch=.14,zoom=1;
let dragging=false,dragX=0,dragY=0;
const deg=Math.PI/180;
const v=(x,y,z)=>[x,y,z];
const add=(a,b)=>[a[0]+b[0],a[1]+b[1],a[2]+b[2]];
const scale=(a,t)=>a.map(x=>x*t);
const dot=(a,b)=>a.reduce((s,x,i)=>s+x*b[i],0);
const cross=(a,b)=>[a[1]*b[2]-a[2]*b[1],a[2]*b[0]-a[0]*b[2],a[0]*b[1]-a[1]*b[0]];
const norm=a=>{const d=Math.hypot(...a)||1;return scale(a,1/d)};
const rot=(a,axis,theta)=>{
 const k=norm(axis),c=Math.cos(theta),s=Math.sin(theta);
 return add(add(scale(a,c),scale(cross(k,a),s)),scale(k,dot(k,a)*(1-c)));
};
function frameFromPrevious(frame,axis,ang){
 const axisWorld=frame[axis==='x'?0:axis==='y'?1:2];
 return frame.map(e=>rot(e,axisWorld,ang));
}
const getAxis=(f,k)=>f[k==='x'?0:k==='y'?1:2];
function transform(pos,frame,local){return add(pos,add(add(scale(frame[0],local[0]),scale(frame[1],local[1])),scale(frame[2],local[2])))}
let shapes=[];
function seg(a,b,color,width=1){shapes.push({type:'seg',a,b,color,width,depth:(a[2]+b[2])/2})}
function sphere(a,r,color,outline='#13273a'){shapes.push({type:'ball',a,r,color,outline,depth:a[2]})}
function rect3(center,frame,w,h,color,outline='#516a7b'){
 const a=transform(center,frame,[-w/2,-h/2,0]);
 const b=transform(center,frame,[w/2,-h/2,0]);
 const c=transform(center,frame,[w/2,h/2,0]);
 const d=transform(center,frame,[-w/2,h/2,0]);
 shapes.push({type:'poly',points:[a,b,c,d],color,outline,depth:(a[2]+b[2]+c[2]+d[2])/4})
}
const xyz=[v(1,0,0),v(0,1,0),v(0,0,1)];
function buildArm(){
 shapes=[];
 const root=v(0,.16,0);
 const base=xyz;
 // ground and pedestal
 for(let i=-3;i<=3;i++){
   seg(v(i*.4,0,-1.5),v(i*.4,0,1.5),'#263d54',1);
   seg(v(-1.5,0,i*.4),v(1.5,0,i*.4),'#263d54',1);
 }
 sphere(v(0,.12,0),.32,'#566a77');
 seg(v(0,0,0),root,'#aec1ce',12);
 let point=add(root,v(0,.23,0));
 let frame=xyz;
 const centers=[];
 for(let i=0;i<6;i++){
   frame=frameFromPrevious(frame,specs[i].axis,angles[i]*deg);
   centers.push({p:point,f:frame});
   const next=transform(point,frame,[0,specs[i].len,0]);
   const chosen=i===selected;
   // paired frame rails and main motor body (depth through 3-D orientation)
   const left=transform(point,frame,[-.12,0,0]);
   const right=transform(point,frame,[.12,0,0]);
   seg(left,transform(next,frame,[-.12,0,0]),'#a1b9c7',8);
   seg(right,transform(next,frame,[.12,0,0]),'#a1b9c7',8);
   seg(point,next,'#344e62',17);
   sphere(point,.13,chosen?'#ffbb78':'#597f94');
   sphere(transform(point,frame,[0,0,.14]),.065,chosen?'#ffd692':'#c9dbe1');
   sphere(next,.055,'#a6c3d0');
   rect3(transform(point,frame,[0,.06,.16]),frame,.27,.16,chosen?'#eaa372':'#2d4659');
   if(axisVisible){
     for(const [k,color] of [[0,'#fa7f78'],[1,'#7ad4a0'],[2,'#89b5ff']]){
       seg(point,transform(point,frame,scale(xyz[k],.30)),color,3);
     }
   }
   point=next;
 }
 // open/closed visual gripper, intentionally not connected to a real motor
 const gap=gripOpen?.17:.065;
 seg(point,transform(point,frame,[0,.20,0]),'#b5cbd5',12);
 for(let sign of [-1,1]){
   const a=transform(point,frame,[sign*gap,.19,0]);
   const b=transform(point,frame,[sign*gap,.41,0]);
   seg(a,b,'#d1dce0',9);
   sphere(b,.042,'#f2ad7c');
 }
 // reference triad on ground
 seg(v(-1.05,.02,-1.05),v(-.65,.02,-1.05),'#e97c7b',3);
 seg(v(-1.05,.02,-1.05),v(-1.05,.42,-1.05),'#85cf9a',3);
 seg(v(-1.05,.02,-1.05),v(-1.05,.02,-.65),'#90baff',3);
 return centers;
}
function viewPoint(p){
 // world -> orbital camera coordinates (orthographic perspective)
 let q=rot(p,v(0,1,0),yaw);
 q=rot(q,v(1,0,0),pitch);
 return q;
}
function project(q,w,h){
 const scalePixel=Math.min(w/3.8,h/3.45)*zoom;
 const depth=5-q[2];const perspective=5/depth;
 return {x:w/2+q[0]*scalePixel*perspective,y:h*.89-q[1]*scalePixel*perspective,r:scalePixel*perspective,z:q[2]};
}
function render(){
 const w=cv.width,h=cv.height;
 ctx.clearRect(0,0,w,h);
 let g=ctx.createLinearGradient(0,0,0,h);
 g.addColorStop(0,'#172f47');g.addColorStop(1,'#07101e');ctx.fillStyle=g;ctx.fillRect(0,0,w,h);
 const centers=buildArm();
 shapes=shapes.map(s=>{
  if(s.type==='seg')return {...s,a:viewPoint(s.a),b:viewPoint(s.b)};
  if(s.type==='ball')return {...s,a:viewPoint(s.a)};
  return {...s,points:s.points.map(viewPoint)};
 });
 // render back to front, using world camera Z
 shapes.sort((a,b)=>{
 const z=s=>s.type==='seg'?(s.a[2]+s.b[2])/2:s.type==='ball'?s.a[2]:s.points.reduce((n,p)=>n+p[2],0)/4;
 return z(a)-z(b);
 });
 for(const s of shapes){
  if(s.type==='seg'){
   const a=project(s.a,w,h),b=project(s.b,w,h);
   ctx.lineWidth=s.width*window.devicePixelRatio*zoom;ctx.strokeStyle=s.color;ctx.lineCap='round';
   ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke();
  }else if(s.type==='ball'){
   const a=project(s.a,w,h);ctx.fillStyle=s.color;ctx.strokeStyle='#1a2e3b';ctx.lineWidth=2;
   ctx.beginPath();ctx.arc(a.x,a.y,Math.max(3,s.r*a.r),0,Math.PI*2);ctx.fill();ctx.stroke();
  }else{
   ctx.beginPath();s.points.forEach((p,i)=>{const a=project(p,w,h);i?ctx.lineTo(a.x,a.y):ctx.moveTo(a.x,a.y)});
   ctx.closePath();ctx.fillStyle=s.color;ctx.fill();ctx.strokeStyle=s.outline;ctx.stroke();
  }
 }
 ctx.font=`${12*devicePixelRatio}px monospace`;
 ctx.textAlign='left';
 centers.forEach((c,i)=>{
  const pp=project(viewPoint(c.p),w,h);
  ctx.fillStyle=i===selected?'#ffd29b':'#d0ecf3';
  ctx.fillText('ID '+String(i+1).padStart(3,'0'),pp.x+12*devicePixelRatio,pp.y-10*devicePixelRatio);
 });
}
function resize(){
 const rect=sceneEl.getBoundingClientRect();const dpr=Math.min(devicePixelRatio||1,2);
 cv.width=Math.max(1,Math.round(rect.width*dpr));cv.height=Math.max(1,Math.round(rect.height*dpr));
 render();
}
const controlBox=document.getElementById('controls');
function controlsMarkup(){return specs.map((s,i)=>`<div class="joint ${i===selected?'active':''}" id="jpanel${i}"><div class="jrow"><button type="button" class="jname" data-select="${i}">${s.name}<span> ID ${String(i+1).padStart(3,'0')} · ${s.label}</span></button><span class="jvalue" id="val${i}">${angles[i].toFixed(0)}°</span></div><div class="rawrow">실측 Present Position: <b>${measuredReference[i]}</b>　|　기준 자세 대비: <b id="delta${i}">0°</b></div><input aria-label="${s.name} 관절 목표각" type="range" id="joint${i}" min="-${limits[i]}" max="${limits[i]}" step="1" value="${angles[i]}"><div class="scale"><span>−${limits[i]}°</span><span>0°</span><span>+${limits[i]}°</span></div></div>`).join('');}
controlBox.innerHTML=controlsMarkup();
function apply(){angles.forEach((d,i)=>{
 document.getElementById(`val${i}`).textContent=`${d.toFixed(0)}°`;
 document.getElementById(`delta${i}`).textContent=`${d>=0?'+':''}${d.toFixed(0)}°`;
 document.getElementById(`joint${i}`).value=String(d);
 document.getElementById(`jpanel${i}`).classList.toggle('active',selected===i);
 });
 status.textContent=`선택: J${selected+1} / ID ${String(selected+1).padStart(3,'0')} · 상대각 ${angles[selected]}° · 실물 모터 미연결`;
 render();
}
for(let i=0;i<6;i++)document.getElementById(`joint${i}`).addEventListener('input',e=>{angles[i]=Number(e.target.value);selected=i;apply()});
controlBox.addEventListener('click',e=>{const b=e.target.closest('[data-select]');if(b){selected=Number(b.dataset.select);apply()}});
document.getElementById('home').onclick=()=>{angles.fill(0);apply()};
document.getElementById('pose').onclick=()=>{[0,25,-30,20,20,-15].forEach((n,i)=>angles[i]=n);apply()};
document.getElementById('grip').onclick=()=>{gripOpen=!gripOpen;status.textContent=`가상 집게 ${gripOpen?'열림':'닫힘'} · 실물 구동 없음`;render()};
document.getElementById('axes').onclick=()=>{axisVisible=!axisVisible;status.textContent=`가상 회전축 표시 ${axisVisible?'ON':'OFF'}`;render()};
document.getElementById('resetCam').onclick=()=>{yaw=.68;pitch=.14;zoom=1;render()};
document.getElementById('copy').onclick=()=>{
 const data={mode:'SIMULATION_ONLY',measured_at:'2026-11-23',motor_ids:[1,2,3,4,5,6],measured_present_position_raw:measuredReference,virtual_relative_angles_deg:[...angles],gripper_open_virtual:gripOpen,calibrated:false,hardware_command:false};
 const blob=new Blob([JSON.stringify(data,null,2)],{type:'application/json'});
 const a=document.createElement('a');const url=URL.createObjectURL(blob);a.href=url;a.download='mecha_lab_angles.json';a.click();setTimeout(()=>URL.revokeObjectURL(url),1000);
 status.textContent='JSON 파일로 저장했습니다. 실물 제어 명령은 포함되지 않습니다.';
};
cv.addEventListener('pointerdown',e=>{dragging=true;dragX=e.clientX;dragY=e.clientY;cv.setPointerCapture(e.pointerId)});
cv.addEventListener('pointermove',e=>{if(!dragging)return;yaw+=(e.clientX-dragX)*.008;pitch=Math.max(-.75,Math.min(.65,pitch+(e.clientY-dragY)*.006));dragX=e.clientX;dragY=e.clientY;render()});
for(const ev of ['pointerup','pointercancel','lostpointercapture'])cv.addEventListener(ev,()=>dragging=false);
cv.addEventListener('wheel',e=>{e.preventDefault();zoom=Math.max(.5,Math.min(1.65,zoom*(e.deltaY>0?.92:1.08)));render()},{passive:false});
window.addEventListener('resize',resize);
if('ResizeObserver' in window)new ResizeObserver(resize).observe(sceneEl);
resize();apply();
</script>
</body>
</html>

'''

components.html(GAME_HTML, height=970, scrolling=False)
