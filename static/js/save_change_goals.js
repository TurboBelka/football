$(document).ready(function(){


    $('input.goal').change(function(){
        console.log(123);
        var url = Urls['match:save_changes']($(this).data('match_id'));
        var data = {
                'goals': $(this).val(),
                'team': $(this).data('team'),
                'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
            };
        $.ajax({
            url: url,
            data: data,
            method: 'POST',
            success: function(response){
//                window.location.replace(response);
            }
        });
    });
});