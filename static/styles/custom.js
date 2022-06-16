//$(document).ready(function(){
//    $('input[type="file"]').change(function(e){
//        var fileName = e.target.files[0].name;
//        $('.img-caption').attr("src", fileName);
//    });
//});
function readURL(input) {
  if (input.files && input.files[0]) {
    var reader = new FileReader();
    reader.onload = function (e) {
      $('.img-caption')
        .attr('src', e.target.result);
    };
    reader.readAsDataURL(input.files[0]);
  }
}

let a=["Hello","World","Now"];
var b='';
//function generateCaptions(){
//    for(let i=0; i<a.length; i++){
//        b+='<p>' + a[i] + '</p>';
//    }
//    $('.captions').html(b);
//    $('.generate-caption').css("display", "none");
//    $('.reset-caption').css("display", "inline-block");
//}
