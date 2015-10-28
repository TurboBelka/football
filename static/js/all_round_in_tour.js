$(document).ready(function() {
    $('#tours > li').click(function() {
        $('#tours li').removeClass('choosed');
        $(this).toggleClass('choosed');
        if ($(this).hasClass('choosed')){
            var url = $(this).data('url');
            $.ajax({
                url: url,
                method: 'get',
                dataType: 'JSON',
                success: function(response){
                    $('#round_in_tour').empty();
                    $.each(response, function(key, val){
                        var url = Django.url('round:get_teams', val.id);
                        $('#round_in_tour').append(
                                '<option data-type_rang="' +
                                val.type_rang + '"' + 'data-url="' + url + '" >'
                                + val.type_name + '</option>');
                    });
                },
                error: function(){
                    $('#round_in_tour').html('<option id="-1">none</option>');
                }
            });
        }
    });

    $('#round_in_tour').change(function(){
        var url = $('option:selected').data('url');
        console.log(url);
        $.ajax({
            url: url,
            method: 'get',
            dataType: 'JSON',
            success: function(response){
                $('#teams_in_round').empty();
                $.each(response, function(key, val){
                    $('#teams_in_round').append(
                    '<li class="list-group-item"><div><img src="'
                    + JSON.parse(val['logo']) + '"/></div><div><p>' +
                    + JSON.parse(val['name']) + '</p></div></li>'
                    );
                });
            }
        });
    });

    $('#round_in_tour').change();
});