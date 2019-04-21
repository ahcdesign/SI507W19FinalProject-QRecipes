// JavaScript to input the recipes into the database

$(function() {
	$('#recipe_submit').click(function() {
		$.ajax({
			url: '/qrecipes/addreciperow',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response) {
				alert($.parseJSON(response)["message"]);
			},
			error: function(error){
				alert("There was an error");
				console.log(error)
			}
		});
	});
});