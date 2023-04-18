$(document).ready(function() {
    var csrftoken = $('[name=csrfmiddlewaretoken]').val();
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    $('.like-button').click(function(e) {
        e.preventDefault();
        var status_id = $(this).attr('id').split('-')[2];
        var like_count = parseInt($('#like-count-' + status_id).text());

        $.ajax({
            type: 'POST',
            url: "/news/like/",
            data: {
                'status_id': status_id,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function(response) {
                if (response['like_count'] !== null) {
                    like_count = response['like_count'];
                    $('#like-count-' + status_id).text(like_count);
                }
            }
        });
    });
});






