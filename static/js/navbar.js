$(window).on('scroll', function () {
    if ($(window).scrollTop()) {
        $('nav').addClass('black');

    }

    else {
        $('nav').removeClass('black');
    }
})