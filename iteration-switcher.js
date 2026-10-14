/* Private preview: floating switcher between design iterations 1–10.
   Iteration 1 lives in /iteration-1/; 2–10 share the root pages and are chosen with ?iter=N. */
(function(){
 var NAMES={1:'Original',2:'Ledger',3:'Skyline Noir',4:'Proof First',5:'Editorial',6:'Conversion Desk',7:'Blueprint',8:'Desert Luxe',9:'Bento',10:'Kinetic'};
 var me=document.currentScript;
 var cur=+(me&&me.getAttribute('data-iter'))||(function(){try{var q=+new URLSearchParams(location.search).get('iter');if(q>=2&&q<=10)return q;var v=+localStorage.getItem('qd-iter');return v>=2&&v<=10?v:2}catch(e){return 2}})();
 var page=(location.pathname.split('/').pop()||'index.html');
 if(!/\.html$/.test(page))page='index.html';
 var href=function(n){return n===1?'/iteration-1/'+page:'/'+page+'?iter='+n+location.hash};
 var css=document.createElement('style');
 css.textContent='.v3-review{display:none!important}.qd-iter{position:fixed;left:14px;bottom:14px;z-index:9999;font:600 13px/1.2 system-ui,-apple-system,sans-serif}'+
 '.qd-iter>button{display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:999px;border:1px solid rgba(255,255,255,.25);background:#111827;color:#fff;cursor:pointer;box-shadow:0 10px 30px -10px rgba(0,0,0,.5)}'+
 '.qd-iter>button b{background:#e8cd8e;color:#241a08;border-radius:999px;padding:2px 8px}'+
 '.qd-iter ol{position:absolute;bottom:48px;left:0;margin:0;padding:6px;list-style:none;min-width:230px;background:#111827;border-radius:14px;box-shadow:0 20px 50px -15px rgba(0,0,0,.6)}'+
 '.qd-iter ol[hidden]{display:none}.qd-iter li a{display:flex;gap:10px;padding:9px 10px;border-radius:9px;color:#e5e7eb;text-decoration:none}'+
 '.qd-iter li a:hover,.qd-iter li a:focus-visible{background:#1f2937;outline:none}.qd-iter li a[aria-current]{background:#e8cd8e;color:#241a08}'+
 '.qd-iter li a span{opacity:.6;min-width:20px}.qd-iter .qd-all{border-top:1px solid #374151;margin-top:4px;padding-top:4px}'+
 '@media(max-width:760px){.qd-iter{bottom:86px}}';
 document.head.appendChild(css);
 var box=document.createElement('nav');box.className='qd-iter';box.setAttribute('aria-label','Design iterations');
 var btn=document.createElement('button');btn.type='button';btn.setAttribute('aria-expanded','false');
 btn.innerHTML='<b>'+cur+'/10</b>Iteration '+cur+' · '+NAMES[cur]+' ▴';
 var list=document.createElement('ol');list.hidden=true;
 for(var n=1;n<=10;n++){var li=document.createElement('li'),a=document.createElement('a');a.href=href(n);a.innerHTML='<span>'+n+'</span>'+NAMES[n];if(n===cur)a.setAttribute('aria-current','page');li.appendChild(a);list.appendChild(li)}
 var all=document.createElement('li');all.className='qd-all';all.innerHTML='<a href="/iterations.html"><span>☰</span>Compare all iterations</a>';list.appendChild(all);
 btn.onclick=function(){var o=list.hidden;list.hidden=!o;btn.setAttribute('aria-expanded',String(o))};
 document.addEventListener('keydown',function(e){if(e.key==='Escape'&&!list.hidden){list.hidden=true;btn.setAttribute('aria-expanded','false');btn.focus()}});
 document.addEventListener('click',function(e){if(!box.contains(e.target)&&!list.hidden){list.hidden=true;btn.setAttribute('aria-expanded','false')}});
 box.appendChild(list);box.appendChild(btn);
 (document.readyState==='loading')?document.addEventListener('DOMContentLoaded',function(){document.body.appendChild(box)}):document.body.appendChild(box);
})();
