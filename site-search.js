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
  var words = q.replace(/[‘’']/g,'').split(/\s+/).filter(Boolean);
  var scored = [];
  index.forEach(function(p){
    var title = p.title.toLowerCase().replace(/[‘’']/g,'');
    var hay = title + ' ' + p.url.toLowerCase().replace(/[\/\-\.#]/g,' ');
    for(var i=0;i<words.length;i++){ if(hay.indexOf(words[i]) === -1) return; }
    var score = title.indexOf(q) === 0 ? 0 : (title.indexOf(q) !== -1 ? 1 : 2);
    if(p.url.indexOf('/shows/') === 0) score -= 0.5;
    scored.push({p:p, s:score});
  });
  scored.sort(function(a,b){ return a.s - b.s; });
  var matches = scored.slice(0,10).map(function(x){ return x.p; });
  if(matches.length===0){
    results.innerHTML = '<div class="nav-search-empty">No matches found</div>';
    return;
  }
  results.innerHTML = matches.map(function(p){
    var t = p.title.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
    return '<a href="'+p.url+'">'+t+'</a>';
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
  var old = document.getElementById('village-murder-feature');
  if(old) old.remove();
  var pageBody = document.querySelector('.page-body');
  if(!pageBody) return;
  var playHeading = null;
  var headings = pageBody.querySelectorAll('h2');
  for(var i=0;i<headings.length;i++){
    if(headings[i].textContent.replace(/\s+/g,' ').trim() === 'Play Along'){
      playHeading = headings[i];
      break;
    }
  }
  if(!playHeading || !playHeading.parentElement) return;
  var feature = document.createElement('a');
  feature.id = 'village-murder-feature';
  feature.href = 'https://cozytvcompanion.etsy.com/listing/4584482709';
  feature.target = '_blank';
  feature.rel = 'noopener';
  feature.setAttribute('aria-label','Murder at the Village Fête printable mystery game on Etsy');
  feature.style.cssText = 'display:block;max-width:300px;margin:8px 0 24px;text-decoration:none;';
  feature.innerHTML = '<img src="/village-murder-fete-cover.jpg?v=3" alt="Murder at the Village Fête printable mystery game" style="display:block;width:100%;height:auto;border-radius:10px;border:1px solid rgba(201,168,76,.35);box-shadow:0 8px 22px rgba(0,0,0,.18);">' +
    '<div style="font-family:Raleway,sans-serif;font-size:10px;font-weight:700;letter-spacing:1px;text-transform:uppercase;color:#c9a96e;margin-top:8px;">Featured Mystery Game · Solve the Mystery →</div>';
  var playWrap = playHeading.parentElement;
  var grid = playWrap.nextElementSibling;
  if(grid){
    pageBody.insertBefore(feature, grid);
  } else {
    pageBody.appendChild(feature);
  }
}

if(document.readyState === 'loading'){
  document.addEventListener('DOMContentLoaded', addVillageMurderFeature);
} else {
  addVillageMurderFeature();
}

