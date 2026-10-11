"""Package the approved, unchanged square QDnCo artwork as website icons."""
from pathlib import Path
from PIL import Image
from bs4 import BeautifulSoup
import base64,json,shutil
ROOT=Path(__file__).resolve().parent
FILES=['favicon.svg','favicon.ico','icon-48.png','icon-96.png','icon-192.png','icon-512.png','apple-touch-icon.png','site.webmanifest']
TAGS='''<link rel="icon" type="image/png" sizes="96x96" href="/icon-96.png"><link rel="icon" type="image/svg+xml" href="/favicon.svg"><link rel="shortcut icon" href="/favicon.ico"><link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png"><link rel="manifest" href="/site.webmanifest">'''
def package():
 source=ROOT/'assets/qdnco-brand-square.jpg'
 im=Image.open(source).convert('RGB')
 for size in [48,96,192,512]:im.resize((size,size),Image.Resampling.LANCZOS).save(ROOT/f'icon-{size}.png')
 im.resize((180,180),Image.Resampling.LANCZOS).save(ROOT/'apple-touch-icon.png')
 im.save(ROOT/'favicon.ico',sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)])
 encoded=base64.b64encode(source.read_bytes()).decode()
 (ROOT/'favicon.svg').write_text(f'<svg xmlns="http://www.w3.org/2000/svg" width="720" height="720" viewBox="0 0 720 720"><title>QDnCo</title><image width="720" height="720" href="data:image/jpeg;base64,{encoded}"/></svg>')
 (ROOT/'site.webmanifest').write_text(json.dumps({'name':'QDnCo','short_name':'QDnCo','start_url':'/','display':'browser','icons':[{'src':f'/icon-{n}.png','sizes':f'{n}x{n}','type':'image/png'} for n in [192,512]]},indent=2))
def apply(root):
 root=Path(root)
 for f in FILES:
  if root!=ROOT:shutil.copy2(ROOT/f,root/f)
 count=0
 for p in root.rglob('*.html'):
  if root==ROOT and (len(p.relative_to(ROOT).parts)>1 and p.relative_to(ROOT).parts[0] not in ['insights']):continue
  s=p.read_text();soup=BeautifulSoup(s,'html.parser')
  if not soup.head:continue
  # Preserve original page bytes except icon tags and logo schema fields.
  for tag in soup.find_all('link'):
   rel=tag.get('rel',[])
   if any('icon' in r or r=='manifest' for r in rel):
    s=s.replace(str(tag),'') if str(tag) in s else s
  import re
  s=re.sub(r'<link\b[^>]*\brel=["\'][^"\']*(?:icon|manifest)[^"\']*["\'][^>]*>','',s,flags=re.I)
  s=s.replace('</head>',TAGS+'</head>',1)
  s=s.replace('https://qdnco.com/_redesign/brands/qdco.png','https://qdnco.com/icon-512.png')
  p.write_text(s);count+=1
 return count
if __name__=='__main__':
 import sys
 package(); print('QDnCo icons applied to',apply(Path(sys.argv[1]) if len(sys.argv)>1 else ROOT),'HTML files')
