(function ($) {
    $.fn.mobileMenu = function (options) {
        function isMobile() {
            return ($('body').width() < settings.mobileWidth);
        }
        var defaults = {
            defaultText: THEMEREX_NAVIGATE_TO,
            className: 'select-menu',
			mainMenuSelector: '#mainmenu',
			mobileWidth: 800
        	}, 
			settings = $.extend(defaults, options),
            el = $(this),
			first = settings.defaultText;
        this.each(function () {
            var clonedObj = el.clone().removeClass('sf-js-enabled').removeAttr('id').addClass('theme_button');
			el.find('a').each(function () {
            	if($(this).text() == "") {
            		return;
            	}
				if (this.href == window.location.href)
					first = $(this).text();
            });
			$('<div class="' + settings.className + '">'
				+ '<a class="' + settings.className + '-button theme_button"><span class="icon"></span>'
				+ '<span class="holder">' + first + '</span></a>'
				+ '</div>').append(clonedObj).insertAfter(el);
			$('.' + settings.className + ' > ul a').addClass('theme_button');
			$('.' + settings.className + ' > ul').hide();
            $('.' + settings.className).on('click', '.'+settings.className+'-button', function (e) {
				$(this).siblings('ul').slideToggle();
				e.preventDefault();
				return false;
            });
        });

        function runPlugin() {
            if (isMobile()) {
                $('.'+settings.className).show();
                $(settings.mainMenuSelector).hide();
                $('body').addClass('menu_mobile');
            } else {
                $('.'+settings.className).hide();
                $(settings.mainMenuSelector).show();
                $('body').removeClass('menu_mobile');
            }
        }
        runPlugin();
        $(window).resize(function () {
            runPlugin();
        });
        return this;
    };
})(jQuery);