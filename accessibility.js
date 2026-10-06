/* Small enhancements for third-party decoration and repeated disclosures. */
(function () {
  function hideChatSpinner() {
    document.querySelectorAll('#chatbase-bubble-window svg').forEach(function (icon) {
      if (icon.querySelector('.chatbase-spinner')) {
        icon.setAttribute('aria-hidden', 'true');
        icon.setAttribute('focusable', 'false');
      }
    });
  }
  function labelFloatingChatLandmark() {
    document.querySelectorAll('body > div[style*="position: fixed"], body > div[style*="position:fixed"]').forEach(function (box) {
      if (box.id === 'backToTop' || box.hasAttribute('role')) return;
      if (box.querySelector('iframe[id*="chatbase"], [id*="chatbase"], iframe[src*="chatbase"]')) {
        box.setAttribute('role', 'region');
        box.setAttribute('aria-label', 'Chat support');
      }
    });
  }
  labelFloatingChatLandmark();
  new MutationObserver(labelFloatingChatLandmark).observe(document.body, { childList: true, subtree: true });

  function labelSupportWidget() {
    var button = document.getElementById('bmc-wbtn');
    if (button && !button.hasAttribute('role')) {
      button.setAttribute('role', 'region');
      button.setAttribute('aria-label', 'Support British TV Hub');
    }
    if (button && button.parentElement && button.parentElement.tagName === 'DIV' && !button.parentElement.hasAttribute('role')) {
      button.parentElement.setAttribute('role', 'region');
      button.parentElement.setAttribute('aria-label', 'Support options');
    }
  }
  labelSupportWidget();
  new MutationObserver(labelSupportWidget).observe(document.body, { childList: true, subtree: true });
  function improveFormAccessibility(root) {
    var scope = root && root.querySelectorAll ? root : document;
    scope.querySelectorAll('input:not([type="hidden"]), select, textarea').forEach(function (control) {
      var hasLabel = (control.labels && control.labels.length) ||
        control.hasAttribute('aria-label') || control.hasAttribute('aria-labelledby') ||
        control.hasAttribute('title');
      if (!hasLabel) {
        var fallback = control.getAttribute('placeholder') || control.getAttribute('name') || control.id || '';
        fallback = fallback.replace(/[-_]+/g, ' ').replace(/\b\w/g, function (m) { return m.toUpperCase(); }).trim();
        if (fallback) control.setAttribute('aria-label', fallback);
      }
    });
    ['nav-search-results', 'result-wrap'].forEach(function (id) {
      var region = document.getElementById(id);
      if (region && !region.hasAttribute('aria-live')) {
        region.setAttribute('aria-live', 'polite');
        region.setAttribute('aria-atomic', 'false');
      }
    });
  }
  improveFormAccessibility(document);
  new MutationObserver(function (mutations) {
    mutations.forEach(function (mutation) {
      mutation.addedNodes.forEach(function (node) {
        if (node.nodeType === 1) improveFormAccessibility(node);
      });
    });
  }).observe(document.body, { childList: true, subtree: true });
  function labelVideoLinks() {
    document.querySelectorAll('iframe[src*="youtube.com/embed/"], iframe[src*="youtube-nocookie.com/embed/"]').forEach(function (frame) {
      if (!frame.getAttribute('title')) {
        var nearbyHeading = frame.closest('section, article, div') && frame.closest('section, article, div').querySelector('h1, h2, h3');
        frame.setAttribute('title', nearbyHeading ? nearbyHeading.textContent.trim() + ' video' : 'British TV Hub video');
      }

      // Explicitly prevent autoplay, even if an old embed URL contains autoplay=1.
      if (!frame.dataset.hubAutoplayChecked) {
        try {
          var embedUrl = new URL(frame.src, window.location.href);
          var changed = false;
          if (embedUrl.searchParams.get('autoplay') !== '0') {
            embedUrl.searchParams.set('autoplay', '0');
            changed = true;
          }
          // Ask YouTube to display captions by default when captions exist.
          if (embedUrl.searchParams.get('cc_load_policy') !== '1') {
            embedUrl.searchParams.set('cc_load_policy', '1');
            changed = true;
          }
          if (!embedUrl.searchParams.get('cc_lang_pref')) {
            embedUrl.searchParams.set('cc_lang_pref', 'en');
            changed = true;
          }
          if (changed) frame.src = embedUrl.toString();
        } catch (e) {}
        frame.dataset.hubAutoplayChecked = 'true';
      }

      var wrapper = frame.parentElement;
      if (!wrapper) return;
      var caption = wrapper.nextElementSibling;

      // Guarantee a visible Watch on YouTube button immediately below every embed.
      if (!caption || !caption.classList.contains('hub-video-caption')) {
        caption = document.createElement('p');
        caption.className = 'hub-video-caption';
        wrapper.insertAdjacentElement('afterend', caption);
      }

      var link = caption.querySelector('a');
      if (!link) {
        link = document.createElement('a');
        link.className = 'hub-youtube-button';
        link.target = '_blank';
        link.rel = 'noopener';
        caption.appendChild(link);
      }

      var videoTitle = frame.title.replace(/\s+video$/i, '').trim() || 'British TV Hub video';
      var embedMatch = frame.src.match(/\/embed\/([^?&/]+)/);
      var watchUrl = embedMatch ? 'https://www.youtube.com/watch?v=' + encodeURIComponent(embedMatch[1]) : 'https://www.youtube.com/';
      link.href = watchUrl;
      link.textContent = 'Watch ' + videoTitle + ' on YouTube';
      link.setAttribute('aria-label', 'Watch ' + videoTitle + ' on YouTube (opens in a new tab)');
    });
  }
  labelVideoLinks();
  new MutationObserver(labelVideoLinks).observe(document.body, { childList: true, subtree: true });
  hideChatSpinner();
  new MutationObserver(hideChatSpinner).observe(document.body, { childList: true, subtree: true });
  document.querySelectorAll('.hub-skip-link').forEach(function (link) {
    link.addEventListener('click', function () {
      var target = document.getElementById(link.hash.slice(1));
      if (target) target.focus();
    });
  });
  // Let keyboard users dismiss open navigation/search controls with Escape.
  document.addEventListener('keydown', function (event) {
    if (event.key !== 'Escape') return;

    var discover = document.getElementById('nav-discover-menu');
    var discoverToggle = document.querySelector('.nav-dropdown-toggle');
    if (discover && discover.style.display !== 'none') {
      discover.style.display = 'none';
      if (discoverToggle) {
        discoverToggle.setAttribute('aria-expanded', 'false');
        discoverToggle.focus();
      }
      event.preventDefault();
      return;
    }

    var searchBox = document.getElementById('nav-search-box');
    var searchToggle = document.querySelector('.nav-search-toggle');
    if (searchBox && searchBox.style.display !== 'none') {
      searchBox.style.display = 'none';
      if (searchToggle) {
        searchToggle.setAttribute('aria-expanded', 'false');
        searchToggle.focus();
      }
      event.preventDefault();
    }
  });

  var mobileToggle = document.getElementById('nav-hamburger-btn');
  var navigation = document.querySelector('nav.site-nav-std');
  if (mobileToggle && navigation) {
    document.addEventListener('keydown', function (event) {
      var discover = document.getElementById('nav-discover-menu');
      if (event.defaultPrevented || (discover && discover.style.display !== 'none' && discover.contains(document.activeElement))) return;
      if (event.key === 'Escape' && navigation.classList.contains('mobile-menu-open') && navigation.contains(document.activeElement)) {
        navigation.classList.remove('mobile-menu-open');
        mobileToggle.setAttribute('aria-expanded', 'false');
        mobileToggle.focus();
        event.preventDefault();
      }
    });
  }
})();
