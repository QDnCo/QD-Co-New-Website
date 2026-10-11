const fs=require('fs'),vm=require('vm'),path=require('path');
const deps=path.resolve(__dirname,'../../Portfolio Website/node_modules');
const React=require(deps+'/react'),ReactDOMServer=require(deps+'/react-dom/server'),Motion=require(deps+'/framer-motion');
const {transform}=require(deps+'/sucrase');
const root=path.resolve(__dirname,'..');
let html=fs.readFileSync(root+'/index.html','utf8');
let jsx=html.match(/<script type="text\/babel">([\s\S]*?)<\/script>/)[1];
jsx=jsx.replace(/ReactDOM.createRoot[\s\S]*$/,'');
jsx=jsx.replace('const[data,setData]=useState([])','const[data,setData]=useState(QD_CASES)');
let context={React,window:{Motion},location:{pathname:'/index.html',hash:''},localStorage:{getItem:()=>null},console,QD_CASES:JSON.parse(fs.readFileSync(root+'/case-studies.json','utf8'))};
context.window.React=React;vm.createContext(context);
try{vm.runInContext(transform(jsx,{transforms:['jsx'],production:true,jsxRuntime:'classic'}).code+';this.QDApp=App;',context);let rendered=ReactDOMServer.renderToStaticMarkup(React.createElement(context.QDApp));fs.writeFileSync(__dirname+'/test-render.html',rendered);console.log('SSR OK',rendered.length)}catch(e){console.error(e);process.exit(1)}
