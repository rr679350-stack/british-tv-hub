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
  hideChatSpinner();
  new MutationObserver(hideChatSpinner).observe(document.body, { childList: true, subtree: true });
  document.querySelectorAll('.hub-skip-link').forEach(function (link) {
    link.addEventListener('click', function () {
      var target = document.getElementById(link.hash.slice(1));
      if (target) target.focus();
    });
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
