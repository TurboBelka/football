$(document).ready(function(){
    $("#my_select").change(function(){
    var tour_id = {'my_select': $(this).val()};
        $.ajax({
            url: $(this).data('url'),
            method: 'get',
            data: tour_id,
            success: function(obj){
                console.log(obj[0]['fields']['name']);
                var o=[{name: '1231321651'}];
                var t = $('#my_templ2').tmpl(o);//.appendTo('#teams');
                console.log(t);
            },
            error: function(xhr, status, error){
               alert(error);
            }
        });
    });
});

