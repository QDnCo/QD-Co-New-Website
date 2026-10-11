from pathlib import Path
P=Path(__file__).resolve().parent
s=(P/'index.html').read_text()
s=s.replace('QDnCo — Private design review 03','QDnCo Dubai — Private design review')
for n in ['dubai','dubai-about','dubai-work','dubai-contact']:
 (P/(n+'.html')).write_text(s)
print('Built four private Dubai pages from the shared India layout. No production changes.')

# Keep the owner-authorized temporary preview current after both regional builds.
if Path("/tmp/qdnco-share-preview-20261011").is_dir():
 import subprocess,sys
 subprocess.run([sys.executable,str(P/"sync-share-preview.py")],check=True)
