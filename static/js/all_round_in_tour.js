var round_selected = 0;
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
//                        var url = Django.url('round:get_teams', val.id);
                        var url = Urls['round:get_teams'](val.id);
                        $('#round_in_tour').append(
                                '<option data-type_rang="' +
                                val.type_rang + '"' + ' data-url="' + url +
                                '" data-round_id="' + val.id + '">'
                                + val.type_name + " (" + val.date_start + ')</option>');
                    });
                    $('#round_in_tour').change();

                },
                error: function(){
                    $('#round_in_tour').html('<option id="-1">none</option>');
                }
            });
        }
    });

    $('#round_in_tour').change(function(){
        var url = $('option:selected').data('url');
        round_selected = $('option:selected').data('round_id');
        var url_image = Urls['match:match'](round_selected);
        $('#look_image').attr('href', url_image);
        $.ajax({
            url: url,
            method: 'get',
            success: function(response){
                $('#teams_in_round').empty();
                $.each(response, function(key, val){
                    if (val['logo']==null){
                        val['logo']="/static/teams_logo/your-logo-here.png"
                    }
                    $('#teams_in_round').append(
                    '<li class="list-group-item"><div class="row"><div class="col-xs-4"><img src="'+
                    val['logo'] + '"/></div><div class="col-xs-8"><p>' +
                    val['name'] + '</p></div></div></li>'
                    );
                });
            }
        });
    });

    $('#add_new').click(function(eventObj){
        eventObj.preventDefault();
        var tour_id = $('#tours li.choosed').data('tour_id');
        var url = Urls['round:choose_type_round'](tour_id);
        $.ajax({
            url: url,
            method: 'get',
            success: function(response){
                $('#type_round').empty();
                $.each(response, function(i, val){
                    $('#type_round').append(
                        "<option data-id='" + (i + 1) + "'>" + val + "</option>"
                    );
                });

                $('input[name=date_start]').datepicker({
                    format: 'yyyy-mm-dd',
                    orientation: "bottom right"
                    });
                $('input[name=date_end]').datepicker({
                    format: 'yyyy-mm-dd',
                    orientation: "bottom right"
                    });
                $('#modal_add_round').modal();
            }
        });
    });

    $('#create_round').click(function(eventObj){
        eventObj.preventDefault();
        var tour_id = $('#tours li.choosed').data('tour_id');
        var url = Urls['round:create_round']();
        var date_start = new Date($('input[name=date_start]').val());
        var date_end = new Date($('input[name=date_end]').val());

        var data = {
            'type_id': $('#type_round option:selected').data('id'),
            'tour_id': tour_id,
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken').val()
        };
        var tour_d_start = new Date($('#tours li.choosed').data('tour_dstart'));

        if (date_start.getFullYear() < tour_d_start.getFullYear()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else if (date_start.getMonth() < tour_d_start.getMonth()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else if (date_start.getDay() < tour_d_start.getDay()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else{
            data['date_start'] = date_start;
        }

        var tour_d_end = new Date($('#tours li.choosed').data('tour_dend'));

        if (date_end.getFullYear() > tour_d_end.getFullYear()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else if (date_end.getMonth() > tour_d_end.getMonth()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else if (date_end.getDay() > tour_d_end.getDay()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else if (date_end.getFullYear() < date_start.getFullYear()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else if (date_end.getMonth() < date_start.getMonth()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else if (date_end.getDay() < date_start.getDay()){
            $('#modal_add_round').modal('hide');
            $('#errorModal').modal();
        }else{
            data['date_end'] = date_end;
             $.post(url, data, function(response){
                    window.location.replace(response);})
        }


    });

    $('#gen_matchs').click(function(eventObj){
        eventObj.preventDefault();
        var url = Urls['round:add_teams'](round_selected);
        $.ajax({
            url: url,
            method: 'get',
            success: function(response){
                if ($('#round_in_tour option:selected').data('type_rang')=='6'){

                }
                $('#all_teams').empty();
                $.each(response, function(key, val){
                    if (val['logo']==""){
                        val['logo']="/static/teams_logo/your-logo-here.png"
                    }
                    $('#all_teams').append(
                    '<li class="list-group-item" data-team_id="' + val['id'] +
                    '"><div class="row"><div class="col-xs-4"><img src="'+
                    val['logo'] + '"/></div><div class="col-xs-8"><p>' +
                    val['name'] + '</p></div></div></li>'
                    );
                });
                $('#all_teams li').click(function() {
                    $(this).toggleClass('choosed');
                });
                if ($('#round_in_tour option:selected').data('type_rang') == '6'){
                    $('#countMatch').show();
                }else{
                    $('#countMatch').hide();
                }
                $('#modalAddTeam').modal();
            }
        });
    });

     $('#add_choosed').click(function(eventObj){
        eventObj.preventDefault();
        var teams_to_add = [];
        $('#all_teams > li.choosed').each(function(){
            teams_to_add.push($(this).data('team_id'));
        });

        data =  {
             'teams_id': JSON.stringify(teams_to_add),
             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
             'count_match': $('#count_match').val()
            };
        var round_selected = $('#round_in_tour option:selected').data('round_id');

        console.log(data);
        var url1 = Urls['round:gen_matchs'](round_selected);
        $.post(url1, data, function(response){
            window.location.replace(response);}).fail(function(){
                $('#errorModal').modal();
            });
     });

});