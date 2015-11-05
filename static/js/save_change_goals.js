$(document).ready(function(){
    $('input.goal').change(function(){
        var url = Urls['match:save_changes']($(this).data('match_id'));
        var data = {
                'goals': $(this).val(),
                'team': $(this).data('team'),
                'csrfmiddlewaretoken': $("[name='csrfmiddlewaretoken']").val()
            };
        var self = this;
        $.ajax({
            url: url,
            data: data,
            method: 'POST',
            success: function(response){
                $(self).parent().html($(self).val());
            }
        });
    });
});