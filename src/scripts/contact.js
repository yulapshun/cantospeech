window.addEventListener('load', function() {
  const form =  document.querySelector('#contactForm');
  const formStatusContainer = document.querySelector('.form-submit-status');

  form.addEventListener('submit', function(event) {
    event.preventDefault();
    fetch(event.target.action, {
      method: 'POST',
      body: new FormData(event.target)
    }).then(response => {
      if (!response.ok) {
        formStatusContainer.classList.add('error');
        formStatusContainer.innerHTML = 'Something went wrong. Please try againg later.';
        return;
      }

      form.querySelectorAll('input, textarea').forEach(a => a.value = '');
      formStatusContainer.classList.remove('error');
      formStatusContainer.innerHTML = 'Thank you for your message! We will get back to you soon.';
    })
  });
});
