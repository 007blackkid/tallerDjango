var total;
var articulos;

$(document).ready(function() {

 CalcularTotal();
 document.getElementById("articulos").innerHTML = articulos;
 document.getElementById("total").innerHTML = "$"+total+" MXN";

});


function CalcularTotal() {    
    var filas=document.querySelectorAll("#ventasTable tbody tr"); 
    total=0; 
    articulos =0;   
    filas.forEach(function(e) {         
        var columnas=e.querySelectorAll("td");        
        var cantidad=parseFloat(columnas[3].textContent); 

        articulos++;
        total+=cantidad;
    });    
    var filas=document.querySelectorAll("#miTabla tfoot tr td");
    console.log(total);
    console.log(articulos);
}


