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

        /*$.ajax({
            url: url,
            method: 'post',
            data: {
             'users_id': JSON.stringify(arr),
             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response){
//                window.location.replace(response);
            },
            error: function(){
                alert("you must select an even number of players");
            }
        });*/
        data =  {
             'users_id': JSON.stringify(arr),
             'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            };
        $.post(url, data).fail(function(){alert(0);}).done(function(){alert(1);});
    });
});
