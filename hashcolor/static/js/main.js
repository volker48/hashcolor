$(function () {
    $('#hash_form').submit(function (e) {
            e.preventDefault();
            var string = $(this).find('input').val();
            if (!string) {
                return;
            }
            $.get('/' + string + '/', function (data) {
                $('.jumbotron').css('background', '#' + data.hashcolor);
                $('.swatch').css('background', '#' + data.hashcolor);
                $('.hexcolor').text('#' + data.hashcolor);
            });
        }
    );
});
