$(document).ready(function() {
				$("#feedback").submit(function(event) {
					event.preventDefault();
					$.ajax({
						url: "contact/",
						beforeSend: function() {
							$("#load").fadeIn(400);
						},
						type: "post",
						data: $("#feedback").serialize(),
						success: function(answer) {
							$("#sendmessage").fadeIn();
							$("#feedback").trigger("reset");
							$("#feedback").bind("click", function(event){
							    $("#sendmessage").fadeOut();
							})

						}
					}).done(function() {
						$("#load").fadeOut(400);
					});
				});
			});