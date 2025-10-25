window.addEventListener('load', function() {
  const headerMenu = document.querySelector('.header-menu');
  const menuOverlay = document.querySelector('.menu-overlay');
  const menuToggle = document.querySelector('.menu-toggle');
  const menuClose = document.querySelector('.menu-close');
  const submenuToggles = document.querySelectorAll('.submenu');
  const submenuLinks = document.querySelectorAll('.submenu ul a');

  let menuShowing = false;

  menuToggle.addEventListener('click', function() {
    if (menuShowing) {
      menuShowing = false;
      headerMenu.classList.remove('show');
      menuOverlay.classList.remove('menu-showing');
    } else {
      menuShowing = true;
      headerMenu.classList.add('show');
      menuOverlay.classList.add('menu-showing');
    }
  });

  menuClose.addEventListener('click', function() {
    menuShowing = false;
    headerMenu.classList.remove('show');
    menuOverlay.classList.remove('menu-showing');
  });

  menuOverlay.addEventListener('click', function() {
    menuShowing = false;
    headerMenu.classList.remove('show');
    menuOverlay.classList.remove('menu-showing');
  });

  submenuToggles.forEach(toggle => {
    toggle.addEventListener('click', function(event) {
      event.preventDefault();
      toggle.classList.toggle('show');
    });
  });

  submenuLinks.forEach(link => {
    link.addEventListener('click', function(event) {
      event.stopPropagation();
    });
  });
});
