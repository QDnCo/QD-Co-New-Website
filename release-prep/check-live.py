from pathlib import Path
from urllib.request import Request,urlopen
from concurrent.futures import ThreadPoolExecutor
import xml.etree.ElementTree as ET,json,hashlib
P=Path(__file__).resolve().parent;B=P.parent/'release-source'
urls=[e.text for e in ET.fromstring((P/'live-sitemap.xml').read_text()).iter() if e.tag.endswith('}loc')]
def check(u):
 try:
  with urlopen(Request(u,headers={'User-Agent':'QDnCoMigrationAudit/1.0'}),timeout=25) as r:
   data=r.read();rel=u.removeprefix('https://qdnco.com/');rel=rel+'index.html' if not rel or rel.endswith('/') else rel;local=B/rel
   return dict(url=u,status=r.status,final=r.url,sha256=hashlib.sha256(data).hexdigest(),matchesLocalBaseline=local.exists() and local.read_bytes()==data)
 except Exception as e:return dict(url=u,error=str(e))
rows=list(ThreadPoolExecutor(8).map(check,urls));(P/'live-url-http-audit.json').write_text(json.dumps(rows,indent=2));print(json.dumps({'checked':len(rows),'ok':sum(x.get('status')==200 for x in rows),'differentFromLocal':[x['url'] for x in rows if x.get('status')==200 and not x['matchesLocalBaseline']],'errors':[x for x in rows if 'error'in x]},indent=2))
