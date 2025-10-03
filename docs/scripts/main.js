window.onload = function() {
  const headerMenu = document.querySelector('.header-menu');
  const menuOverlay = document.querySelector('.menu-overlay');
  const menuToggle = document.querySelector('.menu-toggle');
  const menuClose = document.querySelector('.menu-close');

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

  menuOverlay.addEventListener('click', function(){
    menuShowing = false;
    headerMenu.classList.remove('show');
    menuOverlay.classList.remove('menu-showing');
  });
};
