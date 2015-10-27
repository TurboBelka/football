$(document).ready(function() {
    $('input[name=date_start]').datepicker({
        format: 'yyyy-mm-dd',
        orientation: "bottom right"
        });
    $('input[name=date_end]').datepicker({
        format: 'yyyy-mm-dd',
        orientation: "bottom right"
        });
    $('my_form').submit(function(eventObj){
        eventObj.preventDefault();
        var date_start = new Date($('input[name=date_start]').val());
        var date_end = new Date($('input[name=date_end]').val());
        if (date_start.getFullYear() > date_end.getFullYear()){
            console.log(date_start);
            $('#errorModal').modal();
        }else if (date_start.getMonth() > date_end.getMonth()){
            $('#errorModal').modal();
        }else if (date_start.getDay() > date_end.getDay()){
            $('#errorModal').modal();
        }else{
            var elem_of_data = $('#my_form').serialize();
            $.ajax({
                url: $('#my_form').attr('action'),
                method: $('#my_form').attr('method'),
                data: elem_of_data,

            });
        }


    });
});
