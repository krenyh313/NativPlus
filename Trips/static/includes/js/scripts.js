var map;
function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: 32.090595, lng: 34.802134 },
        zoom: 15
    });
}

//     var photos = ["includes/images/Gal.png", "includes/images/Aric.png", "includes/images/Yael.png", "includes/images/Yuval.png", "includes/images/Chen.png", "includes/images/Matan.png", "includes/images/Shira.png", "includes/images/Ohad.png"];
//     var name = ["Gal Baruch ", "Aric Harel ", "Yeal Shor", "Yuval Segev", "Chen Lev", "Matan Ziv", "Shira Rot", "Ohad Lavi"];
//     var age = ["27", "38", "21", "49", "24", "30", "29", "39"];
//     var gender = ["woman", "man", "woman", "man", "woman", "man", "woman", "man"];
//     var smoking = ["yes", "no", "no", "yes", "no", "yes", "yes", "no"];
//     var music = ["yes", "yes", "no", "yes", "no", "yes", "no", "yes"];
//     var pet = ["yes", "no", "no", "yes", "yes",];
//     var time = ["18:30", "19:00", "18:30", "18:45", "20:00", "20:15", "18:45", "19:00"];
//     var location = ["Hadera", "Gan-Shmuel", "Netanya", "Zihron-Yaacov", "Herzliya", "Hadera", "Haifa", "Kfar-Yona"];
//     var rating = ["9.5", "8.2", "7.9", "7.2", "9.0", "8.9", "6.8", "7.0"];

function selected(num) {
    var pref = document.getElementsByClassName("preferences")[0];
    var btn = pref.getElementsByClassName("btn")[num - 1];
    if (btn.style.borderColor == "rgb(70, 136, 71)")
        btn.style.borderColor = "rgb(204, 204, 204)";
    else
        btn.style.borderColor = "rgb(70, 136, 71)";
}

$(document).ready(function () {
    $.ajaxSetup({ cache: false });
    $('#id_Destination').keyup(function () {
        $('#result').html('');
        $('#state').val('');
        var searchField = $('#id_Destination').val();
        var expression = new RegExp(searchField, "i");
        // $.getJSON("{% static 'json/city.json' %}", function (data) {
        $.getJSON("city.json", function (data) {
            $.each(data, function (key, value) {
                if (value.name.search(expression) != -1) {
                    $('#result').append('<li class="list-group-item link-class"> ' + value.name + ' </li> ');
                }
            });
        });
    });

    $('#result').on('click', 'li', function () {
        var click_text = $(this).text().split('|');
        $('#id_Destination').val($.trim(click_text[0]));
        $("#result").html('');
    });
});

$(document).ready(function () {
    if ($(window).width() < 900) {
        $('.hamburger').hover(function () {
            $('nav').slideDown('medium');
        },
            $('nav').hover(
                function () {
                    $('nav').show();
                },
                function () {
                    $('nav').slideUp('medium');
                }
            )
        );
    }
});