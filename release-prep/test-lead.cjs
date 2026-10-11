const fs=require('fs'),vm=require('vm'),assert=require('node:assert/strict');
let posts=0,events=0;
const ctx={window:{},location:{hostname:'localhost',pathname:'/contact/',href:'http://localhost/contact/'},document:{referrer:''},FormData:class{constructor(form){return form.values}},Date,console};
vm.createContext(ctx);vm.runInContext(fs.readFileSync(__dirname+'/lead-adapter.js','utf8'),ctx);
const input={name:'LOCAL TEST',phone:'+91 9999999999',market:'Local test project',enquiryType:'Developer',service:'Meta/Google Ad Campaigns',campaignCount:'3',sameWhatsApp:'no',whatsappPhone:'+91 8888888888',preferredDate:'2026-11-01',indicativePrice:'INR 66000 per campaign/month'};
const lead=ctx.QDMapLead(input,{page:'https://qdnco.com/contact/',utm_campaign:'test'});
assert.equal(lead.project,'Local test project');assert.equal(lead.campaign_count,'3');assert.equal(lead.whatsapp_phone,'+91 8888888888');assert.equal(lead.budget,'INR 66000 per campaign/month');
assert.throws(()=>ctx.QDMapLead({...input,phone:'123'},{}));
let state;const button={disabled:false},form={dataset:{},values:Object.entries(input),querySelector:()=>button},event={currentTarget:form,preventDefault(){}};
const helper={context:()=>({page:'https://qdnco.com/contact/'}),requestId:()=> 'local-test-receipt-123',send:async()=>{posts++}};ctx.QDLeadCapture=helper;ctx.window.gtag=()=>{events++};
(async()=>{
 await ctx.window.QDSubmitEnquiry(event,s=>state=s);assert.equal(posts,0);assert.match(state,/no enquiry sent/);
 ctx.location.hostname='qdnco.com';await ctx.window.QDSubmitEnquiry(event,s=>state=s);assert.equal(posts,1);assert.equal(events,1);assert.match(state,/received/);assert.equal(button.disabled,false);
 helper.send=async()=>{throw Error('failure')};await ctx.window.QDSubmitEnquiry(event,s=>state=s);assert.equal(events,1);assert.match(state,/could not confirm/);assert.equal(button.disabled,false);
 const backend={PropertiesService:{getScriptProperties:()=>({getProperty:()=> 'test'})},console};vm.createContext(backend);vm.runInContext(fs.readFileSync(__dirname+'/lead-backend-candidate.gs','utf8'),backend);
 const clean=backend.cleanLead({...lead,request_id:'local-test-receipt-123'});assert.equal(clean.whatsapp_phone,'+91 8888888888');assert.equal(clean.service,input.service);assert.equal(clean.campaign_count,'3');assert.equal(clean.preferred_date,'2026-11-01');
 const report={passed:['new form maps to legacy required fields','extra enquiry fields survive backend normalization','local-host submission blocked','success event only after confirmed receipt','failed receipt shows retry without conversion event','invalid phone rejected'],externalRequests:0};fs.writeFileSync(__dirname+'/lead-tests.json',JSON.stringify(report,null,2));console.log(JSON.stringify(report,null,2));
})().catch(e=>{console.error(e);process.exit(1)});
