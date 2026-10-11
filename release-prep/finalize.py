"""Local-only semantic metadata, legacy compatibility, migration reports."""
from pathlib import Path
from bs4 import BeautifulSoup
import json,hashlib,re
P=Path(__file__).resolve().parent;R=P/'candidate';B=P.parent/'release-source'
manifest=json.loads((P/'route-manifest.json').read_text())
# Old pricing URL stays public with the new, visible calculator; do not 404 paid/ad backlinks.
s=(R/'contact/index.html').read_text().replace('https://qdnco.com/contact/','https://qdnco.com/pricing/index.html').replace('<title>Real Estate Marketing Pricing & Contact | QDnCo</title>','<title>Real Estate Marketing Pricing & Campaign Calculator | QDnCo</title>')
(R/'pricing/index.html').write_text(s)
manifest.append(dict(source='pricing/index.html',url='https://qdnco.com/pricing/index.html',file='pricing/index.html'))
for m in manifest:
 f=R/m['file'];s=f.read_text();soup=BeautifulSoup(s,'html.parser');block=soup.find('script',type='application/ld+json');schema=json.loads(block.string);graph=schema['@graph']
 if m['source'] in ['index.html','dubai.html']:
  questions=[]
  for d in soup.select('#faq details'):
   questions.append({'@type':'Question','name':d.summary.get_text(' ',strip=True),'acceptedAnswer':{'@type':'Answer','text':d.p.get_text(' ',strip=True)}})
  if questions:graph.append({'@type':'FAQPage','@id':m['url']+'#faq','mainEntity':questions})
  for card in soup.select('#services li'):
   heading=card.find(['h3','h4']);
   if not heading:continue
   graph.append({'@type':'Service','name':re.sub(r'^\d+\s+','',heading.get_text(' ',strip=True)),'provider':{'@id':'https://qdnco.com/#organization'},'areaServed':{'@type':'Country','name':'United Arab Emirates' if m['source']=='dubai.html' else 'India'},'url':m['url']+'#services'})
  # Anchor destinations retain old incoming campaign links to the homepage.
  aliases='<span id="top"></span><span id="intro"></span>'
  s=s.replace('<div id="root">','<div id="root">'+aliases,1)
  # React also retains these compatibility anchors via the runtime patch below.
  s=s.replace('id="roadmap"','id="roadmap"',1)
  s=s.replace('<footer class="v3-footer','<span id="contact"></span><span id="pricing"></span><span id="roadmap-full"></span><footer class="v3-footer',1)
 if '/dubai/' in m['url']:
  graph.append({'@type':'Audience','@id':m['url']+'#audience','audienceType':'Dubai realtors, developers and mandate firms; realtors / channel partners'})
  for node in graph:
   if node.get('@type') in ['WebPage','ContactPage','AboutPage','Service']:node['audience']={'@id':m['url']+'#audience'}
 if m['url']!='https://qdnco.com/':graph.append({'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'QDnCo','item':'https://qdnco.com/'},{'@type':'ListItem','position':2,'name':soup.title.get_text(),'item':m['url']}]})
 s=s.replace(str(block),'<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script>') if str(block) in s else re.sub(r'<script type="application/ld\+json">[\s\S]*?</script>',lambda _:'<script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False).replace('<','\\u003c')+'</script>',s,count=1)
 f.write_text(s);m['sha256']=hashlib.sha256(f.read_bytes()).hexdigest()
# Runtime anchors: hash jump / old modal CTA should bring visitors to actual enquiry contact.
app=R/'_redesign/app.js';a=app.read_text();a+='''
(function(){function legacyAnchor(){if(['#contact','#pricing'].includes(location.hash)){location.replace((location.pathname.startsWith('/dubai/')?'/dubai/contact/':'/contact/')+location.search)}else if(location.hash==='#roadmap-full'){document.getElementById('roadmap')?.scrollIntoView()}else if(['#intro','#top'].includes(location.hash)){window.scrollTo(0,0)}}window.addEventListener('hashchange',legacyAnchor);legacyAnchor()})();
''';app.write_text(a)
# Retain historical URLs; mark withdrawn commercial models and link current calculators.
legacy=[]
for f in R.rglob('*.html'):
 if '_redesign' in str(f) or f.relative_to(R).as_posix() in {m['file'] for m in manifest}:continue
 raw=f.read_text();doc=BeautifulSoup(raw,'html.parser');[x.decompose() for x in doc(['script','style'])];text=doc.get_text(' ',strip=True)
 if not any(x in text for x in ['₹550','AED 200 per','₹75,000–₹1,00,000','₹495','Pay per qualified lead if']):continue
 target='/dubai/contact/' if str(f.relative_to(R)).startswith('dubai/') else '/pricing/index.html'
 notice=f'<aside aria-label="Current pricing update" style="padding:24px;margin:24px auto;max-width:1080px;border:2px solid #a1844b;border-radius:16px;background:#faf3e5;color:#202620"><strong>QDnCo pricing update — 11 October 2026.</strong><p>Earlier lead-fee and flat-retainer examples on this page are historical and are no longer QDnCo offers. Meta/Google Ad Campaigns are priced by campaign count in India and project count in Dubai. Other services are quoted individually. Media spend is separate.</p><a href="{target}">See the current pricing calculator and included services →</a></aside>'
 raw=re.sub(r'(<body[^>]*>)',lambda m:m[1]+notice,raw,count=1)
 # Remove outdated FAQ/Offer markup; retain website/article/entity schema without stale prices.
 def clean_schema(match):
  try:data=json.loads(match[1])
  except:return ''
  if '@graph' in data:data['@graph']=[x for x in data['@graph'] if x.get('@type') not in ['FAQPage','Offer','Product','Service']]
  elif data.get('@type') in ['FAQPage','Offer','Product','Service']:return ''
  return '<script type="application/ld+json">'+json.dumps(data)+'</script>'
 raw=re.sub(r'<script type="application/ld\+json">([\s\S]*?)</script>',clean_schema,raw)
 f.write_text(raw);legacy.append(str(f.relative_to(R)))
# Current AI-readable summary excludes superseded pricing offered by older exports.
summary='''# QDnCo — current website reference\n\nReal estate performance marketing for developers, channel partners and mandate firms. QDnCo is based in Bengaluru, India; serving Dubai is not a claim of a Dubai office.\n\n## Services\nMeta/Google Ad Campaigns; Real Estate SEO & AI Search Optimization (SEO, AEO and GEO); CRM Setup & Automation; Landing Pages; AI Lead Follow-Up & WhatsApp Automation.\n\n## Commercial model\nIndia campaign retainers: channel partner INR 54,000 for one, 48,600 each for two, 45,600 each for three or four, 43,200 each for five or more. Developer/mandate: INR 78,000; 70,200; 66,000; 62,400 respectively.\nDubai realtor/channel partner project retainers (one campaign per project): AED 4,650 for one; 4,185 each for two; 3,927 each for three/four; 3,720 each for five or more. Dubai developers and mandate firms: AED 6,717 for one; 6,045 each for two; 5,683 each for three/four; 5,373 each for five or more. Rates use the exact India tier ratios scaled to AED 4,650 for the realtor anchor, rounded to the nearest AED; not an exchange-rate conversion. Dubai audience priority: realtors, developers and mandate firms; channel partner is a secondary synonym. Final scope confirmed in writing. Media spend separate; three-month engagement. Other services custom quote. No current pay-per-qualified-lead billing offer.\n\n## Evidence\nManagement-reported aggregate India experience is labelled in the website. Pipeline influenced is not sales revenue. Do not infer Dubai campaign outcomes from India figures, or endorsement from developer marks.\n\n## Contact\nqdnco01@gmail.com; +91 88611 79992\n\n## Canonical pages\n'''
summary+='\n'.join('- '+m['url'] for m in manifest if m['source']!='company-profile.html')+'\n\n## Research, guides and footprint\nhttps://qdnco.com/resources/\nhttps://qdnco.com/guides/\nhttps://qdnco.com/answers/\nhttps://qdnco.com/data/\nhttps://qdnco.com/sitemap.xml\n'
(R/'llms-full.txt').write_text(summary)
(R/'llms.txt').write_text(summary+'\n## Public profiles\n'+'\n'.join('- '+p['name']+': '+p['url'] for p in json.loads((P/'profiles.json').read_text())))
(P/'legacy-commercial-notices.json').write_text(json.dumps(legacy,indent=2))
(P/'route-manifest.json').write_text(json.dumps(manifest,indent=2))
# Sitemaps: every added indexable route including pricing remains listed.
s=(R/'sitemap.xml').read_text()
for m in manifest:
 if m['source']=='company-profile.html' or '<loc>'+m['url']+'</loc>' in s:continue
 s=s.replace('</urlset>',f'<url><loc>{m["url"]}</loc></url>\n</urlset>')
(R/'sitemap.xml').write_text(s)
print('Structured metadata + legacy commercial notices:',len(legacy),'pages. No deployment.')

# New resource pages get distinct descriptions, sharing metadata and truthful Article/Collection schema.
for f in [R/'resources/index.html',*sorted((R/'insights').glob('*.html'))]:
 doc=BeautifulSoup(f.read_text(),'html.parser');title=doc.title.get_text(' ',strip=True).replace(' — Private Preview','')
 url=doc.select_one('link[rel=canonical]')['href'];h=doc.h1.get_text(' ',strip=True)
 first=doc.find('p');description=(first.get_text(' ',strip=True) if first else h+' — QDnCo real estate marketing resources.')[:170]
 for name,content in [('description',description),('twitter:card','summary_large_image')]:
  tag=doc.new_tag('meta',attrs={'name':name,'content':content});doc.head.append(tag)
 for prop,content in [('og:title',title),('og:description',description),('og:url',url),('og:type','website' if f.name=='index.html' else 'article'),('og:image','https://qdnco.com/_redesign/shots/indium.jpg')]:doc.head.append(doc.new_tag('meta',attrs={'property':prop,'content':content}))
 tag=doc.new_tag('script',type='application/ld+json');tag.string=json.dumps({'@context':'https://schema.org','@type':'CollectionPage' if f.name=='index.html' else 'Article','headline':h,'name':title,'url':url,'description':description,'publisher':{'@id':'https://qdnco.com/#organization','@type':'Organization','name':'QDnCo','url':'https://qdnco.com/'}});doc.head.append(tag);f.write_text(str(doc))
# Resolve resource navigation against the release routes, including query/fragment variants.
from urllib.parse import urlsplit,urlunsplit
routes={'index.html':'/','about.html':'/about/','work.html':'/work/index.html','contact.html':'/contact/','dubai.html':'/dubai/','dubai-contact.html':'/dubai/contact/','resources.html':'/resources/','company-profile.html':'/company-profile/'}
for f in [R/'resources/index.html',*sorted((R/'insights').glob('*.html'))]:
 doc=BeautifulSoup(f.read_text(),'html.parser')
 for a in doc.select('[href]'):
  u=urlsplit(a['href']);key=u.path.removeprefix('../')
  if not u.netloc and key in routes:a['href']=urlunsplit(('','',routes[key],u.query,u.fragment))
  if a['href']=='gold-ui.css':a['href']='/_redesign/gold-ui.css'
 f.write_text(str(doc))
for f in (P.parent/'insights').iterdir():
 if f.suffix in ['.css','.csv']:(R/'insights'/f.name).write_bytes(f.read_bytes())
# Track the new resource pages with the same property; never send local preview traffic.
analytics='''<script>if(['qdnco.com','www.qdnco.com'].includes(location.hostname)){var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=G-GZE73M9Q4M';document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config','G-GZE73M9Q4M',{content_group:'Resources'});}</script>'''
for f in [R/'resources/index.html',*sorted((R/'insights').glob('*.html'))]:
 s=f.read_text()
 if 'G-GZE73M9Q4M' not in s:s=s.replace('</body>',analytics+'</body>');f.write_text(s)
