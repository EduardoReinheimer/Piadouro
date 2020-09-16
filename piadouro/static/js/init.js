(function($) {
    $(function() {

        $('.sidenav').sidenav();
        $(".dropdown-trigger").dropdown();

    }); // end of document ready
})(jQuery); // end of jQuery name space

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
    var piado_forms = document.querySelectorAll('.piar');

    piado_forms.forEach(piado_form => {
        piado_form.addEventListener('keypress', function (event) {
            if(event.key == 'Enter'){
                event.preventDefault();
                event.stopPropagation();
                piado_form.submit();
            }
        })
    });

    //Modal
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, {});
  });