/* Project specific Javascript goes here. */

$(document).keydown(function(e){
    // Focus search bar when `/` is pressed
    var forward_slash = 191;
    var skip_types = ['input', 'textarea']
    if (skip_types.indexOf(e.target.tagName.toLowerCase()) != -1) return;
    if (e.keyCode == forward_slash) {
       $('input[name=q]').focus();
       return false;
    }
});
