;(function ($, window, undefined) {
	app = {
		run: function () {
			this.cargar_controles();
		}

		,cargar_controles: function(){
			$( ".modal" ).modal("show");
		}		

	}

	app.run();
})(jQuery, window);