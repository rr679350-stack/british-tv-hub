function toggleSiteSearch(){
  var box = document.getElementById('nav-search-box');
  if(!box) return;
  var showing = box.style.display !== 'none';
  box.style.display = showing ? 'none' : 'block';
  if(!showing){
    var input = document.getElementById('nav-search-input');
    if(input){ input.value=''; }
    var results = document.getElementById('nav-search-results');
    if(results){ results.innerHTML=''; }
    setTimeout(function(){ if(input){ input.focus(); } }, 10);
  }
}
function filterSiteSearch(q){
  var results = document.getElementById('nav-search-results');
  if(!results) return;
  q = q.trim().toLowerCase();
  if(!q){ results.innerHTML=''; return; }
  var index = window.SITE_SEARCH_INDEX || [];
  var matches = index.filter(function(p){ return p.title.toLowerCase().indexOf(q) !== -1; }).slice(0,8);
  if(matches.length===0){
    results.innerHTML = '<div class="nav-search-empty">No matches found</div>';
    return;
  }
  results.innerHTML = matches.map(function(p){
    return '<a href="'+p.url+'">'+p.title+'</a>';
  }).join('');
}
function handleSiteSearchKey(e){
  if(e.key==='Enter'){
    var first = document.querySelector('#nav-search-results a');
    if(first){ window.location.href = first.getAttribute('href'); }
  }
  if(e.key==='Escape'){ toggleSiteSearch(); }
}
document.addEventListener('click', function(e){
  var box = document.getElementById('nav-search-box');
  var toggle = document.querySelector('.nav-search-toggle');
  if(!box || box.style.display==='none') return;
  if(!box.contains(e.target) && e.target!==toggle){
    box.style.display='none';
  }
});

function addVillageMurderFeature(){
  if(location.pathname !== '/quizzes-and-games.html' && location.pathname !== '/quizzes-and-games') return;

  var intro = document.querySelector('.hero-intro');
  if(intro){
    intro.textContent = 'Every quiz, game and interactive mystery on British TV Hub, gathered in one place — build a mystery, test your British TV knowledge, or become the detective yourself.';
  }

  var pageBody = document.querySelector('.page-body');
  if(!pageBody || document.getElementById('village-murder-feature')) return;

  var feature = document.createElement('section');
  feature.id = 'village-murder-feature';
  feature.setAttribute('aria-labelledby','village-murder-title');
  feature.style.cssText = 'max-width:1100px;margin:36px auto 42px;background:linear-gradient(145deg,#202a3d,#2e3950);border:1px solid rgba(201,168,76,.45);border-radius:14px;padding:clamp(24px,4vw,42px);box-shadow:0 16px 40px rgba(0,0,0,.16);';
  feature.innerHTML = ''+
    '<div style="font-family:Raleway,sans-serif;font-size:11px;letter-spacing:2px;text-transform:uppercase;color:#c9a96e;margin-bottom:10px;">Featured Mystery Game</div>'+
    '<h2 id="village-murder-title" style="font-family:Playfair Display,serif;font-size:clamp(2rem,4vw,3rem);line-height:1.12;color:#f0e8d4;margin:0 0 8px;">Murder at the <em style="color:#d9bd86;">Village Fête</em></h2>'+
    '<p style="font-family:Crimson Text,serif;font-size:20px;line-height:1.55;color:#e7dec9;margin:0 0 20px;max-width:820px;">You’ve watched enough British mysteries — now it’s your turn to solve one.</p>'+
    '<p style="font-size:16px;line-height:1.75;color:#c9c2b4;margin:0 0 18px;max-width:900px;">A village fête in Bellweather-on-Wye turns deadly when chairman Arthur Bell is found behind the prize marquee. Four suspects had reasons to want him silenced. One of them is lying.</p>'+
    '<p style="font-size:16px;line-height:1.75;color:#c9c2b4;margin:0 0 22px;max-width:900px;"><strong style="color:#f0e8d4;">The Village Murder Case File</strong> is a 10-page printable whodunit with four suspects, witness statements, evidence and clues, an illustrated village map, a crime timeline, detective notes, a final accusation page, and the complete solution.</p>'+
    '<div style="display:flex;gap:10px;flex-wrap:wrap;margin:0 0 26px;">'+
      '<span style="font-family:Raleway,sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#e7dec9;border:1px solid rgba(201,168,76,.35);padding:8px 11px;border-radius:999px;">10-page printable</span>'+
      '<span style="font-family:Raleway,sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#e7dec9;border:1px solid rgba(201,168,76,.35);padding:8px 11px;border-radius:999px;">Solo or group play</span>'+
      '<span style="font-family:Raleway,sans-serif;font-size:11px;letter-spacing:1px;text-transform:uppercase;color:#e7dec9;border:1px solid rgba(201,168,76,.35);padding:8px 11px;border-radius:999px;">Instant download</span>'+
    '</div>'+
    '<a href="https://cozytvcompanion.etsy.com/listing/4584482709" target="_blank" rel="noopener" style="display:inline-block;background:#c9a96e;color:#1a2135;text-decoration:none;font-family:Raleway,sans-serif;font-size:12px;font-weight:700;letter-spacing:1.4px;text-transform:uppercase;padding:13px 22px;border-radius:3px;">Solve the Mystery →</a>'+
    '<div style="font-family:Crimson Text,serif;font-size:15px;color:#aaa394;margin-top:14px;">Perfect for a cosy evening at home, solo sleuthing, game night, or sharing with another armchair detective.</div>';

  var first = pageBody.firstElementChild;
  pageBody.insertBefore(feature, first || null);
}

if(document.readyState === 'loading'){
  document.addEventListener('DOMContentLoaded', addVillageMurderFeature);
} else {
  addVillageMurderFeature();
}

