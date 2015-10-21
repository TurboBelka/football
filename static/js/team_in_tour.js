$(document).ready(function(){
    $("#my_select").change(function(){
    var url = $('option:selected', this).data('create_url');
    var url1 = $('option:selected', this).data('url');
    var url_gen = $('option:selected', this).data('url_gen');
        $.ajax({
            url: url1,
            method: 'get',
            success: function(obj){
                var tmp = $.templates('#my_templ');
                var htmlOutput = tmp.render(obj);
                $('#teams').html(htmlOutput);
                $('#create_team').attr("href", url);
                $('#generate_team').attr("href", url_gen);
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
