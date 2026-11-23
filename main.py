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
