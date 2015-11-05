$(document).ready(function() {
    $('#my_form input[name=date_start]').datepicker({
        format: 'yyyy-mm-dd',
        orientation: "bottom right"
        });
    $('#my_form input[name=date_end]').datepicker({
        format: 'yyyy-mm-dd',
        orientation: "bottom right"
        });
    $('#my_form').submit(function(eventObj){

        var date_start = new Date($('input[name=date_start]').val());
        var date_end = new Date($('input[name=date_end]').val());
        if (date_start > date_end){
            $('#errorModal').modal();
            eventObj.preventDefault();
            return;
        }else{
            var elem_of_data = $('#my_form').serialize();
//            $.ajax({
//                url: $('#my_form').attr('action'),
//                method: $('#my_form').attr('method'),
//                data: elem_of_data,

//            });
        }
    });
});
