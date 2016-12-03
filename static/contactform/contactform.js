function display_form_errors(errors, $form) {
    for (var k in errors) {
        if (k == 'message')
        {
            $form.find('textarea[name=' + k + ']').after('<div class="validation_error"  style="text-align: left;">' + errors[k] + '</div>');
        }
        $form.find('input[name=' + k + ']').after('<div class="validation_error"  style="text-align: left";' +
                                                    'style="vertical-align: top">' + '<span>' + errors[k] + '</span>' + '</div>');
    }
}
$(document).ready(function() {
				$("#feedback").submit(function(event) {
					event.preventDefault();
					$("div.validation_error").remove();
					$.ajax({
						url: "contact/",
						beforeSend: function() {
							$("#load").fadeIn(400);
						},
						type: "post",
						data: $("#feedback").serialize(),
						success: function(data) {
                             if ( data.result == 'success') {
                                $("#sendmessage").text(data.message);
                                $("#sendmessage").show();
                                $("#sendmessage").fadeIn();
							    $("#feedback").trigger("reset");
							    $("#feedback").bind("click", function(event){
							    $("#sendmessage").fadeOut();
							    })
                             }
                             else if (data.result == 'error')
                             {
                                  display_form_errors(data['response'], $("#feedback"));
                             }
                        }
					}).done(function() {
						$("#load").fadeOut(400);
					});
				});
			});