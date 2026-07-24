(function(){
  var KEY = 'btvh_watchlist_v1';

  function getAll(){
    try {
      var raw = localStorage.getItem(KEY);
      return raw ? JSON.parse(raw) : {};
    } catch(e){
      return {};
    }
  }

  function getStatus(slug){
    return getAll()[slug] || null;
  }

  function setStatus(slug, status){
    var all = getAll();
    if(status){
      all[slug] = status;
    } else {
      delete all[slug];
    }
    try {
      localStorage.setItem(KEY, JSON.stringify(all));
    } catch(e){}
    document.dispatchEvent(new CustomEvent('btvh:watchlist-change', { detail: { slug: slug, status: status } }));
  }

  function paint(el){
    var slug = el.getAttribute('data-slug');
    var current = getStatus(slug);
    var btns = el.querySelectorAll('.wl-btn');
    for(var i = 0; i < btns.length; i++){
      var btn = btns[i];
      var isActive = current === btn.getAttribute('data-status');
      btn.classList.toggle('active', isActive);
      btn.setAttribute('aria-pressed', isActive ? 'true' : 'false');
    }
  }

  function init(){
    var groups = document.querySelectorAll('.wl-buttons[data-slug]');
    for(var g = 0; g < groups.length; g++){
      (function(el){
        paint(el);
        var btns = el.querySelectorAll('.wl-btn');
        for(var i = 0; i < btns.length; i++){
          btns[i].addEventListener('click', function(){
            var slug = el.getAttribute('data-slug');
            var val = this.getAttribute('data-status');
            var current = getStatus(slug);
            setStatus(slug, current === val ? null : val);
            paint(el);
          });
        }
      })(groups[g]);
    }
  }

  window.BTVHWatchlist = { getAll: getAll, getStatus: getStatus, setStatus: setStatus, paint: paint, init: init };

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
