$(document).ready(function () {
    var csrftoken = $('[name=csrfmiddlewaretoken]').val();
    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    $('.like-button').click(function (e) {
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
            success: function (response) {
                if (response['like_count'] !== null) {
                    like_count = response['like_count'];
                    $('#like-count-' + status_id).text(like_count);
                    // Update the dislike count if the status was previously disliked
                    if (response['status_disliked']) {
                        var dislike_count = parseInt($('#dislike-count-' + status_id).text());
                        $('#dislike-count-' + status_id).text(dislike_count - 1);
                    }
                }
            }
        });
    });

    $('.dislike-button').click(function (e) {
        e.preventDefault();
        var status_id = $(this).attr('id').split('-')[2];
        var dislike_count = parseInt($('#dislike-count-' + status_id).text());

        $.ajax({
            type: 'POST',
            url: "/news/dislike/",
            data: {
                'status_id': status_id,
                'csrfmiddlewaretoken': csrftoken
            },
            success: function (response) {
                if (response['dislike_count'] !== null) {
                    dislike_count = response['dislike_count'];
                    $('#dislike-count-' + status_id).text(dislike_count);
                    // Update the dislike count if the status was previously disliked
                    if (response['status_liked']) {
                        var like_count = parseInt($('#like-count-' + status_id).text());
                        $('#like-count-' + status_id).text(like_count - 1);
                    }
                }
            }
        });
    });
});
