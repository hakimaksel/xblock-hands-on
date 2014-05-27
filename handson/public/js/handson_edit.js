function HandsOnEditBlock(runtime, element) {
    $('.xblock-save-button').bind('click', function() {
        var data = {
            'workpad': $('#workpad').val(),
	    'video': $('#video').val(),
        };
        var handlerUrl = runtime.handlerUrl(element, 'studio_submit');
        $.post(handlerUrl, JSON.stringify(data)).complete(function() {
            window.location.reload(false);
        });
    });
}