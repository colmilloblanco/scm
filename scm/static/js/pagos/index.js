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
