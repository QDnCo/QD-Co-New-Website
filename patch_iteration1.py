# Rebuild /iteration-1/ = the original design (commit f5f2b9d) with links kept inside the folder.
import json,subprocess,re
from pathlib import Path
P=Path(__file__).resolve().parent;D=P/'iteration-1';D.mkdir(exist_ok=True)
pages=['index','india','dubai','about','work','contact','dubai-about','dubai-work','dubai-contact','company-profile']+['case-'+c['slug'] for c in json.loads((P/'case-studies.json').read_text())]
for n in pages:
 s=subprocess.run(['git','show','f5f2b9d:'+n+'.html'],cwd=P,capture_output=True,text=True,check=True).stdout
 s=s.replace('<head>','<head><base href="/">',1)
 s=s.replace("const v3link=(page='index')=>(V3_DUBAI?(page==='index'?'dubai':'dubai-'+page):page)+'.html';","const v3link=(page='index')=>'/iteration-1/'+(V3_DUBAI?(page==='index'?'dubai':'dubai-'+page):page)+'.html';")
 for a,b in [('href="index.html"','href="/iteration-1/index.html"'),('href="dubai.html"','href="/iteration-1/dubai.html"'),("'work.html#'","'/iteration-1/work.html#'"),("href={'case-'","href={'/iteration-1/case-'"),('href="work.html"','href="/iteration-1/work.html"'),('href="contact.html"','href="/iteration-1/contact.html"'),('href="dubai-contact.html"','href="/iteration-1/dubai-contact.html"'),('href="company-profile.html"','href="/iteration-1/company-profile.html"'),("href={'work.html#'","href={'/iteration-1/work.html#'")]:
  s=s.replace(a,b)
 s=s.replace('QDnCo — Private design review 03','QDnCo — Iteration 1 (original)').replace('QDnCo Dubai — Private design review','QDnCo Dubai — Iteration 1 (original)')
 s=s.replace('assets/qd-ad-enhanced-1080x1920.mp4','assets/qd-ad-enhanced-540x960.mp4')  # lighter streaming copy of the same film

 # Founder film: autoplay muted when in view, "Play with sound" button (browsers block unmuted autoplay).
 s=s.replace("const filmRef=React.useRef(null),[needsSound,setNeedsSound]=useState(false);","const filmRef=React.useRef(null),wantsSound=React.useRef(false),[needsSound,setNeedsSound]=useState(true);")
 s=s.replace("if(!video)return;video.muted=false;video.volume=1;","if(!video)return;wantsSound.current=true;video.muted=false;video.volume=1;")
 s=s.replace("    if(video.ended)video.currentTime=0;\n","    if(video.ended)video.currentTime=0;\n    if(!wantsSound.current)video.muted=true;\n")
 s=s.replace("<video ref={filmRef} onVolumeChange","<video ref={filmRef} muted autoPlay onVolumeChange")
 s=s.replace('</body>','<script src="/iteration-switcher.js" data-iter="1"></script></body>',1)
 (D/(n+'.html')).write_text(s)
print('iteration-1:',len(pages),'pages')
