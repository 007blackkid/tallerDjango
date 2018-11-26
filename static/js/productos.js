 $(document).ready(function(){
    $('.modal').modal();
    $('select').formSelect();    
  });


$("#btnEditar").on('click', function (){

  	var id=0;
   // Código alfa (para evaluar resultado en es.stackoverflow.com)
    this.href=window.location.href+"editarProducto/"+id;
    console.log("SE PRESIONO");
});