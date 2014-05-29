$(function(){

    var imageNumber=1;
    $( "div.slide" ).html( "<img src=https://s3.amazonaws.com/xblock/slider/Slide"+imageNumber+".JPG width='800' height='600'>" );

    //Forward Button
    $( "forward" ).click(function () {
	imageNumber++;
	$( "div.slide" ).html( "<img src=https://s3.amazonaws.com/xblock/slider/Slide"+imageNumber+".JPG width='800' height='600'>" );
    });

    //Back Button
    $( "back" ).click(function () {
	if(imageNumber>1){
	    imageNumber--;
	    $( "div.slide" ).html( "<img src=https://s3.amazonaws.com/xblock/slider/Slide"+imageNumber+".JPG width='800' height='600'>" );
	}
    });

    /***
	$('.bxslider').bxSlider({
	video: true,
	useCSS: false
	});
    ***/
});
