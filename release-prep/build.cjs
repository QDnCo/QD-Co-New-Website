/* Local-only release builder. No deployment commands, no production writes. */
const fs=require('fs'),path=require('path'),vm=require('vm'),crypto=require('crypto');
const root=path.resolve(__dirname,'..'),live=path.resolve(root,'release-source'),out=path.join(__dirname,'candidate');
const deps=path.resolve(root,'node_modules');
const React=require(deps+'/react'),SSR=require(deps+'/react-dom/server'),Motion=require(deps+'/framer-motion');
const {transform}=require(deps+'/sucrase');
const read=p=>fs.readFileSync(p,'utf8'),write=(p,s)=>{fs.mkdirSync(path.dirname(p),{recursive:true});fs.writeFileSync(p,s)};
const sha=s=>crypto.createHash('sha256').update(s).digest('hex');
if(out!==path.join(root,'release-prep/candidate'))throw Error('Unsafe destination');
fs.mkdirSync(out,{recursive:true});fs.cpSync(live,out,{recursive:true});
for(const dir of ['assets','brands','adreel','shots','team'])fs.cpSync(path.join(root,dir),path.join(out,'_redesign',dir),{recursive:true,filter:p=>!p.endsWith('.md')});
for(const file of ['gold-ui.css','responsive.css','v4.css','iterations.css','iteration-switcher.js','testimonials.js','testimonials.json','case-studies.json'])fs.copyFileSync(path.join(root,file),path.join(out,'_redesign',file));
const cases=JSON.parse(read(root+'/case-studies.json'));
const profiles=JSON.parse(read(__dirname+'/profiles.json'));
const route={'index.html':'/','india.html':'/','dubai.html':'/dubai/','about.html':'/about/','work.html':'/work/index.html','contact.html':'/contact/','dubai-about.html':'/dubai/about/','dubai-work.html':'/dubai/work/','dubai-contact.html':'/dubai/contact/','company-profile.html':'/company-profile/','resources.html':'/resources/'};
for(const c of cases)route['case-'+c.slug+'.html']='/work/'+c.slug+'.html';
const assetRewrite=s=>s.replace(/(["'`(=])\/?(assets|brands|adreel|shots|team)\//g,'$1/_redesign/$2/').replace(/(["'])case-studies\.json\1/g,'$1/_redesign/case-studies.json$1');
let template=read(root+'/index.html'),jsx=template.match(/<script type="text\/babel">([\s\S]*?)<\/script>/)[1].replace(/ReactDOM.createRoot[\s\S]*$/,'');
jsx=jsx.replaceAll('location.pathname','QD_PAGE');
jsx=jsx.replace("const v3link=(page='index')=>(V3_DUBAI?(page==='index'?'dubai':'dubai-'+page):page)+'.html';","const v3link=(page='index')=>QD_ROUTES[(V3_DUBAI?(page==='index'?'dubai':'dubai-'+page):page)+'.html'];");
jsx=jsx.replace('const[data,setData]=useState([])','const[data,setData]=useState(QD_CASES)');
jsx=jsx.replaceAll("'case-'+p.slug+'.html'","QD_ROUTES['case-'+p.slug+'.html']").replaceAll("'case-'+q.slug+'.html'","QD_ROUTES['case-'+q.slug+'.html']");
for(const [from,to] of Object.entries(route))jsx=jsx.replaceAll('"'+from+'"','"'+to+'"').replaceAll("'"+from+"'","'"+to+"'");
// Keep runtime route dictionary keys as preview filenames, not destination URLs.
jsx=jsx.replace(/QD_ROUTES\[("|')(\/[^\]]*)\1\]/g,(m,q,d)=>'QD_ROUTES['+JSON.stringify(Object.keys(route).find(k=>route[k]===d)||d)+']');
jsx=jsx.replace(/href="insights\//g,'href="/insights/').replaceAll('"insights/','"/insights/').replaceAll("'insights/","'/insights/");
jsx=jsx.replace('<div className="v3-review">PRIVATE REVIEW 03 · NOT PUBLISHED</div>','');
jsx=jsx.replace(' · Private design review','').replace('Company profile / Private review','Company profile');
jsx=jsx.replace('used in this private design preview','project imagery').replace('Private pricing review · These rates are not a published offer.','Indicative estimate. Final scope and fees confirmed in writing.');
jsx=jsx.replace('onSubmit={e=>{e.preventDefault();setDone(true)}}','onSubmit={e=>window.QDSubmitEnquiry(e,setDone)}');
jsx=jsx.replace('Preview enquiry flow ↗','Send my enquiry ↗').replace("done?'Preview complete. No information was sent and no booking was created.':'Private preview. This form does not submit leads or reserve a calendar slot.'","done||'By submitting, you agree to be contacted about this enquiry. A preferred date is a request, not a confirmed booking.'");
jsx=jsx.replace('minLength="7"','minLength="8"').replace('digits.length>=7','digits.length>=8');
jsx=jsx.replace('<input type="hidden" name="enquiryType" value={role}/>','<input type="hidden" name="enquiryType" value={role}/><input type="hidden" name="indicativePrice" value={hasCampaignPrice?(V3_DUBAI?"AED "+dubaiRate+" per project/month":"INR "+price+" per campaign/month"):"Custom scope requested"}/><a href="/legal/privacy.html">Privacy policy</a>');
jsx=jsx.replaceAll('work.html#','/work/index.html#');
jsx+='\nV3_FOOTER_GROUPS["Find QDnCo"].push(["Sortlist","https://www.sortlist.com/agency/qdnco"]);';
jsx=assetRewrite(jsx);
const code=transform(jsx,{transforms:['jsx'],production:true,jsxRuntime:'classic'}).code;
write(out+'/_redesign/app.js',code+'\nReactDOM.createRoot(document.getElementById("root")).render(React.createElement(App));');
write(out+'/_redesign/lead-adapter.js',read(__dirname+'/lead-adapter.js'));
let head=template.slice(template.indexOf('<head>')+6,template.indexOf('</head>'));
head=head.replace(/<title>[\s\S]*?<\/title>/g,'').replace(/<meta\s+(?:name|property)="(?:description|robots|geo\.[^"]+|ICBM|og:[^"]+|twitter:[^"]+)"[^>]*>/g,'');
head=head.replace(/<script[^>]*src="https:\/\/cdn.tailwindcss.com"[^>]*><\/script>/g,'').replace(/<script[^>]*src="[^"]*babel[^\"]*"[^>]*><\/script>/g,'');
head=head.replace(/<script>\s*tailwind.config[\s\S]*?<\/script>/g,'');
head=head.replace(/href="gold-ui.css[^\"]*"/g,'href="/_redesign/gold-ui.css"');head=assetRewrite(head).replaceAll('href="favicon.svg"','href="/favicon.svg"');
head=head.replace(/href="responsive.css[^\"]*"/g,'href="/_redesign/responsive.css"');head=head.replace(/href="v4.css[^\"]*"/g,'href="/_redesign/v4.css"');head=head.replace(/href="iterations.css[^\"]*"/g,'href="/_redesign/iterations.css"');
const liveHome=read(live+'/index.html');
const tw=liveHome.match(/<style id="tw-build">([\s\S]*?)<\/style>/);if(tw)head='<style id="tw-build">'+tw[1]+'</style>'+head;
head+='<style>#boot-loader{display:none}html{scroll-behavior:smooth}</style><noscript><style>[style*="opacity:0"]{opacity:1!important;transform:none!important}.v3-client-questions button{display:none}</style></noscript>';
const endpoint=liveHome.match(/https:\/\/script.google.com\/macros\/s\/[^\s"'<>]+\/exec/)[0];
const metadata={
 'index.html':['Real Estate Marketing Agency in Bangalore & India | QDnCo','Real estate performance marketing and lead generation for developers, channel partners and mandate firms. Meta/Google ads, SEO and CRM support.'],
 'dubai.html':['Real Estate Marketing for Dubai Realtors & Developers | QDnCo','Property marketing for Dubai realtors, developers and mandate firms: Meta/Google ads, real estate SEO, AI search visibility and sales follow-up.'],
 'about.html':['About QDnCo | Real Estate Marketing Team','Meet the QDnCo team connecting property marketing, creative campaigns and lead follow-up for developers and channel partners.'],
 'work.html':['Real Estate Marketing Projects & Case Studies | QDnCo','Explore QDnCo’s direct and partner-led property portfolio, campaign plans and clearly attributed results.'],
 'contact.html':['Real Estate Marketing Pricing & Contact | QDnCo','Estimate Meta/Google campaign fees for your projects and contact QDnCo. Custom scopes for SEO, AI search, CRM and landing pages.'],
 'dubai-about.html':['About QDnCo | Dubai Property Marketing','Meet the India-based QDnCo team helping Dubai realtors, developers and mandate firms with property marketing, creative and technology.'],
 'dubai-work.html':['Dubai Property Marketing Portfolio | QDnCo','Explore Dubai developer project context and QDnCo’s approach to property marketing. Project imagery is not proof of campaign results.'],
 'dubai-contact.html':['Dubai Real Estate Marketing Pricing in AED | QDnCo','Dubai realtor/channel partner campaigns from AED 4,650 per project/month. Separate developer/mandate rates. Media spend additional; volume pricing available.'],
 'company-profile.html':['QDnCo Company Profile','Explore QDnCo’s real estate marketing services and team.']};
const graphOrg={'@type':'Organization','@id':'https://qdnco.com/#organization',name:'QDnCo',url:'https://qdnco.com/',logo:'https://qdnco.com/_redesign/brands/qdco.png',email:'qdnco01@gmail.com',telephone:'+918861179992',sameAs:profiles.filter(p=>p.status==='verified-public').map(p=>p.url)};
const manifest=[];
for(const [file,url] of Object.entries(route)){
 if(file==='india.html'||file==='resources.html')continue;
 const c=cases.find(c=>file==='case-'+c.slug+'.html');const [title,description]=metadata[file]||[c.project+' — Real Estate Case Study | QDnCo',c.subtitle];
 const ctx={React,window:{Motion},location:{pathname:url,hash:''},localStorage:{getItem:()=>null},console,QD_PAGE:'/'+file,QD_ROUTES:route,QD_CASES:cases};ctx.window.React=React;vm.createContext(ctx);vm.runInContext(code+';this.QDApp=App;',ctx);
 const rendered=SSR.renderToStaticMarkup(React.createElement(ctx.QDApp));
 const canonical='https://qdnco.com'+url;const esc=s=>s.replaceAll('&','&amp;').replaceAll('"','&quot;').replaceAll('<','&lt;');
 const webpage={'@type':file.includes('contact')?'ContactPage':file.includes('about')?'AboutPage':c?'Article':'WebPage','@id':canonical+'#page',url:canonical,name:title,description,isPartOf:{'@id':'https://qdnco.com/#website'},about:{'@id':graphOrg['@id']}};
 const schemas={'@context':'https://schema.org','@graph':[graphOrg,{'@type':'WebSite','@id':'https://qdnco.com/#website',url:'https://qdnco.com/',name:'QDnCo',publisher:{'@id':graphOrg['@id']}},webpage]};
 const alternates=['index.html','dubai.html'].includes(file)?'<link rel="alternate" hreflang="en-IN" href="https://qdnco.com/"><link rel="alternate" hreflang="en-AE" href="https://qdnco.com/dubai/"><link rel="alternate" hreflang="x-default" href="https://qdnco.com/">':'';
 const meta=`<title>${esc(title)}</title><meta name="description" content="${esc(description)}"><meta name="robots" content="${file==='company-profile.html'?'noindex,follow':'index,follow,max-image-preview:large'}"><link rel="canonical" href="${canonical}">${alternates}<meta property="og:type" content="website"><meta property="og:site_name" content="QDnCo"><meta property="og:title" content="${esc(title)}"><meta property="og:description" content="${esc(description)}"><meta property="og:url" content="${canonical}"><meta property="og:image" content="https://qdnco.com/_redesign/shots/indium.jpg"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="${esc(title)}"><meta name="twitter:description" content="${esc(description)}"><meta name="twitter:image" content="https://qdnco.com/_redesign/shots/indium.jpg"><script type="application/ld+json">${JSON.stringify(schemas).replaceAll('<','\\u003c')}</script>`;
 const globals=`const QD_PAGE=${JSON.stringify('/'+file)},QD_ROUTES=${JSON.stringify(route)},QD_CASES=${JSON.stringify(cases).replaceAll('<','\\u003c')};window.QD_LEAD_ENDPOINT=${JSON.stringify(endpoint)};`;
 const analytics=`<script>if(['qdnco.com','www.qdnco.com'].includes(location.hostname)){var s=document.createElement('script');s.async=true;s.src='https://www.googletagmanager.com/gtag/js?id=G-GZE73M9Q4M';document.head.appendChild(s);window.dataLayer=window.dataLayer||[];window.gtag=function(){dataLayer.push(arguments)};gtag('js',new Date());gtag('config','G-GZE73M9Q4M',{content_group:location.pathname.startsWith('/dubai/')?'Dubai':'India'});}</script>`;
 const target=url.endsWith('/')?url+'index.html':url;
 write(out+target,`<!doctype html><html lang="en" data-theme="light"><head>${head}${meta}</head><body><div id="root">${rendered}</div><noscript><p>To send an enquiry, call <a href="tel:+918861179992">+91 88611 79992</a> or <a href="mailto:qdnco01@gmail.com">email QDnCo</a>.</p></noscript><script>${globals}</script><script src="/js/lead-capture.js"></script><script src="/_redesign/lead-adapter.js"></script><script src="/_redesign/app.js"></script>${analytics}</body></html>`);
 manifest.push({source:file,url:canonical,file:target.slice(1),staticCharacters:rendered.length,sha256:sha(read(out+target))});
}
// Preserve all published resource URLs, and add the preview resource library separately.
for(const file of ['resources.html',...fs.readdirSync(root+'/insights').filter(f=>f.endsWith('.html')).map(f=>'insights/'+f)]){
 let s=assetRewrite(read(root+'/'+file)).replaceAll('noindex,nofollow','index,follow').replaceAll(' — Private Preview','').replaceAll('Private preview','Resource library');
 for(const [from,to]of Object.entries(route))s=s.replaceAll('href="'+from+'"','href="'+to+'"');
 const target=file==='resources.html'?'/resources/index.html':'/'+file;
 s=s.replace('</head>',`<link rel="canonical" href="https://qdnco.com${target.replace(/index.html$/,'')}"></head>`);write(out+target,s);
}
let ht=read(out+'/.htaccess');
ht=ht.replace(/\(blog\|blogs\|insights\|articles\|resources\)/g,'(blog|blogs|articles)');
const aliases=Object.entries(route).filter(([f])=>!f.startsWith('case-')&&f!=='index.html').map(([f,u])=>`RewriteRule ^${f.replace('.','\\.')}$$ ${u} [R=301,L]`).join('\n');
ht=ht.replace('RewriteEngine On','RewriteEngine On\n# New-design preview aliases; no existing resource URL is removed.\n'+aliases);write(out+'/.htaccess',ht);
let sitemap=read(__dirname+'/live-sitemap.xml');for(const m of manifest){if(m.source==='company-profile.html'||sitemap.includes('<loc>'+m.url+'</loc>'))continue;sitemap=sitemap.replace('</urlset>',`<url><loc>${m.url}</loc></url>\n</urlset>`)}
for(const u of ['/resources/','/insights/',...fs.readdirSync(root+'/insights').filter(f=>f.endsWith('.html')&&f!=='index.html').map(f=>'/insights/'+f)])if(!sitemap.includes('<loc>https://qdnco.com'+u+'</loc>'))sitemap=sitemap.replace('</urlset>',`<url><loc>https://qdnco.com${u}</loc></url>\n</urlset>`);
write(out+'/sitemap.xml',sitemap);
write(out+'/llms.txt',read(__dirname+'/live-llms.txt')+'\n\n## Updated website routes\n'+manifest.filter(m=>m.source!=='company-profile.html').map(m=>'- '+m.url).join('\n')+'\n\n## Public company profiles\n'+profiles.filter(p=>p.status==='verified-public').map(p=>'- '+p.name+': '+p.url).join('\n')+'\n');
write(__dirname+'/route-manifest.json',JSON.stringify(manifest,null,2));
console.log('LOCAL ONLY:',out,manifest.length,'server-rendered pages; live content copied, no deployment.');
