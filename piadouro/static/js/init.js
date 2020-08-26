(function($) {
    $(function() {

        $('.sidenav').sidenav();
        $(".dropdown-trigger").dropdown();

    }); // end of document ready
})(jQuery); // end of jQuery name space

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('select');
    var instances = M.FormSelect.init(elems, {});
  });