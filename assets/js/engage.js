/* Gridence engagement layer. Runs after site.js has rendered the page. */
(()=>{
const $=(s,r=document)=>r.querySelector(s);
const P=/\/(services|insights)\//.test(location.pathname)?'../':'';
const KEY='gridence.check.v1';
const ls={get(){try{return JSON.parse(localStorage.getItem(KEY))}catch(e){return null}},set(v){try{localStorage.setItem(KEY,JSON.stringify(v))}catch(e){}},del(){try{localStorage.removeItem(KEY)}catch(e){}}};
const ss={get(k){try{return sessionStorage.getItem(k)}catch(e){return null}},set(k,v){try{sessionStorage.setItem(k,v)}catch(e){}}};
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const openWA=m=>{if(typeof waUrl==='function'){const u=waUrl(m);if(u)window.open(u,'_blank','noopener,noreferrer')}else{const n=(window.GRIDENCE_WHATSAPP_NUMBER||'').replace(/\D/g,'');if(n)window.open('https://wa.me/'+n+'?text='+encodeURIComponent(m),'_blank','noopener,noreferrer')}};

const Q=[
 {k:'fac',q:'What kind of facility is this for?',o:[['dc','Data centre or IT park'],['com','Commercial building or retail'],['hosp','Hotel, hospital or restaurant chain'],['ind','Industrial plant'],['dev','New development or project']]},
 {k:'need',q:'What matters most right now?',o:[['cost','Bringing electricity costs under control'],['safety','Electrical safety and audits'],['infra','A new or expanded power setup'],['comp','Approvals, utility coordination and closure'],['green','Solar, open access or EV charging']]},
 {k:'bill',q:'Roughly what is your monthly electricity bill?',o:[['s','Under ₹2 lakh'],['m','₹2 to 10 lakh'],['l','₹10 to 50 lakh'],['xl','Above ₹50 lakh'],['na','Not sure, or not applicable yet']]}
];
const label=(k,v)=>(Q.find(x=>x.k===k).o.find(o=>o[0]===v)||[,''])[1];
const R={
 cost:{svc:'electricity-bill-optimisation',name:'Electricity Bill Optimisation',h:'Start with your bill, line by line',s:['Collect the last 12 months of bills and meter data','Compare billed demand with sanctioned load and contract demand','Check the tariff category and any power factor adjustments']},
 safety:{svc:'energy-safety-audits',name:'Energy & Electrical Safety Audits',h:'Start by defining what an audit should cover',s:['Gather drawings, maintenance records and earlier audit findings','Decide which installations and risks are in scope','List open observations and who owns each one']},
 infra:{svc:'power-infrastructure',name:'Power Infrastructure Design & Supply',h:'Start with load and timelines',s:['Estimate connected load and expected growth','Confirm supply availability and utility timelines','Map design, sourcing and installation milestones']},
 comp:{svc:'regulatory-compliance',name:'Regulatory Compliance & Closure',h:'Start by mapping what applies to you',s:['List the approvals and statutory requirements that apply','Keep supporting documents together in one place','Track each submission, inspection and closure step']},
 green:{svc:'renewable-energy',name:'Solar, Open Access & EV Solutions',h:'Start with your consumption profile',s:['Profile consumption across the day and month','Check roof area and open access eligibility','Allow for future EV charging load']}
};
const FN={dc:'For critical digital infrastructure, continuity and load planning usually come first.',com:'For commercial properties, tenant load and utility coordination tend to shape the plan.',hosp:'For round-the-clock facilities, reliability and safety carry extra weight.',ind:'For high-demand operations, demand and tariff details matter most.',dev:'For new projects, early utility planning helps reduce uncertainty later.'};
const BN={s:'Even at this size, a short bill review shows where to look.',m:'At this scale, demand and tariff details are worth a structured review.',l:'At this scale, demand and tariff details are worth a structured review.',xl:'At this scale, a detailed look at demand and tariff structure is worthwhile.',na:'We can work from your project requirements instead of a bill.'};

/* ---------- Energy check modal ---------- */
let ov,dlg,step=0,ans={},last=null;
function build(){
 ov=document.createElement('div');ov.className='hc-overlay';
 ov.innerHTML='<div class="hc-dialog" role="dialog" aria-modal="true" aria-labelledby="hcTitle" tabindex="-1"><button class="hc-close" type="button" aria-label="Close">×</button><div id="hcBody"></div></div>';
 document.body.appendChild(ov);dlg=$('.hc-dialog',ov);
 ov.addEventListener('click',e=>{if(e.target===ov)close()});
 $('.hc-close',ov).addEventListener('click',close);
 document.addEventListener('keydown',e=>{
  if(!ov.classList.contains('open'))return;
  if(e.key==='Escape')close();
  if(e.key==='Tab'){const f=[...dlg.querySelectorAll('button,a[href]')].filter(x=>x.offsetParent);if(!f.length)return;const a=f[0],z=f[f.length-1];if(e.shiftKey&&document.activeElement===a){e.preventDefault();z.focus()}else if(!e.shiftKey&&document.activeElement===z){e.preventDefault();a.focus()}}
 });
}
function meter(n){return '<div class="hc-meter" aria-hidden="true">'+[0,1,2,3].map(i=>'<i class="'+(i<=n?'on':'')+'"></i>').join('')+'</div>'}
function render(){
 const body=$('#hcBody');
 if(step<Q.length){
  const q=Q[step];
  body.innerHTML=meter(step)+'<p class="hc-count">Question '+(step+1)+' of '+Q.length+'</p><h3 id="hcTitle">'+q.q+'</h3><div class="hc-opts">'+q.o.map(o=>'<button class="hc-opt" type="button" data-v="'+o[0]+'">'+o[1]+'</button>').join('')+'</div>'+(step?'<button class="hc-back" type="button">← Back</button>':'');
  body.querySelectorAll('.hc-opt').forEach(b=>b.addEventListener('click',()=>{ans[q.k]=b.dataset.v;step++;if(step===Q.length)ls.set({...ans,ts:Date.now()});render()}));
  $('.hc-back',body)?.addEventListener('click',()=>{step--;render()});
 }else{
  const r=R[ans.need],msg=waMsg(ans);
  body.innerHTML=meter(3)+'<p class="hc-count">Your starting point</p><h3 id="hcTitle">'+r.h+'</h3><p class="hc-note">'+FN[ans.fac]+' '+BN[ans.bill]+'</p><ol class="hc-steps">'+r.s.map(x=>'<li>'+x+'</li>').join('')+'</ol><div class="hc-actions"><button class="btn btn-lime hc-send" type="button">Send my answers on WhatsApp ↗</button><a class="under-link" href="'+P+'services/'+r.svc+'.html">About '+esc(r.name)+'</a></div><button class="hc-back hc-redo" type="button">Start over</button><small class="hc-fine">A guide to what to review first. It is not a savings estimate or a technical assessment.</small>';
  $('.hc-send',body).addEventListener('click',()=>openWA(msg));
  $('.hc-redo',body).addEventListener('click',()=>{ans={};step=0;ls.del();render()});
 }
 (body.querySelector('.hc-opt')||body.querySelector('.hc-send')||dlg).focus();
}
function waMsg(a){return ['Hello Gridence, I completed the energy check on your website.','Facility: '+label('fac',a.fac),'Priority: '+label('need',a.need),'Monthly bill: '+label('bill',a.bill),'I would like to discuss next steps.'].join('\n')}
function open(){
 if(!ov)build();
 last=document.activeElement;
 const saved=ls.get();
 if(saved&&saved.fac&&saved.need&&saved.bill&&!ans.fac){ans={fac:saved.fac,need:saved.need,bill:saved.bill};step=Q.length}else if(!ans.fac){step=0}
 render();ov.classList.add('open');document.body.classList.add('hc-lock');ss.set('hcSeen','1');hideNudge();
}
function close(){ov.classList.remove('open');document.body.classList.remove('hc-lock');last&&last.focus&&last.focus()}
document.addEventListener('click',e=>{const t=e.target.closest('[data-hc]');if(t){e.preventDefault();open()}});

/* ---------- Nav link ---------- */
const nav=$('.nav');
if(nav)nav.insertAdjacentHTML('beforeend','<a href="#" data-hc class="nav-check">Energy check</a>');

/* ---------- Home: check band, returning banner, FAQ ---------- */
const home=document.body.dataset.page==='home';
if(home){
 const intro=$('.section.intro');
 if(intro)intro.insertAdjacentHTML('beforebegin','<section class="hc-band" aria-label="Energy check"><div><h2>Where should your energy attention go first?</h2><p>Answer three questions in about two minutes. You get a starting checklist for your facility and a ready-made message for our team.</p></div><button class="btn btn-dark" type="button" data-hc>Take the energy check</button></section>');
 const s=ls.get();
 if(s&&s.need&&R[s.need]&&!ss.get('hcBanner')){
  const hdr=$('.header');
  hdr&&hdr.insertAdjacentHTML('afterend','<div class="hc-banner" role="status"><span>Welcome back. Your last check pointed to <b>'+esc(R[s.need].name)+'</b>.</span><span class="hc-banner-actions"><button type="button" data-hc>See my checklist</button><button type="button" class="hc-banner-x" aria-label="Dismiss">×</button></span></div>');
  $('.hc-banner-x')?.addEventListener('click',e=>{ss.set('hcBanner','1');e.target.closest('.hc-banner').remove()});
 }
}
if(home||document.body.dataset.page==='services'){
 const cta=$('.bottom-cta');
 const F=[['How does an engagement usually start?','With a short conversation about your facility, bills or project. We then agree the scope and the information needed before recommending anything.'],['Do I need documents ready before I get in touch?','No. Start with a message, and we will tell you which documents are worth gathering.'],['Do you promise savings?','No. We identify what is worth investigating. Outcomes depend on the applicable tariff orders, your operating pattern and the utility process.'],['Where do you work?','Consulting and project support are available across India.'],['Can you help with a project already under way?','Yes. We can support specific needs such as utility coordination, documentation or inspections.']];
 cta&&cta.insertAdjacentHTML('beforebegin','<section class="section faq"><div class="section-head"><div><h2>Questions we hear first</h2></div><p>Short answers before you reach out. Anything else, ask us directly.</p></div><div class="faq-list">'+F.map(f=>'<details><summary>'+f[0]+'</summary><p>'+f[1]+'</p></details>').join('')+'</div></section>');
}

/* ---------- Articles: progress bar + next read ---------- */
const art=$('.article-content');
if(art){
 document.body.insertAdjacentHTML('afterbegin','<div class="read-progress" aria-hidden="true"><span></span></div>');
 const bar=$('.read-progress span');
 const upd=()=>{const h=document.documentElement,max=h.scrollHeight-h.clientHeight;bar.style.width=(max>0?Math.min(100,h.scrollTop/max*100):0)+'%'};
 addEventListener('scroll',upd,{passive:true});upd();
 if(typeof posts!=='undefined'){
  const n=posts.find(p=>!location.pathname.includes(p.slug));
  if(n)art.closest('section').insertAdjacentHTML('afterend','<section class="next-read"><small>Read next</small><a href="'+n.slug+'.html"><h3>'+esc(n.title)+'</h3><p>'+esc(n.desc)+'</p><b>Read insight ↗</b></a><button class="btn btn-dark" type="button" data-hc>Take the energy check</button></section>');
 }
}

/* ---------- Home: "Start with your challenge" ---------- */
const ns=$('.needs-section');
if(ns){
 const IC={
  cost:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M6 3h12v18l-3-2-3 2-3-2-3 2z"/><path d="M9 8h6M9 12h6"/></svg>',
  safety:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 3l8 3v6c0 4.5-3.2 7.8-8 9-4.8-1.2-8-4.5-8-9V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/></svg>',
  infrastructure:'<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M13 2L5 13h6l-1 9 8-11h-6z"/></svg>',
  renewable:'<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v3M12 19v3M2 12h3M19 12h3M4.9 4.9L7 7M17 17l2.1 2.1M4.9 19.1L7 17M17 7l2.1-2.1"/></svg>'
 };
 const N=[
  {id:'cost',t:'High electricity costs',s:'Bills feel high or hard to read',h:'Make sense of your electricity bill.',c:'Review tariff components, demand patterns and billing parameters to understand where a closer look may be worthwhile.',l:['Billing components and tariff applicability','Sanctioned load, contract demand and demand patterns','Mismatches worth raising with the utility'],svc:'electricity-bill-optimisation',b:'Explore bill optimisation'},
  {id:'safety',t:'Electrical safety & audits',s:'Check risks in a running facility',h:'Put electrical safety in focus.',c:'Understand the condition of your electrical systems, identify observations and prioritise practical corrective actions.',l:['Energy consumption and operating patterns','Electrical systems and safety practices','Prioritised corrective actions'],svc:'energy-safety-audits',b:'Explore safety audits'},
  {id:'infrastructure',t:'New facility or power setup',s:'Plan load, supply and installation',h:'Plan power around your project.',c:'Bring load requirements, infrastructure planning, utility coordination and execution into one clear scope.',l:['Load requirements and project constraints','Distribution design and supply sourcing','Installation and execution planning'],svc:'power-infrastructure',b:'Explore power infrastructure'},
  {id:'renewable',t:'Renewable energy options',s:'Solar, open access and EV charging',h:'Evaluate cleaner energy pathways.',c:'Explore rooftop solar, open access and EV charging options against your facility profile and business priorities.',l:['Energy profile and project feasibility','Rooftop solar and open access models','EV charging requirements'],svc:'renewable-energy',b:'Explore renewable energy'}
 ];
 ns.innerHTML='<div class="nx-head"><div class="section-label">02 / START WITH YOUR CHALLENGE</div><h2>What does your business need help with?</h2><p>Pick the one closest to yours and we will show you where we would start.</p></div><div class="nx"><div class="nx-tabs" role="tablist" aria-label="Business challenge">'+N.map(n=>'<button class="nx-tab" type="button" role="tab" id="nxt-'+n.id+'" aria-controls="nxPanel" aria-selected="false" tabindex="-1" data-id="'+n.id+'"><span class="nx-ic">'+IC[n.id]+'</span><span class="nx-tx"><b>'+n.t+'</b><small>'+n.s+'</small></span></button>').join('')+'</div><div class="nx-panel" id="nxPanel" role="tabpanel" aria-live="polite"></div></div>';
 const tabs=[...ns.querySelectorAll('.nx-tab')],panel=$('#nxPanel');
 const pick=(id,focus)=>{
  const n=N.find(x=>x.id===id);if(!n)return;
  tabs.forEach(t=>{const on=t.dataset.id===id;t.setAttribute('aria-selected',on);t.tabIndex=on?0:-1;if(on&&focus)t.focus()});
  panel.setAttribute('aria-labelledby','nxt-'+id);
  panel.innerHTML='<div class="nx-body"><h3>'+n.h+'</h3><p>'+n.c+'</p><ul>'+n.l.map(x=>'<li>'+x+'</li>').join('')+'</ul></div><div class="nx-actions"><a class="btn btn-lime" href="'+P+'services/'+n.svc+'.html">'+n.b+' ↗</a><button class="nx-ask" type="button">Ask us about this</button></div>';
  $('.nx-ask',panel).addEventListener('click',()=>openWA('Hello Gridence, I would like to discuss: '+n.t.toLowerCase()+'.'));
  panel.classList.remove('nx-swap');void panel.offsetWidth;panel.classList.add('nx-swap');
 };
 tabs.forEach((t,i)=>{
  t.addEventListener('click',()=>pick(t.dataset.id));
  t.addEventListener('keydown',e=>{const k=e.key;if(!/^Arrow(Up|Down|Left|Right)$/.test(k))return;e.preventDefault();const d=/Down|Right/.test(k)?1:-1;pick(tabs[(i+d+tabs.length)%tabs.length].dataset.id,true)});
 });
 const sv=ls.get(),pre={cost:'cost',safety:'safety',infra:'infrastructure',green:'renewable'}[sv&&sv.need];
 pick(pre||'cost');
}

/* ---------- Mobile sticky bar ---------- */
document.body.insertAdjacentHTML('beforeend','<div class="sticky-bar"><button type="button" data-hc>Energy check</button><button type="button" class="sb-wa">WhatsApp us</button></div>');
$('.sb-wa').addEventListener('click',()=>openWA('Hello Gridence, I have an enquiry about your energy services.'));
const sb=$('.sticky-bar');
const onScroll=()=>sb.classList.toggle('show',scrollY>480);
addEventListener('scroll',onScroll,{passive:true});onScroll();

/* ---------- One-time, non-blocking nudge (desktop) ---------- */
let nudge=null;
function hideNudge(){nudge&&nudge.classList.remove('show')}
function showNudge(){
 if(ss.get('hcSeen')||ss.get('hcNudged')||ls.get()||/contact/.test(location.pathname)||innerWidth<900)return;
 ss.set('hcNudged','1');
 nudge=document.createElement('div');nudge.className='hc-nudge';
 nudge.innerHTML='<button class="hc-nudge-x" type="button" aria-label="Dismiss">×</button><b>Not sure where to start?</b><p>Take the two-minute energy check for a tailored checklist.</p><button class="btn btn-lime" type="button" data-hc>Start the check</button>';
 document.body.appendChild(nudge);requestAnimationFrame(()=>nudge.classList.add('show'));
 $('.hc-nudge-x',nudge).addEventListener('click',hideNudge);
}
setTimeout(showNudge,50000);
let armed=false;setTimeout(()=>armed=true,8000);
document.addEventListener('mouseout',e=>{if(armed&&e.clientY<=0&&!e.relatedTarget)showNudge()});
})();
