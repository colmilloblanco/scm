;(function($, window, undefined) {
	app = {
		run: function () {
			this.cargar_controles();
			this.events();
		}

		,cargar_controles: function () {
			$( ".table" ).dataTable();
			$( '.btn-generar-pago' ).popupWindow({ 
						centerScreen:1 
				}); 
		}

		,events: function () {
			$( ".table > tbody > tr > td" ).on( "click", ":input", this.click_check_multa );
			
		}

		,click_check_multa: function(){
			total = 0 ;
			ids = ""			
			$( ".table > tbody > tr" ).each(function(){
				$this = $( this ),
				$check = $this
						.children()
						.eq(0).find(":input"),
				$monto = $this
						.children()
						.eq(6)
						.text()


				if ($check.attr( "checked")){
					ids += $check.val() + "-"
					total =  total + parseFloat($monto) 
				}				

			})
			$ ( "#monto_pagar" ).text( "Monto a Pagar S/." +
				total)
			if (ids) {
				$( ".btn-generar-pago" ).attr( "href" , '/pagos/generar/' + ids )				
			} else{

				$( ".btn-generar-pago" ).removeAttr( "href")				
			}
		}

		

	}

	app.run()
})
(jQuery, window);
