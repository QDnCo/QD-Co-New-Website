from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin,urlparse,unquote
import json,re,hashlib,xml.etree.ElementTree as ET
P=Path(__file__).resolve().parent;R=P/'candidate';B=P.parent/'release-source'
class Page(HTMLParser):
 def __init__(self,s):
  super().__init__();self.links=[];self.meta={};self.h1=0;self.canon=[];self.feed(s)
 def handle_starttag(self,t,a):
  a=dict(a)
  if t=='h1':self.h1+=1
  if t=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if t=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
  if t in ('a','img','script','link','video','source','iframe'):
   for k in ['href','src','poster']:
    if a.get(k):self.links.append(a[k])
def resolve(u):
 p=R/unquote(urlparse(u).path).lstrip('/');return p/'index.html' if p.is_dir() or u.endswith('/') else p
old=ET.fromstring((P/'live-sitemap.xml').read_text());urls=[e.text for e in old.iter() if e.tag.endswith('}loc')]
missing=[u for u in urls if not resolve(u).exists()]
pages=json.loads((P/'route-manifest.json').read_text());errors=[];broken=[]
for f in [R/'resources/index.html',*sorted((R/'insights').glob('*.html'))]:
 h=Page(f.read_text());pages.append(dict(file=str(f.relative_to(R)),url=h.canon[0]))
for p in pages:
 s=(R/p['file']).read_text();h=Page(s)
 if not re.search(r'<title>[^<]+</title>',s):errors.append([p['file'],'missing title'])
 if h.h1!=1:errors.append([p['file'],'H1 count',h.h1])
 if h.canon!=[p['url']]:errors.append([p['file'],'canonical',h.canon])
 if not h.meta.get('description'):errors.append([p['file'],'missing description'])
 for data in re.findall(r'<script type="application/ld\+json">([\s\S]*?)</script>',s):json.loads(data)
 for link in h.links:
  u=urljoin(p['url'],link);v=urlparse(u)
  if v.netloc=='qdnco.com' and v.scheme=='https' and not resolve(u).exists():broken.append([p['file'],link])
 if 'type="text/babel"' in s or 'cdn.tailwindcss.com' in s:errors.append([p['file'],'runtime compiler'])
retained=[];changed=[]
for f in B.rglob('*'):
 if not f.is_file():continue
 rel=f.relative_to(B);target=R/rel
 if not target.exists():errors.append([str(rel),'deleted baseline file']);continue
 (retained if f.read_bytes()==target.read_bytes() else changed).append(str(rel))
result=dict(oldSitemapURLs=len(urls),missingOldURLs=missing,renderedPages=len(pages),unchangedBaselineFiles=len(retained),changedBaselineFiles=changed,errors=errors,brokenLocalReferences=list({tuple(x) for x in broken}),checks='Static HTML, metadata, JSON-LD, URL/file continuity. Does not assert external publication or ranking.')
(P/'audit.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
raise SystemExit(bool(errors or missing or broken))
