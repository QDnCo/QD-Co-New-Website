from pathlib import Path
P=Path(__file__).parent
R=P/'build-inputs'
s=(R/'dubai-v3-base.html').read_text()
s=s.replace('href="https://qdnco.com/guides/">Guides & insights ↗','href="insights/index.html">Guides & insights ↗')
s=s.replace('</head>','<style>'+(P/'dubai-v4.css').read_text()+'</style></head>')
s=s.replace('ReactDOM.createRoot(document.getElementById("root")).render(<App/>);',(P/'dubai-v4.jsx').read_text()+'\nReactDOM.createRoot(document.getElementById("root")).render(<DubaiApp/>);')
s=s.replace('Architectural hero is an AI-generated concept, not a client project.','Performance figures retain their stated source and scope.')
s=s.replace('QDnCo — Private design review 03','QDnCo Dubai — Private design review 04')
for n in ['dubai','dubai-about','dubai-work','dubai-contact']:(P/(n+'.html')).write_text(s)
print('Built four private Dubai pages. India and production files not written.')
