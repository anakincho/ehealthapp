$(document).ready(function() {
	
	function toggleBing(bingCheckboxID, BingToggleID) {
	var checkbox = document.getElementById(bingCheckboxID);
	var toggle = document.getElementById(bingToggleID);
	updateToggle = bingCheckbox.checked ? bingToggle.disabled=true : toggle.disabled=false;
	}