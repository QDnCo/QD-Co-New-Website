# Refresh only the sanitized temporary snapshot; never production.
from pathlib import Path
import shutil,subprocess,json
src=Path(__file__).resolve().parent
root=Path('/tmp/qdnco-share-preview-20261011');root.mkdir(exist_ok=True)
for p in src.iterdir():
 if p.is_file() and (p.suffix in ['.html','.css','.jsx','.js'] or p.name=='case-studies.json') and not p.name.startswith('dubai-v4'):
  shutil.copy2(p,root/p.name)
for folder in ['assets','brands','adreel','shots','team','insights','profile-preview']:
 for p in (src/folder).rglob('*'):
  if p.is_file() and p.suffix.lower() in ['.png','.jpg','.jpeg','.webp','.avif','.svg','.mp4','.webm','.woff','.woff2','.html','.css','.js','.pdf'] or p.is_file() and p.name in ['world.json','india-states.json']:
   dest=root/p.relative_to(src);dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
(root/'robots.txt').write_text('User-agent: *\nDisallow: /\n')

print("Temporary share preview refreshed")

# Keep preserved guides and publications branded in the temporary snapshot.
if (src/'release-prep/shared-header-report.json').exists():
 import sys
 subprocess.run([sys.executable,str(src/'release-prep/preview-branded-pages.py')],check=True)

subprocess.run([sys.executable,str(src/"brand-icons.py"),str(root)],check=True)
