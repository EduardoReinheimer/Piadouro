document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
    var comentario_forms = document.querySelectorAll('.piar');
    var clickable_icons = document.querySelectorAll('i[href]');
  
    comentario_forms.forEach(comentario_form => {
      comentario_form.addEventListener('submit', function (event) {
        if (event.target.querySelector('textarea').value === '') {
          M.toast({html: 'Escreva alguma coisa vacilão!'});
          event.stopPropagation();
          event.preventDefault();
        }
      });
      comentario_form.addEventListener('keypress', function (event) {
        if(event.key === 'Enter'){
          event.preventDefault();
          event.stopPropagation();
          comentario_form.submit();
        }
      });
    });
  
    clickable_icons.forEach(icon => {
      icon.addEventListener('click', event => {
        location.href = target.getAttribute('href');
      })
    })

    // Modal
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {});
  
    // Materialize Jquery
    $('.sidenav').sidenav();
    $(".dropdown-trigger").dropdown();
  });