$(document).ready(function () {
	var cookie1 = $.cookie("cookie1");
	var cookie2 = $.cookie("cookie2");
	var cookie3 = $.cookie("cookie3");
	!( cookie1 == "changed" ) || $('.Checkbox1').attr('checked',true);
	!( cookie2 == "changed" ) || $('.Checkbox2').attr('checked',true);
	!( cookie3 == "changed" ) || $('.Checkbox3').attr('checked',true);
	$('.Checkbox1').change(function () {               
		if( this.checked ) {
			$.cookie("cookie1", "changed");
		} else {
			$.cookie("cookie1", null);
		}         
	}).change();
	$('.Checkbox2').change(function () {
		if( this.checked ) {
			$.cookie("cookie2", "changed");
		} else {
			$.cookie("cookie2", null);
		}         
	}).change(); //ensure visible state matches initially
	$('.Checkbox3').change(function () {
		if( this.checked ) {
			$.cookie("cookie3", "changed");
		} else {
			$.cookie("cookie3", null);
		}         
	}).change(); //ensure visible state matches initially
});  //end function