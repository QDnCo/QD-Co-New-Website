from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import re,json,hashlib
P=Path(__file__).resolve().parent;R=P/'candidate';cache=P/'vendor-cache';cache.mkdir(exist_ok=True)
h=(R/'index.html').read_text();urls=re.findall(r'<script[^>]*src="(https://unpkg.com/[^"]+)"',h)
def download(u):
 n=u.split('/')[-1];f=cache/n
 if not f.exists():
  with urlopen(u,timeout=30) as r:data=r.read()
  f.write_bytes(data)
 target=R/'_redesign/vendor'/n;target.parent.mkdir(exist_ok=True);target.write_bytes(f.read_bytes())
 return {'source':u,'local':'/_redesign/vendor/'+n,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()}
rows=list(ThreadPoolExecutor(4).map(download,urls))
for item in json.loads((P/'route-manifest.json').read_text()):
 f=R/item['file'];s=f.read_text()
 for r in rows:s=s.replace(r['source'],r['local'])
 f.write_text(s)
(P/'vendor-manifest.json').write_text(json.dumps(rows,indent=2));print('Pinned official npm distribution assets copied locally:',len(rows))
