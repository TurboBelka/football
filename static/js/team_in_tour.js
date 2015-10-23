$(document).ready(function(){
    $("#my_select").change(function(){

        var url = $('option:selected', this).data('create_url');
        var url1 = $('option:selected', this).data('url');
        var url_gen = $('option:selected', this).data('url_gen');
        var mode = $('option:selected', this).data('tour_mode');
        console.log(mode);
        if (mode == 1){
            $('#create_team').attr("disabled", true);
            $('#generate_team').attr("disabled", true);
            $('#create_team').attr("href", "");
            $('#generate_team').attr("href", "");
        }else{
            $('#create_team').attr("disabled", false);
            $('#generate_team').attr("disabled", false);
            $('#create_team').attr("href", url);
            $('#generate_team').attr("href", url_gen);
        }
        $.ajax({
            url: url1,
            method: 'get',
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
    $("#my_select").val($(this).data('tour_id'));
    $("#my_select").change();
});
