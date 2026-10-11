"""Apply shared navigation to preserved website pages; never modifies production."""
from pathlib import Path
from bs4 import BeautifulSoup
import json, re, shutil, sys
P=Path(__file__).resolve().parent; R=P/'candidate'
manifest=json.loads((P/'route-manifest.json').read_text()); redesigned={x['file'] for x in manifest}
css='''
.qd-shared-header,.qd-shared-header *{box-sizing:border-box}
.qd-shared-header{position:fixed;z-index:1000;top:20px;left:4vw;right:4vw;max-width:1488px;margin:auto;padding:12px 22px;display:flex;align-items:center;justify-content:space-between;gap:18px;border:1px solid #a18b623d;border-radius:24px;background:#fff8e9f5;color:#252a24;backdrop-filter:blur(20px);font:13px Inter,Arial,sans-serif;box-shadow:0 4px 18px #00000008}
.qd-shared-header a{color:inherit;text-decoration:none}
.qd-shared-header .v3-logo{display:block;flex-shrink:0;width:140px;padding:6px 10px;border:1px solid #a48b5f99;border-radius:17px;background:#fff}
.qd-shared-header .v3-logo img{display:block;width:100%;height:36px;object-fit:contain;margin:0;filter:brightness(0)}
.qd-shared-header .v3-logo small{display:block;color:#171a25;font-size:7px;letter-spacing:.08em;text-align:center;margin-top:2px}
.qd-shared-header nav{display:flex;align-items:center;gap:4px;padding:5px;border:1px solid #a18b624d;border-radius:999px;background:#bda16c08;margin:0}
.qd-shared-header nav>a,.qd-shared-header summary{display:block;padding:10px 17px;border:1px solid transparent;border-radius:999px;white-space:nowrap;cursor:pointer;font-size:13px;font-weight:500;list-style:none}
.qd-shared-header summary::-webkit-details-marker{display:none}.qd-shared-header summary:after{content:' +'}
.qd-shared-header nav .v3-nav-current{border-color:#ad8b48aa;background:linear-gradient(130deg,#d7b66b38,#b99a5812);animation:qd-header-arrive .55s ease-out}
.qd-shared-header a:hover,.qd-shared-header summary:hover{background-color:#b99a5820}
.qd-shared-header a:focus-visible,.qd-shared-header button:focus-visible,.qd-shared-header summary:focus-visible{outline:2px solid #ac8745;outline-offset:3px}
.qd-shared-header .nav-right{display:flex;align-items:center;gap:12px}
.qd-shared-header .v3-button{display:inline-flex;align-items:center;gap:25px;padding:16px 24px;border:1px solid #c6a86688;border-radius:999px;background:linear-gradient(110deg,#dcb660,#f3dda1,#dcb660);font-size:12px;font-weight:650;color:#282416;white-space:nowrap}
.qd-shared-header .v3-market-buttons{display:flex;gap:3px;padding:4px;border:1px solid #a18b624d;border-radius:999px}
.qd-shared-header .v3-market-buttons a{padding:9px 12px;border-radius:999px;font-size:11px}.qd-shared-header .v3-market-buttons .active{background:#7c6030;color:#fff}
.qd-shared-header .v3-resource-menu{position:relative;border:0;padding:0;margin:0;background:none}
.qd-shared-header .v3-resource-menu>div{position:absolute;top:calc(100% + 10px);left:0;width:230px;padding:10px;border:1px solid #ac915855;border-radius:16px;background:#fff8eb;box-shadow:0 12px 32px #0002}
.qd-shared-header .v3-resource-menu>div a{display:block;padding:11px;border-radius:9px;font-size:12px}
.qd-shared-header .qd-theme{padding:8px 12px;border:1px solid #a18b624d;border-radius:999px;background:transparent;color:inherit;cursor:pointer;font-size:16px}
.qd-shared-header[data-theme=dark]{background:#111720f5;color:#f3eee3;border-color:#b6a17b38}.qd-shared-header[data-theme=dark] .v3-resource-menu>div{background:#151c25}
.qd-branded-page{padding-top:125px!important;scroll-padding-top:125px}
@keyframes qd-header-arrive{from{opacity:.35}to{opacity:1}}
@media(max-width:1150px){.qd-shared-header{left:2vw;right:2vw;padding:10px 14px;gap:8px}.qd-shared-header nav>a,.qd-shared-header summary{padding:9px 10px}.qd-shared-header .nav-right{gap:7px}.qd-shared-header .v3-button{padding:12px 15px}}
@media(max-width:850px){.qd-shared-header{top:8px;flex-wrap:wrap;border-radius:20px}.qd-shared-header nav{order:3;width:100%;justify-content:center;overflow:visible}.qd-shared-header .v3-logo{width:105px}.qd-shared-header .v3-logo img{height:30px}.qd-shared-header .v3-logo small{font-size:6px}.qd-shared-header .v3-button{display:none}.qd-shared-header .v3-market-buttons a{padding:8px;font-size:10px}.qd-shared-header .qd-theme{padding:6px}.qd-shared-header nav>a,.qd-shared-header summary{font-size:11px;padding:8px 10px}.qd-shared-header .v3-resource-menu>div{left:auto;right:0}.qd-branded-page{padding-top:150px!important}}
@media(prefers-reduced-motion:reduce){.qd-shared-header nav .v3-nav-current{animation:none}}
'''
js='''(()=>{const h=document.querySelector('.qd-shared-header'),b=h?.querySelector('.qd-theme');if(!h||!b)return;function set(t){h.dataset.theme=t;b.textContent=t==='dark'?'☀':'☾';b.setAttribute('aria-label','Switch navigation to '+(t==='dark'?'light':'dark')+' mode');b.setAttribute('aria-checked',String(t==='dark'))}let t;try{t=localStorage.getItem('qdnco-preview-theme')}catch{}set(t==='dark'?'dark':'light');b.addEventListener('click',()=>{const t=h.dataset.theme==='dark'?'light':'dark';set(t);try{localStorage.setItem('qdnco-preview-theme',t)}catch{}})})();'''
css+='\n/* Responsive publication navigation and reading surfaces. */\n.qd-branded-page main{min-width:0;max-width:1200px;box-sizing:border-box}\n.qd-branded-page main img,.qd-branded-page main video{max-width:100%;height:auto}\n.qd-branded-page main :is(input,select,textarea){max-width:100%;font-size:16px}\n.qd-branded-page main a{overflow-wrap:anywhere}\n.qd-branded-page main table{display:block;max-width:100%;overflow-x:auto}\n@media(max-width:1100px){.qd-shared-header{flex-wrap:wrap}.qd-shared-header nav{order:3;width:100%;justify-content:center}.qd-branded-page{padding-top:165px!important}}\n@media(max-width:600px){.qd-shared-header{left:8px;right:8px;padding:8px}.qd-shared-header nav{gap:0;padding:3px}.qd-shared-header nav>a,.qd-shared-header summary{font-size:11px;padding:10px 7px;min-height:44px;box-sizing:border-box;display:flex;align-items:center}.qd-shared-header .v3-logo{width:85px}.qd-shared-header .v3-resource-menu>div{max-width:calc(100vw - 40px);box-sizing:border-box}.qd-branded-page main{padding:24px 20px}.qd-branded-page main h1{font-size:clamp(32px,9vw,48px);overflow-wrap:break-word}.qd-resource-library main ul{grid-template-columns:minmax(0,1fr);padding-left:20px}.qd-branded-page main .intro{font-size:18px}.qd-branded-page main .cta{padding:24px}.qd-resource-library .v3-cta-enquiry{display:block}.qd-resource-library .v3-enquiry-starter{margin-top:24px}}\n'
(R/'_redesign/shared-header.css').write_text(css);(R/'_redesign/shared-header.js').write_text(js)
headers={}
for market,f in [('india','index.html'),('dubai','dubai/index.html')]:
 headers[market]=str(BeautifulSoup((R/f).read_text(),'html.parser').select_one('header.v3-nav'))
report=[]
for f in sorted(R.rglob('*.html')):
 rel=f.relative_to(R).as_posix()
 if rel in redesigned or rel.startswith('_redesign/'):continue
 doc=BeautifulSoup(f.read_text(),'html.parser')
 if not doc.body or not doc.head:continue
 market='dubai' if 'dubai' in rel.lower() else 'india'
 header=BeautifulSoup(headers[market],'html.parser').header
 header['class']=['qd-shared-header'];header['data-theme']='light'
 for x in header.select('[aria-current]'):del x['aria-current']
 for x in header.select('.v3-nav-current'):x['class']=[]
 active='Work' if rel.startswith('work/') else 'About' if rel.startswith('about/') else 'Resources'
 for x in header.select('nav>a,nav>details>summary'):
  if x.get_text(strip=True)==active:x['class']=['v3-nav-current'];x['aria-current']='page'
 toggle=header.select_one('[role=switch]')
 if toggle:
  button=doc.new_tag('button',attrs={'type':'button','class':'qd-theme','role':'switch','aria-checked':'false','aria-label':'Switch navigation to dark mode'});button.string='☾';toggle.replace_with(button)
 # Replace navigational header only, preserving article headings and breadcrumb links.
 old=doc.select_one('header.bar') or doc.select_one('body > nav')
 if not old and rel=='resources/index.html':old=doc.find('nav')
 if old:old.decompose()
 doc.body.insert(0,header);doc.body['class']=doc.body.get('class',[])+['qd-branded-page']
 doc.head.append(doc.new_tag('link',rel='stylesheet',href='/_redesign/shared-header.css'))
 doc.head.append(doc.new_tag('script',src='/_redesign/shared-header.js',defer=''))
 f.write_text(str(doc));report.append({'file':rel,'market':market,'logoHome':header.select_one('.v3-logo')['href']})
(P/'shared-header-report.json').write_text(json.dumps(report,indent=2))
print('Branded legacy/resource pages:',len(report))
# Downloadable publications retain content, with a clickable logo/navigation on every page.
import fitz
pdf_report=[]
for f in R.rglob('*.pdf'):
 doc=fitz.open(f);dubai='dubai' in f.name;home='https://qdnco.com/dubai/' if dubai else 'https://qdnco.com/'
 for page in doc:
  profile=page.rect.width>800
  if profile:
   page.add_redact_annot(fitz.Rect(40,25,155,70),fill=(.04,.065,.11));page.apply_redactions()
  rect=fitz.Rect(45,22 if profile else 8,145,65 if profile else 40)
  page.draw_rect(rect,color=(.69,.56,.34),fill=(.04,.065,.11),width=.7)
  page.insert_image(rect+ (5,4,-5,-4),filename=str(R/'_redesign/brands/qdco.png'),keep_proportion=True)
  page.insert_link({'kind':fitz.LINK_URI,'from':rect,'uri':home})
  x=180;y=47 if profile else 28
  for label,suffix in [('Home',''),('About','about/'),('Work','work/'),('Contact','contact/'),('Resources','resources/')]:
   url=('https://qdnco.com/resources/' if label=='Resources' else home+suffix)
   page.insert_text((x,y),label,fontsize=9,color=(.8,.69,.47) if profile else (.25,.24,.2))
   page.insert_link({'kind':fitz.LINK_URI,'from':fitz.Rect(x-3,y-12,x+57,y+5),'uri':url});x+=68
 tmp=f.with_suffix('.branded.pdf');doc.save(tmp,garbage=4,deflate=True);doc.close();tmp.replace(f);pdf_report.append(str(f.relative_to(R)))
(P/'branded-pdfs.json').write_text(json.dumps(pdf_report,indent=2))
print('Branded PDFs:',len(pdf_report))
