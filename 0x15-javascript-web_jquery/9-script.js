$(document).ready(function() {
    $.ajax ({
        url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
        type: 'GET',
        datatype: 'json',
        success: function(data){
            $('#hello').text(data.hello);
        }
    });
});
