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
            this.$form_modelo = $('#frm-modelo');
            this.$form_clase = $('#frm-clase');
           this.$form_categoria = $('#frm-categoria');
            

		}

		,load_controls: function  () {
			
			//boton nuevo vehicuclo
			this.$list = $('.list', this.$menu).button({
				icons: {
					primary: 'ui-icon-document'
				}
			})
			// boton guardar
			this.$save = $('.save').button({
				icons: {primary: 'ui-icon-disk'}
			})

			$('select').combobox();
			$('#id_ruc').parent().hide()
		}

		,events: function(){
			this.$form.on('dblclick', '.id_propietario', this.dblclick_propietario)
			$( "#id_tipo_persona" ).on('change', this.change_tipo_persona)
			this.$form.on('dblclick', '.id_combustible', this.dblclick_combustible)
			this.$form.on('dblclick', '.id_sede', this.dblclick_sede)
			this.$form.on('dblclick', '.id_carroceria', this.dblclick_carroceria)
			this.$form.on('dblclick', '.id_color', this.dblclick_color)
			this.$form.on('dblclick', '.id_asociacion', this.dblclick_asociacion)
			this.$form.on('dblclick', '.id_marca', this.dblclick_marca)
			this.$form.on('dblclick', '.id_modelo', this.dblclick_modelo)
			this.$form.on('dblclick', '.id_clase', this.dblclick_clase)
			this.$form.on('dblclick', '.id_categoria', this.dblclick_categoria)
			$( "#btn-add-propietario" ).on( 'click' , this.click_add_propietario);
			$( "#btn-add-combustible" ).on('click', this.click_add_combustible);
			$("#btn-add-sede").on('click', this.click_add_sede);
			$("#btn-add-carroceria").on('click', this.click_add_carroceria);
			$("#btn-add-color").on('click', this.click_add_color);
			$("#btn-add-asociacion").on('click', this.click_add_asociacion);
			$("#btn-add-marca").on('click', this.click_add_marca);
			$("#btn-add-modelo").on('click', this.click_add_modelo);
			$("#btn-add-clase").on('click', this.click_add_clase);
			$("#btn-add-categoria").on('click', this.click_add_categoria);

		}
       // funcion para agregar un nuevo propietario 

		,dblclick_propietario: function(){
			$( "#frm-propietario" ).modal("show");			
			
		}

		,change_tipo_persona: function(){
		
			if($(this).val() == 'N'){
				$("#id_ruc").parent().hide()
				$("#id_dni").parent().show()
			}
			else{
				$("#id_ruc").parent().show()
				$("#id_dni").parent().hide()
			}
		}

		,click_add_propietario: function () {
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
								$( "#frm-propietario" ).modal("hide");
							}
						})
		}
       //funcion para agregar un nuevo combustible

       , dblclick_combustible: function(){
       	$( "#frm-combustible" ).modal("show");	
       }
		
	  	, click_add_combustible:function(){

						$.ajax({
							 type:"POST",
							 url: "/vehiculos/ajax/add/combustible/",
							 data:$("#frm-combustible").serialize()
							 ,dataType:"json"
							 ,beforeSend:function(jqxhr, settings) {
							 	csrf = $.cookie("csrftoken");
							 	jqxhr.setRequestHeader("X-CSRFToken", csrf);
							 	console.log("enviando peticion")
							 },
							 success:function(data){
							 	var valor = data[0].pk
							 	var text = data[0].fields.nombre
							 	//nuevo option para combustible
							 	$("<option>")
							 	.val(valor)
							 	.text(text)
							 	.attr("selected", true)
							 	.prependTo("#id_combustible")//añade option al principio
							 	$(".id_combustible").val(text) //añade el ultimo registro al principio
							 	$(this).parent().find(':input').val("") // limpia la caja de texto
							 	$("#frm-combustible").modal("hide");

							 }

						})
					
		}

      // funcion para agregar una nueva sede 

       ,dblclick_sede:function(){
       	$("#ssede").modal("show");
       }
       	
       	,click_add_sede:function(){
       	 			$.ajax({
       	 				type:"POST",
       	 				url:"/vehiculos/ajax/add/sede/",
       	 				data:$("#frm-sede").serialize(),
       	 				dataType:"json",
       	 				beforeSend:function(jqxhr, settings){
       	 					csrf = $.cookie("csrftoken");
       	 					jqxhr.setRequestHeader("X-CSRFToken", csrf);
       	 					console.log("enviando peticion")

       	 				}
       	 				,success:function(data){
       	 					var valor = data[0].pk
       	 					var text = data[0].fields.descripcion
       	 					$("<option>")
       	 					.val(valor)
       	 					.text(text)
       	 					.attr("select", true)
       	 					.prependTo("#id_sede")

       	 					$(".id_sede").val(text)
       	 					$(this).parent().find(':input').val("")
       	 					$("#ssede").modal("hide");


       	 				}
       	 			})

       	 }

		//funcion para agregar una nueva carroceria
  		,dblclick_carroceria:function(){
	  		$("#scarroceria").modal('show')
	  	}
	  	,click_add_carroceria:function(){
	  					$.ajax({
       	 				type:"POST",
       	 				url:"/vehiculos/ajax/add/carroceria/",
       	 				data:$("#frm-carroceria").serialize(),
       	 				dataType:"json",
       	 				beforeSend:function(jqxhr, settings){
       	 					csrf = $.cookie("csrftoken");
       	 					jqxhr.setRequestHeader("X-CSRFToken", csrf);
       	 					console.log("enviando peticion")
       	 				}
       	 				,success:function(data){
       	 					var valor = data[0].pk
       	 					var text = data[0].fields.nombre
       	 					$("<option>")
       	 					.val(valor)
       	 					.text(text)
       	 					.attr("select", true)
       	 					.prependTo("#id_carroceria")

       	 					$(".id_carroceria").val(text)
       	 					$(this).parent().find(':input').val("")
       	 					$("#scarroceria").modal("hide")


       	 				}
       	 			})
	 
	  		
  	    }

      // Funcion agregar una nueva color
    ,dblclick_color:function(){
    	$("#scolor").modal('show');
    }
    ,click_add_color:function(){
    				$.ajax({
    					type:"POST",
    					data:$("#frm-color").serialize(),
    					url:"/vehiculos/ajax/add/color/",
    					dataType:"json",
    					beforeSend:function(jqxhr, settings){
    						csrf  = $.cookie("csrftoken");
    						jqxhr.setRequestHeader("X-CSRFToken", csrf);
    						console.log("enviando peticion")
    					},
    					success:function(data){
    						var valor = data[0].pk
    						var text = data[0].fields.descripcion

                          $("<option>")
                          .val(valor)
                          .text(text)
                          .attr("select", true)
                          .prependTo("#id_color")//pone a la primera option
                          $(".id_color").val(text)//pone en la caja de texto
                          $(this).parent().find(':intput').val("")
                          $("#scolor").modal('hide');
                      }

    				})

    
    }

   // Funcion Para registro de Asociacion
	   ,dblclick_asociacion:function(){
	   	$("#sasociacion").modal('show');
	   }
	  ,click_add_asociacion:function(){
	   				$.ajax({
	   					type:'POST',
	   					url:'/vehiculos/ajax/add/asociacion/',
	   					data:$("#frm-asociacion").serialize(),
	   					dataType:"json",
	   					beforeSend:function(jqxhr, settings){
	   						csrf = $.cookie("csrftoken");
	   						jqxhr.setRequestHeader("X-CSRFToken", csrf);
	   						console.log("enviando Peticion")

	   					},
	   					success:function(data){
	   						var valor = data[0].pk
	   						var text = data[0].fields.nombre
	   						$("<option>")
	   						.val(valor)
	   						.text(text)
	   						.attr("select", true)
	   						.prependTo("#id_asociacion")
	   						$(".id_asociacion").val(text)
	   						$(this).parent().find(':input').val("")
	   						$("#sasociacion").modal('hide')
                       
	   					}

	   	})

	   }

	   //fucion de Registro de Marca
	   ,dblclick_marca:function(){
	   	$("#smarca").modal('show');
	   	}
	   	,click_add_marca:function(){
	   				$.ajax({
	   					type:"POST",
	   					url:"/vehiculos/ajax/add/marca/",
	   					data:$("#frm-marca").serialize(),
	   					dataType:"json",
	   					beforeSend:function(jqxhr, settings){
	   						csrf = $.cookie("csrftoken");
	   						jqxhr.setRequestHeader("X-CSRFToken", csrf);
	   						console.log("enviando Peticion")

	   					}

	   					,success:function(data){
	   					  var val = data[0].pk
	   					  var text = data[0].fields.descripcion
	   					  $("<option>")
	   					  .val(val)
	   					  .text(text)
	   					  .attr("select", true)
	   					  .prependTo("#id_marca")
	   					  $(".id_marca").val(text)
	   					  $(this).parent().find(':input').val("")
	   					  $("#smarca").modal("hide");
	   					}

	   				})
	   }
	  // Function Modelo
	  ,dblclick_modelo:function(){
	    $("#smodelo").modal('show')
	    }
	   ,click_add_modelo:function(){
	    			$.ajax({
	    				type:"POST",
	    				url:"/vehiculos/ajax/add/modelo/",
	    				data:$("#frm-modelo").serialize(),
	    				dataType:"json"
	    				,beforeSend:function(jqxhrs, settings){
	    					csrf = $.cookie("csrftoken");
	    					jqxhrs.setRequestHeader("X-CSRFToken", csrf);
	    					console.log("enviando Peticion")
	    				}
	    				,success:function(data){
	    					var val = data[0].pk
	    					var text = data[0].fields.descripcion
	    					$("<option>")
	    					.val(val)
	    					.text(text)
	    					.attr("select", true)
	    					.prependTo("#id_modelo")
	    					$(".id_modelo").val(text)
	    					$(this).parent().find(':input').val("")
	   					    $("#smodelo").modal('hide')


	    				}

	    })

	  	
	  }
	  //funcion para registrar una clase
	,dblclick_clase:function(){
	    $("#sclase").modal('show');
		}
	,click_add_clase:function(){
	    			$.ajax({
	    				type:"POST",
	    				url:"/vehiculos/ajax/add/clase/",
	    				data:$("#frm-clase").serialize(),
	    				dataType:"json"
	    				,beforeSend:function(jqxhrs, settings){
	    					csrf = $.cookie("csrftoken");
	    					jqxhrs.setRequestHeader("X-CSRFToken", csrf);
	    					console.log("enviando Peticion")
	    				}
	    				,success:function(data){
	    					var val = data[0].pk
	    					var text = data[0].fields.descripcion
	    					$("<option>")
	    					.val(val)
	    					.text(text)
	    					.attr("select", true)
	    					.prependTo("#id_clase")
	    					$(".id_clase").val(text)
	    					$(this).parent().find(':input').val("")
	   					  $("#sclase").modal('hide');
	    				}

	    })

	  	
	  }
   //funcion para agregar una categoria 
   ,dblclick_categoria:function(){
	    $("#scategoria").modal('show');
	    }
	,click_add_categoria:function(){
	    			$.ajax({
	    				type:"POST",
	    				url:"/vehiculos/ajax/add/categoria/",
	    				data:$("#frm-categoria").serialize(),
	    				dataType:"json"
	    				,beforeSend:function(jqxhrs, settings){
	    					csrf = $.cookie("csrftoken");
	    					jqxhrs.setRequestHeader("X-CSRFToken", csrf);
	    					console.log("enviando Peticion")
	    				}
	    				,success:function(data){
	    					var val = data[0].pk
	    					var text = data[0].fields.descripcion
	    					$("<option>")
	    					.val(val)
	    					.text(text)
	    					.attr("select", true)
	    					.prependTo("#id_categoria")
	    					$(".id_categoria").val(text)
	    					$(this).parent().find(':input').val("")
	   					  $("#scategoria").modal('hide')
	    				}

	    })

	  	
	  }
	   //end app
	}

	window.run = app.init();
});