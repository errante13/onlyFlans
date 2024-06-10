$(document).ready(function(){
    $("#nombre_mostrar").click(function(){
    //  $("#menu").fadeToggle("");
       $("#menu").fadeToggle("slow");
    //  $("#menu").fadeToggle(3000);
    });
 

   $("#ojo").mousedown(function(){
      $("#password").removeAttr('type');
      $("#ojo").addClass('bi-eye-slash-fill').removeClass('bi-eye-fill');
   });

   $("#ojo").mouseup(function(){
      $("#password").attr('type','password');
      $("#ojo").addClass('bi-eye-fill').removeClass('bi-eye-slash-fill');
   });
 
});
