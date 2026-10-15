/* Sticky-note client testimonials, shared by every iteration (1 included).
   Data: /testimonials.json. Inserted at the end of "03 / Who we work with" (#projects). */
(function(){
 var css='.qd-notes{margin:56px auto 0;max-width:1320px}'+
 '.qd-notes-head{display:flex;align-items:flex-end;justify-content:space-between;gap:20px;margin-bottom:34px}'+
 '.qd-notes-head h3{margin:0;font-size:clamp(24px,2.4vw,34px);line-height:1.1}'+
 '.qd-notes-head p{margin:0;max-width:42ch;font-size:15px;opacity:.8}'+
 '.qd-notes-grid{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:38px 30px;padding:18px 6px 6px}'+
 '.qd-note{position:relative;margin:0;padding:46px 30px 28px;border-radius:22px;background:#ffe600;color:#111;box-shadow:0 18px 36px -18px rgba(0,0,0,.45);transform:rotate(var(--tilt,-1.2deg));transition:transform .25s ease}'+
 '.qd-note:nth-child(2){--tilt:1deg}.qd-note:nth-child(3){--tilt:-.6deg}'+
 '.qd-note:hover{transform:rotate(0) translateY(-4px)}'+
 '.qd-note-q{position:absolute;left:-10px;top:-34px;width:72px;height:56px;color:#d01f2e}'+
 '.qd-note-pin{position:absolute;right:20px;top:16px;width:26px;height:26px;color:#111}'+
 '.qd-note blockquote{margin:0;font-size:17px;line-height:1.55;font-weight:500;color:#111}'+
 '.qd-note blockquote p{margin:0;color:#111!important}'+
 '.qd-note figcaption{margin-top:20px;color:#111}'+
 '.qd-note figcaption strong{display:block;font-size:17px;font-weight:800}'+
 '.qd-note figcaption span{display:block;font-size:13.5px;opacity:.75;margin-top:2px}'+
 '.qd-note-flag{position:absolute;left:30px;bottom:-13px;padding:4px 10px;border-radius:99px;background:#111;color:#ffe600;font:700 11px/1.2 system-ui,sans-serif;letter-spacing:.02em}'+
 '@media (max-width:900px){.qd-notes-grid{grid-template-columns:1fr;gap:46px}.qd-notes-head{flex-direction:column;align-items:flex-start}}'+
 '@media (prefers-reduced-motion:reduce){.qd-note{transition:none}}';
 var Q='<svg class="qd-note-q" viewBox="0 0 72 56" aria-hidden="true"><path fill="currentColor" d="M0 56V33C0 15 9 4 27 0l3 7C21 10 16 16 15 25h14v31H0Zm42 0V33C42 15 51 4 69 0l3 7c-9 3-14 9-15 18h14v31H42Z"/></svg>';
 var PIN='<svg class="qd-note-pin" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M15.6 2.3a1 1 0 0 1 1.4 0l4.7 4.7a1 1 0 0 1-.5 1.7l-2.1.4-3.7 3.7.6 4.2a1 1 0 0 1-.3.9l-1.4 1.4a1 1 0 0 1-1.4 0l-3.5-3.5-5.6 5.6a1 1 0 1 1-1.4-1.4l5.6-5.6-3.5-3.5a1 1 0 0 1 0-1.4l1.4-1.4a1 1 0 0 1 .9-.3l4.2.6 3.7-3.7.4-2.1a1 1 0 0 1 .3-.6Z"/></svg>';
 var esc=function(t){var d=document.createElement('div');d.textContent=t||'';return d.innerHTML};
 function build(items){
  var wrap=document.createElement('div');wrap.className='qd-notes';wrap.setAttribute('data-qd-notes','');
  var anyReal=items.some(function(i){return i.approved});
  wrap.innerHTML='<div class="qd-notes-head"><h3>In our clients’ words.</h3><p>'+(anyReal?'Developers and channel partners on working with QDnCo.':'Preview layout. Placeholder cards until real client quotes are approved.')+'</p></div>'+
   '<div class="qd-notes-grid">'+items.map(function(i){return '<figure class="qd-note">'+Q+PIN+'<blockquote><p>'+esc(i.quote)+'</p></blockquote><figcaption><strong>'+esc(i.name)+'</strong><span>'+esc(i.role)+'</span></figcaption>'+(i.approved?'':'<span class="qd-note-flag">Placeholder — not a client quote</span>')+'</figure>'}).join('')+'</div>';
  return wrap;
 }
 var data=null;
 function place(){
  var host=document.getElementById('projects');
  if(!host||!data||host.querySelector('[data-qd-notes]'))return;
  host.appendChild(build(data));
 }
 fetch('/testimonials.json',{cache:'no-cache'}).then(function(r){return r.json()}).then(function(j){
  data=(j.items||[]).filter(function(i){return i&&i.quote});if(!data.length)return;
  var st=document.createElement('style');st.textContent=css;document.head.appendChild(st);
  place();new MutationObserver(place).observe(document.body,{childList:true,subtree:true});
 }).catch(function(){});
})();
