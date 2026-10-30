/* Form konsultasi & tiket support (dari form tiket Altora).
   Sentra belum memakai server tiket, jadi isian divalidasi di browser lalu dikirim sebagai pesan WhatsApp
   ke tim Sentra. Teks mengikuti bahasa halaman (window.SENTRA_UI.ticket dari generator). */
(()=>{
  const form=document.querySelector('[data-ticket-form]');
  if(!form)return;
  const WA='628170822552';
  const D={
    sending:'Membuka WhatsApp…',submit:'Kirim via WhatsApp',
    generic:'Periksa kembali isian yang diberi tanda merah, lalu kirim ulang.',
    required:'Tolong isi {label}.',email:'Masukkan alamat email yang valid, misalnya nama@email.com.',
    min:'{label} masih terlalu singkat. Tambahkan {count} karakter lagi (minimal 15 karakter).',
    ok:'WhatsApp terbuka dengan pesan Anda. Tekan kirim di WhatsApp untuk menyelesaikan.',
    remaining:'{count} karakter lagi agar konteksnya cukup jelas.',ready:'Konteks sudah cukup jelas untuk dikirim.',
    intro:'Halo Sentra Technology, saya mengirim permintaan dari website:',
    labels:{name:'nama',email:'email',whatsapp:'nomor WhatsApp',city:'kota atau lokasi',service:'kebutuhan',needs:'cerita kebutuhan'},
    keys:{name:'Nama',email:'Email',whatsapp:'WhatsApp',city:'Lokasi',organization:'Organisasi',service:'Kebutuhan',needs:'Cerita',timeline:'Target waktu',notes:'Catatan'}
  };
  const U=(window.SENTRA_UI&&window.SENTRA_UI.ticket)||{};
  const copy=Object.assign({},D,U,{labels:Object.assign({},D.labels,U.labels||{}),keys:Object.assign({},D.keys,U.keys||{})});
  const fmt=(t,o)=>t.replace(/\{(\w+)\}/g,(_,k)=>o[k]);

  const fields=[
    {name:'name',min:2},{name:'email',email:true},{name:'whatsapp',min:8},
    {name:'city',min:2},{name:'service'},{name:'needs',min:15},
  ].filter(f=>form.elements[f.name]);
  const out=form.querySelector('[data-ticket-result]');
  const btn=form.querySelector('button[type="submit"]');
  const needs=form.elements.needs;
  const counter=form.querySelector('[data-needs-counter]');

  function fieldErrorElement(input){
    const label=input.closest('label');
    let error=label.querySelector('[data-field-error]');
    if(!error){
      error=document.createElement('span');
      error.className='field-error';
      error.dataset.fieldError='';
      error.setAttribute('role','alert');
      label.append(error);
    }
    return error;
  }
  function clearFieldError(input){
    input.removeAttribute('aria-invalid');
    const error=input.closest('label')?.querySelector('[data-field-error]');
    if(error)error.textContent='';
  }
  function showFieldError(input,message){
    input.setAttribute('aria-invalid','true');
    fieldErrorElement(input).textContent=message;
  }
  function validateField(field){
    const input=form.elements[field.name];
    const value=String(input.value||'').trim();
    const label=copy.labels[field.name]||field.name;
    let message='';
    if(!value)message=fmt(copy.required,{label});
    else if(field.email&&!input.validity.valid)message=copy.email;
    else if(field.min&&value.length<field.min)message=fmt(copy.min,{label:label.charAt(0).toUpperCase()+label.slice(1),count:field.min-value.length});
    if(message)showFieldError(input,message);else clearFieldError(input);
    return !message;
  }
  function updateNeedsCounter(){
    if(!needs||!counter)return;
    const remaining=Math.max(0,15-String(needs.value||'').trim().length);
    counter.textContent=remaining?fmt(copy.remaining,{count:remaining}):copy.ready;
    counter.classList.toggle('ready',remaining===0);
  }
  fields.forEach(field=>{
    const input=form.elements[field.name];
    input.addEventListener('input',()=>{if(input.getAttribute('aria-invalid')==='true')validateField(field);if(field.name==='needs')updateNeedsCounter()});
    input.addEventListener('change',()=>validateField(field));
    input.addEventListener('blur',()=>validateField(field));
  });
  updateNeedsCounter();

  function message(){
    const lines=[copy.intro];
    const tag=form.dataset.ticketTag;if(tag)lines.unshift(tag);
    lines.push('');
    ['name','organization','email','whatsapp','city','service','needs','timeline','notes'].forEach(k=>{
      const el=form.elements[k];if(!el)return;
      let v=String(el.value||'').trim();
      if(el.tagName==='SELECT'&&el.selectedIndex>0)v=el.options[el.selectedIndex].text;
      if(v)lines.push(copy.keys[k]+': '+v);
    });
    return lines.join('\n');
  }

  form.addEventListener('submit',event=>{
    event.preventDefault();
    out.className='form-result';
    out.textContent='';
    const invalid=fields.filter(field=>!validateField(field));
    if(invalid.length){
      out.className='form-result error';
      out.textContent=copy.generic;
      form.elements[invalid[0].name].focus();
      return;
    }
    btn.disabled=true;
    btn.textContent=copy.sending;
    window.open('https://wa.me/'+WA+'?text='+encodeURIComponent(message()),'_blank','noopener');
    out.className='form-result success';
    out.textContent=copy.ok;
    setTimeout(()=>{btn.disabled=false;btn.textContent=copy.submit},1200);
  });
})();
