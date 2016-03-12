/* Project specific Javascript goes here. */

$(document).keydown(function(e){
    // Focus search bar when `/` is pressed
    var forward_slash = 191;
    if (e.keyCode == forward_slash) {
       $('input[name=q]').focus();
       return false;
    }
});
