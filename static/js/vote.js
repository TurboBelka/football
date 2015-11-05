$(document).ready(function(){
    var adjustment;

    $(".simple_with_animation").sortable({
      group: 'simple_with_animation',
      pullPlaceholder: false,
      // animation on drop
      onDrop: function  ($item, container, _super) {
        var $clonedItem = $('<li/>').css({height: 0});
        $item.before($clonedItem);
        $clonedItem.animate({'height': $item.height()});

        $item.animate($clonedItem.position(), function  () {
          $clonedItem.detach();
          _super($item, container);
        });
      },

      // set $item relative to cursor position
      onDragStart: function ($item, container, _super) {
        var offset = $item.offset(),
            pointer = container.rootGroup.pointer;

        adjustment = {
          left: pointer.left - offset.left,
          top: pointer.top - offset.top
        };

        _super($item, container);
      },
      onDrag: function ($item, position) {
        $item.css({
          left: position.left - adjustment.left,
          top: position.top - adjustment.top
        });
      }
    });

    $('#save_changes').click(function(eventObj){
        eventObj.preventDefault();
        var new_users_position = [];
        $('.simple_with_animation li').each(function(){
            new_users_position.push($(this).data('user_id'));
        });
        var data = {
            'new_position': JSON.stringify(new_users_position),
            'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
            'tour_id': $('.simple_with_animation').data('tour_id')
        };
        $.ajax({
            url: Urls['index:res_vote'](),
            data: data,
            method: 'post',
            success: function(response){
                window.location.replace(response);
            }
        });
    });
});