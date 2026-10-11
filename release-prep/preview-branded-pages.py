"""Publish only to the existing noindex temporary snapshot, never production."""
from pathlib import Path
from bs4 import BeautifulSoup
import shutil,json,re
P=Path(__file__).resolve().parent;R=P/'candidate';T=Path('/tmp/qdnco-share-preview-20261011')
if not T.is_dir():raise SystemExit('No running share snapshot; skip')
records=json.loads((P/'shared-header-report.json').read_text())
routes={'/':'/index.html','/about/':'/about.html','/work/':'/work.html','/work/index.html':'/work.html','/contact/':'/contact.html','/resources/':'/resources.html','/dubai/':'/dubai.html','/dubai/about/':'/dubai-about.html','/dubai/work/':'/dubai-work.html','/dubai/contact/':'/dubai-contact.html'}
for row in records:
 src=R/row['file'];dest=T/row['file'];dest.parent.mkdir(parents=True,exist_ok=True)
 doc=BeautifulSoup(src.read_text(),'html.parser')
 for tag in doc.select('meta[name=robots]'):tag.decompose()
 doc.head.append(doc.new_tag('meta',attrs={'name':'robots','content':'noindex,nofollow'}))
 # No analytics or production submission code in the temporary review.
 for tag in doc.find_all('script'):
  if any(x in str(tag) for x in ['googletagmanager','gtag(','google-analytics']):tag.decompose()
 for a in doc.select('a[href]'):
  if a['href'] in routes:a['href']=routes[a['href']]
 dest.write_text(str(doc))
 if row['file']=='resources/index.html':(T/'resources.html').write_text(str(doc))
 # Copy local page dependencies without overwriting existing redesign assets.
 for tag,attr in [('img','src'),('script','src'),('link','href'),('video','poster'),('a','href')]:
  for item in doc.find_all(tag):
   val=item.get(attr,'').split('?')[0]
   if not val or '://' in val or val.startswith('data:'):continue
   source=R/val.lstrip('/') if val.startswith('/') else src.parent/val
   source=source.resolve()
   if source.is_file() and source.is_relative_to(R.resolve()) and source.suffix.lower()!='.html':
    target=T/source.relative_to(R.resolve());target.parent.mkdir(parents=True,exist_ok=True)
    if not target.exists() or source.name.startswith('shared-header'):shutil.copy2(source,target)
for name in ['shared-header.css','shared-header.js']:
 dest=T/'_redesign'/name;dest.parent.mkdir(exist_ok=True);shutil.copy2(R/'_redesign'/name,dest)
for name in json.loads((P/'branded-pdfs.json').read_text()):
 dest=T/name;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(R/name,dest)
 if name.startswith('_redesign/assets/'):
  shutil.copy2(R/name,T/'assets'/Path(name).name)
# Make the shared preview's resource links visit the newly branded preview documents.
for f in T.glob('*.html'):
 s=f.read_text()
 for prefix in ['guides/','answers/','data/','compare/','glossary/','areas/','legal/','tools/']:
  s=s.replace('https://qdnco.com/'+prefix,'/'+prefix)
 f.write_text(s)
print('Temporary branded resources refreshed:',len(records))

# Apply the same approved favicon to every temporary review page.
import subprocess,sys
subprocess.run([sys.executable,str(Path(__file__).resolve().parent.parent/"brand-icons.py"),"/tmp/qdnco-share-preview-20261011"],check=True)
