;(function($, window, undefined){
	app = {
		run: function(){
			this.cache_elements();
			this.load_controls();
		}

		,cache_elements: function(){
			this.$table = $('.table');
			
		}

		,load_controls: function  () {
			/* tabla q contiene a los vehiculos*/
			this.$table.dataTable({				
				'oLanguage':{
					'sLengthMenu': 'Ver _MENU_ registros',
					'sSearch': 'Buscar',
					'sInfo': 'Mostrando _START_ a _END_ de _TOTAL_ registros'
				}
			});
			
		}

		,events: function(){

		}
	}

	app.run()

})(jQuery, window);
;(function($, window, undefined) {
	app = {
		run: function () {
			this.cargar_controles();
		}

		,cargar_controles: function () {
			$( ".table" ).dataTable();
		}

	}

	app.run()
})
(jQuery, window);