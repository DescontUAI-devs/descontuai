function callPaymentProcess () {
	console.log('teste');
	//PAY ATTENTION
	//ESSE METODO ESTÁ APONTANDO PARA PRODUÇÃO

	//trocar esse código pelo codigo do produto no pagseguro
	var codigo = '1F69A3CF7878ED9994B3DF9DDC706796';
	var isOpenLightbox = PagSeguroLightbox({
	    code: codigo
	}, {
	    success : function(transactionCode) {
	    	//continuou
	        alert("success - " + transactionCode);
	    },
	    abort : function() {
	    	//cancelou
	        alert("abort");
	    }
	});

	// Redirecionando o cliente caso o navegador não tenha suporte ao Lightbox
	if (!isOpenLightbox){
	    location.href="https://pagseguro.uol.com.br/v2/checkout/payment.html?code="+code;
	}
}