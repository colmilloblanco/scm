jQuery(function(){
	app = {
		init: function(){
			this.cache_elements();
			this.load_controls();
			this.events();
		}

		,cache_elements: function(){
		
			this.$menu = $('#menu');
			this.$form = $('#frm_new_vehiculo');
			this.$form_list = $('#frm-list');	 
			this.$form_propietario = $('#frm-propietario'); 
            this.$form_combustible = $('#frm-combustible');
            this.$form_sede = $('#frm-sede');
            this.$form_carroceria = $('#frm-carroceria');
            this.$form_color = $('#frm-color');
            this.$form_asociacion = $('#frm-asociacion');
            this.$form_marca = $('#frm-marca');
            this.$form_soat = $('#frm-soat');

		}

		,load_controls: function  () {
			
		

}

		,events: function(){
			this.$form.on('dblclick', '.id_propietario', this.dblclick_propietario)
			

		}
		,dblclick_propietario: function(){
			$( "#spropietario" )
			.dialog({
				autoOpen:false,
				modal: true,
				title: 'Nuevo Propietario',
				width: '40%',
				buttons:{
					Registrar: function(){
						$.ajax({
							type: "POST",
							url: "/vehiculos/ajax/add/propietario/",
							data: $( "#frm-propietario" ).serialize()
							,dataType: "json"
							,beforeSend: function(jqxhr, settings){
								csrf = $.cookie("csrftoken");
								jqxhr.setRequestHeader("X-CSRFToken", csrf);
								console.log("enviando peticion")
							},
							success: function(data){

								var valor = data[0].pk // captura el id de nuevo propietario
								var text = data[0].fields.nombre // captura el nombre del nuevo propietario
								
								/*Crea una nueva option pata el select de propitario*/
								$( "<option>" )
								.val(valor) //agina valor al option
								.text(text) // asigna el texto al option
								.attr( "selected", true ) //seleciona el option creado
								.prependTo("#id_propietario") // agrega el option al pricipio del option


								$( ".id_propietario" ).val(text) // agregra el nombre del nuevo propietario ala caja de e texto

								$(this).parent().find(':input').val("")//limpia la caja de texto del formulario
								$( "#spropietario" ).dialog('close')// cierra la ventana de dialog chau
							}
						})
					},
					Cancelar: function(){
						$(this).parent().find(':input').val("")
						$(this).dialog('close');
					}
				}
			});
			$( "#spropietario" ).dialog('open')
		}

		}

	window.run = app.init();
});