$(function() {
    console.log("in function")
    $("#search").autocomplete({
            source: "/api/search_autocomplete/",
            minLength: 2,
    });
});