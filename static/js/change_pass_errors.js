$(document).ready(function(){
    $('#my_form').submit(function(eventObj){
        eventObj.preventDefault();
        var elem_of_data = $('#my_form').serialize();
        var method = $('#my_form').attr('method');
        var action = $('#my_form').attr('action');
        $.ajax({
            url: action,
            method: method,
            data: elem_of_data,
            error: function(xhr, status, error){
               alert(error);
               },
            success: function(text){
                for(var key in text){
                    $('.help-block').text(text[key]);
                    $('[name='+key+']').parent().addClass('has-error');
                }
            }
        });
    });

    $('#all_tours').change(function(){
        var url = Urls['index:vote']($('#all_tours option:selected').data('tour_id'))
        $('#next_step').attr('href', url);
    });
    if($('#all_tours option').length == 1){
        $('#all_tours').change();
    }
});

