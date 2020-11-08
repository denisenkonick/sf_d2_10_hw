function btn_success_onClick() {
	console.log("success!");
 	$.get("/success", function( data ) {
    console.log( typeof data );
    console.log(data);
  })
}

function btn_danger_onClick() {
	console.log("fail!")
 	let jqxhr = $.get('/fail', function(data){
    console.log(data)})
}

$('.btn-success').on("click", btn_success_onClick())
$('.btn-danger').on("click", btn_danger_onClick())
