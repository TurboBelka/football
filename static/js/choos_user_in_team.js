$(document).ready(function(){
    $('.user_info > li').click(function() {
        $(this).toggleClass("choose-user");
    });

    $('#add_user').click(function(){
        $(".user_info > .choose-user")
            .removeClass("choose-user")
            .appendTo(".choosed_users");

    });

    $('#delete_user').click(function(){
        $(".choosed_users > .choose-user")
            .removeClass("choose-user")
            .appendTo(".user_info");
    });

    $('.user_info > li').hover(function() {
        $(this).toggleClass('hover-light');
    });

    $('.submit_button').click(function(eventObj){
        eventObj.preventDefault();
        var url = $('#res_but').data('url');
        arr = [];
        $('ul.choosed_users > li').each(function(){
            arr.push($(this).data('user_id'));
         });

        data =  {
             'users_id': JSON.stringify(arr),
             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            };
        $.post(url, data, function(response){
            window.location.replace(response);}).fail(function(){
                $('#errorModal').modal();
            });
    });
});
