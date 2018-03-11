//preloader
$(window).on('load', function () {
var $preloader = $('#loader'),
$spinner = $preloader.find('.box');
$spinner.fadeOut();
$preloader.delay(350).fadeOut('slow');
});
$(document).ready(function() {
    $('.zbs').on('click', function () {
        $('#loader').show();
    });
});
$(document).mouseup(function (e) {
var elem = $('.change');
if(e.target!=elem[0]&&!elem.has(e.target).length){
elem.hide();
}
});
$(document).ready(function() {
$('.analiz').on('click', function () {
$('.change').show();
});
});

$(document).ready(function(){
    $('label').hide();
    $('.action-index').on('click',function() {
        $('.optimiz').hide(function () {
            $('.index').show();
            $(".action-index").addClass('active-tab');
            $(".action-opt").removeClass('active-tab');
        });
    });
    $('.action-opt').on('click',function() {
        $('.index').hide(function () {
            $('.optimiz').show();
            $(".action-opt").addClass('active-tab');
            $(".action-index").removeClass('active-tab');
        });
    });


    $('.action-go').on('click',function() {
        $('.yandex').hide(function () {
            $('.google').show();
            $(".action-go").addClass('active-tab');
            $(".action-ya").removeClass('active-tab');
        });
    });
    $('.action-ya').on('click',function() {
        $('.google').hide(function () {
            $('.yandex').show();
            $(".action-ya").addClass('active-tab');
            $(".action-go").removeClass('active-tab');
        });
    });


    $('.map-form').on('click', function () {
        $('.form-map').show();
    })
});


$(document).mouseup(function (e) {
    var elem = $('.form-map');
    if(e.target!=elem[0]&&!elem.has(e.target).length){
        elem.hide();
    }
});

//result ruk seo



//result ruk seo
$(document).ready(function() {
    $('.yaruk-js').on('click', function () {
        $('.ruk-go').hide(function () {
            $('.ruk-ya').show();
        });
    });
    $('.goruk-js').on('click', function () {
        $('.ruk-ya').hide(function () {
            $('.ruk-go').show();
        });
    });
    $('.smmruk-js').on('click', function () {
        $('.ruk-go').hide();
        $('.ruk-ya').hide(function () {
            $('.ruk-smm').show();
        });
    });

});


$(document).ready(function() {
    $('.tkd-js').on('click', function () {
        $('.ruk-untext').hide();
        $('.ruk-link').hide();
        $('.ruk-header').hide(function () {
            $('.ruk-tkd').show();
        });
    });
    $('.header-js').on('click', function () {
        $('.ruk-untext').hide();
        $('.ruk-link').hide();
        $('.ruk-tkd').hide(function () {
            $('.ruk-header').show();
        });
    });
    $('.untext-js').on('click', function () {
        $('.ruk-link').hide();
        $('.ruk-header').hide();
        $('.ruk-tkd').hide(function () {
            $('.ruk-untext').show();
        });
    });
    $('.erlink-js').on('click', function () {
        $('.ruk-header').hide();
        $('.ruk-untext').hide();
        $('.ruk-tkd').hide(function () {
            $('.ruk-link').show();
        });
    });
});




