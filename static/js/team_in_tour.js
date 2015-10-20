$(document).ready(function(){
    $("#my_select").change(function(){
    var tour_id = {'my_select': $(this).val()};
        $.ajax({
            url: $(this).data('url'),
            method: 'get',
            data: tour_id,
            success: function(obj){
                var tmp = $.templates('#my_templ');
                var htmlOutput = tmp.render(obj);
                $('#teams').html(htmlOutput);
            },
            error: function(xhr, status, error){
               alert(error);
            }
        });
    });
});

$(document).ready(function(){
    $("#my_select").change();
});
