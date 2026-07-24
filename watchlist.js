(function(){
  var KEY = 'btvh_watchlist_v1';
  var LABELS = { want: 'Want to Watch', watching: 'Watching', finished: 'Finished' };

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
    var toggle = el.querySelector('.wl-dd-toggle');
    var label = el.querySelector('.wl-dd-label');
    if(!toggle || !label) return;
    if(current && LABELS[current]){
      label.textContent = LABELS[current];
      toggle.classList.add('active');
    } else {
      label.textContent = 'Add to Watch List';
      toggle.classList.remove('active');
    }
    var items = el.querySelectorAll('.wl-dd-item');
    for(var i = 0; i < items.length; i++){
      items[i].classList.toggle('active', items[i].getAttribute('data-status') === current);
    }
  }

  function closeAllMenus(except){
    var open = document.querySelectorAll('.wl-dropdown.open');
    for(var i = 0; i < open.length; i++){
      if(open[i] !== except){ open[i].classList.remove('open'); }
    }
  }

  function init(){
    var groups = document.querySelectorAll('.wl-dropdown[data-slug]');
    for(var g = 0; g < groups.length; g++){
      (function(el){
        paint(el);
        var toggle = el.querySelector('.wl-dd-toggle');
        if(toggle){
          toggle.addEventListener('click', function(e){
            e.stopPropagation();
            var wasOpen = el.classList.contains('open');
            closeAllMenus();
            if(!wasOpen){ el.classList.add('open'); }
          });
        }
        var items = el.querySelectorAll('.wl-dd-item');
        for(var i = 0; i < items.length; i++){
          items[i].addEventListener('click', function(e){
            e.stopPropagation();
            var slug = el.getAttribute('data-slug');
            var val = this.getAttribute('data-status');
            var current = getStatus(slug);
            setStatus(slug, current === val ? null : val);
            paint(el);
            el.classList.remove('open');
          });
        }
      })(groups[g]);
    }
    document.addEventListener('click', function(){ closeAllMenus(); });
    document.addEventListener('keydown', function(e){
      if(e.key === 'Escape'){ closeAllMenus(); }
    });
  }

  window.BTVHWatchlist = { getAll: getAll, getStatus: getStatus, setStatus: setStatus, paint: paint, init: init };

  if(document.readyState === 'loading'){
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
