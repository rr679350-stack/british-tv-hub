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

// Compact nav on scroll
(function(){
  var nav = document.querySelector('nav.site-nav-std');
  if(!nav) return;
  var threshold = 24;
  function onScroll(){
    if(window.scrollY > threshold){
      nav.classList.add('nav-compact');
    } else {
      nav.classList.remove('nav-compact');
    }
  }
  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
