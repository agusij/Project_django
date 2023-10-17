/*!
* Start Bootstrap - Landing Page v6.0.6 (https://startbootstrap.com/theme/landing-page)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-landing-page/blob/master/LICENSE)
*/
// This file is intentionally blank
// Use this file to add JavaScript to your project
$(document).ready(function() {
    $('.like-button').click(function(event) {
        event.preventDefault();
        const url = $(this).attr('href');

        $.post(url, function(data) {
            const likesCount = data.likes_count;
            $(event.target).next().text(likesCount + " likes");
        });
    });
});
