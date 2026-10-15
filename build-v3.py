import hashlib
from pathlib import Path
import re,json,urllib.request,shutil
P=Path(__file__).resolve().parent
s=(P/'build-inputs/legacy-visual-base.html').read_text()
# Retain the original visual components and CSS; replace only page composition.
s=re.sub(r'<meta name="robots"[^>]+>', '<meta name="robots" content="noindex,nofollow">',s)
s=re.sub(r'<link rel="canonical"[^>]+>','',s)
s=re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>','',s)
s=s[:s.index('function App() {')]
s=s.replace('Ongoing · locked by month 3','Ongoing optimisation').replace('₹266 per lead · 51% sales-ready','Qualification · visits · sales feedback').replace('₹6L+ / month under management','Routing · follow-up · reporting').replace('By month three the funnel, the reporting and the scaling rules are locked and repeatable — the system runs whether or not anyone is watching it.','The team refines the funnel, reporting and scaling rules as reliable project evidence develops.')
s=s.replace('The platforms those five capabilities run on','The platforms behind connected delivery')
s=s.replace('<title>Real Estate Marketing, Bangalore | QDnCo</title>','<title>QDnCo — Private design review 03</title>')
css=(P/'v3.css').read_text();s=s.replace('</head>','<style>'+css+'</style></head>')
s+=(P/'v3.jsx').read_text()+'\nReactDOM.createRoot(document.getElementById("root")).render(<App/>);\n</script></body></html>'
s=s.replace('</head>', '<link rel="stylesheet" href="gold-ui.css?v='+hashlib.sha256((P/'gold-ui.css').read_bytes()).hexdigest()[:12]+'"></head>')
s=s.replace('</head>', '<link rel="stylesheet" href="responsive.css?v='+hashlib.sha256((P/'responsive.css').read_bytes()).hexdigest()[:12]+'"></head>')
s=s.replace('</head>', '<link rel="stylesheet" href="v4.css?v='+hashlib.sha256((P/'v4.css').read_bytes()).hexdigest()[:12]+'"></head>')
s=s.replace('</head>', '<link rel="stylesheet" href="iterations.css?v='+hashlib.sha256((P/'iterations.css').read_bytes()).hexdigest()[:12]+'"></head>')
s=s.replace('</body>','<script src="/iteration-switcher.js"></script><script src="/testimonials.js"></script></body>',1)
s=s.replace('<title>QDnCo — Private design review 03</title>','<title>QDnCo — Design iterations</title>')
for n in ['index','india','dubai','about','work','contact','dubai-about','dubai-work','dubai-contact','company-profile']:(P/(n+'.html')).write_text(s)
for case in json.loads((P/'case-studies.json').read_text()):
 (P/('case-'+case['slug']+'.html')).write_text(s)
if not (P/'assets/world.json').exists():
 data=json.load(urllib.request.urlopen('https://raw.githubusercontent.com/nvkelso/natural-earth-vector/master/geojson/ne_110m_admin_0_countries.geojson'))
 (P/'assets/world.json').write_text(json.dumps([f['geometry'] for f in data['features']],separators=(',',':')))
print('Built private iteration 03 only')

import subprocess,sys
subprocess.run([sys.executable,str(P/"brand-icons.py")],check=True)
