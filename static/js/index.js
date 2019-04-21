// Search feature on the homepage for Flask Route #2

$(document).ready(function(){
    $('select').formSelect();
    $('select > option').css('font-size', '40px');
    $('#recipe_submit').click(function() {
        var path = $('select').val();
        
        var search = $("input").val()
        if (search === null || search === "") {
            M.toast({html: "Please enter a search term!"});
            return false;
        } else {
            window.location.href = "/qrecipes/search/" + search
        }
    })
});