/* Candidate only. Preview hosts never submit or send analytics. */
window.QDSubmitEnquiry=async function(event,setState){
 event.preventDefault(); const form=event.currentTarget;
 if(form.dataset.sending==='true')return;
 if(!['qdnco.com','www.qdnco.com'].includes(location.hostname)) {setState('Local release check: no enquiry sent.');return;}
 const values=Object.fromEntries(new FormData(form));
 const lead=QDMapLead(values, QDLeadCapture.context(location.href,document.referrer));
 const signature=JSON.stringify(lead);
 if(form.dataset.signature!==signature){form.dataset.signature=signature;form.dataset.receipt=QDLeadCapture.requestId();}
 lead.request_id=form.dataset.receipt;lead.submitted=new Date().toISOString();
 form.dataset.sending='true';const button=form.querySelector('button[type="submit"]');button.disabled=true;setState('Sending your enquiry…');
 try{await QDLeadCapture.send(window.QD_LEAD_ENDPOINT,lead);setState('Enquiry received. Our team will contact you. A call time is not reserved until confirmed.');
 if(window.gtag)window.gtag('event','generate_lead',{form_name:'phase0',site_region:location.pathname.startsWith('/dubai/')?'dubai':'india'});
 }catch(error){setState('We could not confirm receipt. Your details are still here. Please retry or email qdnco01@gmail.com.');}
 finally{form.dataset.sending='false';button.disabled=false;}
};
function QDMapLead(v,context){
 const phone=String(v.phone||'').trim(),digits=phone.replace(/\D/g,'');
 if(digits.length<8||digits.length>15||!/^[+0-9\s().-]+$/.test(phone))throw Error('Invalid phone');
 return {...context,name:v.name,phone,project:v.market||v.enquiryContext||v.enquiryType,catchment:v.enquiryType,budget:v.indicativePrice||'Custom scope requested',enquiry_type:v.enquiryType,service:v.service,other_service:v.otherService||'',campaign_count:v.campaignCount||'',project_count:v.projectCount||'',whatsapp_preference:v.sameWhatsApp,whatsapp_phone:v.sameWhatsApp==='no'?v.whatsappPhone:v.sameWhatsApp==='yes'?phone:'',preferred_date:v.preferredDate||'',enquiry_context:v.enquiryContext||''};
}
