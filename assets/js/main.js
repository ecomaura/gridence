(function(){
const $=(s,c=document)=>c.querySelector(s),$$=(s,c=document)=>[...c.querySelectorAll(s)];
const nav=$('nav.main'),bg=$('.burger');
bg&&bg.addEventListener('click',()=>{const o=nav.classList.toggle('open');bg.setAttribute('aria-expanded',o)});
$$('.dd>button').forEach(b=>b.addEventListener('click',()=>{const d=b.parentElement,o=d.classList.toggle('open');b.setAttribute('aria-expanded',o)}));
document.addEventListener('keydown',e=>{if(e.key==='Escape'){nav.classList.remove('open');$$('.dd.open').forEach(d=>d.classList.remove('open'))}});
const top=$('#top');addEventListener('scroll',()=>top.classList.toggle('show',scrollY>700),{passive:true});
top.addEventListener('click',()=>scrollTo({top:0}));
const C=window.GRIDENCE||{};
const wa=$('#wa');if(wa&&C.whatsapp){wa.href='https://wa.me/'+C.whatsapp;wa.hidden=false}
$$('form.lead').forEach(f=>{
 const st=$('.status',f),btn=$('button[type=submit]',f);
 const rules={name:v=>v.trim().length>1||'Enter your full name.',company:v=>v.trim().length>1||'Enter your company name.',
  email:v=>/^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/.test(v)||'Enter a valid work email address.',
  phone:v=>(/^\+?[0-9\s\-()]{8,18}$/.test(v.trim())&&v.replace(/\D/g,'').length>=8)||'Enter a valid phone number (8 to 15 digits).',
  industry:v=>!!v||'Select your industry.',service:v=>!!v||'Select the service you need.',
  message:v=>v.trim().length>=10||'Describe your requirement in a few words.'};
 const check=el=>{const r=rules[el.name];if(!r)return true;const m=r(el.value),e=el.parentElement.querySelector('.err');
  el.setAttribute('aria-invalid',m!==true);e.textContent=m===true?'':m;return m===true};
 $$('input,select,textarea',f).forEach(el=>el.addEventListener('blur',()=>check(el)));
 const mailto=()=>{const d=new FormData(f);const b=[...d.entries()].filter(([k])=>k!=='_gotcha').map(([k,v])=>k+': '+v).join('\n');
  return 'mailto:'+C.email+'?subject='+encodeURIComponent('GRIDENCE enquiry')+'&body='+encodeURIComponent(b)};
 const ml=$('.mailfb',f);ml&&ml.addEventListener('click',()=>{ml.href=mailto()});
 f.addEventListener('submit',async e=>{e.preventDefault();st.className='status';st.textContent='';
  const ok=$$('input,select,textarea',f).map(check).every(Boolean);
  if(!ok){const bad=$('[aria-invalid=true]',f);bad&&bad.focus();return}
  if(!C.formspree||C.formspree.includes('YOUR_FORM_ID')){st.className='status bad';
   st.innerHTML='The online form is not connected yet. Please <a href="'+mailto()+'">send this enquiry by email</a> instead.';return}
  btn.disabled=true;const t=btn.textContent;btn.textContent='Sending…';
  try{const r=await fetch(C.formspree,{method:'POST',body:new FormData(f),headers:{Accept:'application/json'}});
   if(!r.ok)throw new Error();f.reset();st.className='status ok';st.textContent='Thank you. Your enquiry has been received and our team will respond by email.'}
  catch(_){st.className='status bad';st.innerHTML='We could not send your enquiry. Please try again or <a href="'+mailto()+'">email us directly</a>.'}
  btn.disabled=false;btn.textContent=t});
});
})();
