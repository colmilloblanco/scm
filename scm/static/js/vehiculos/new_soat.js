
        $(document).ready(function() {
           $("#dialogo").dialog({autoOpen:false});
           $("#abrir").click(function(event) {
               // $("#dialogo").dialog('option','position',[event.offsetX, event.offsetY]);
               
               $("#dialogo").dialog('open');
           });
           $("#cerrar").click(function() {
               $("#dialogo").dialog('close');
           });
        });   
