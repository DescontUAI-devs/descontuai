function callPaymentProcess () {
	//PAY ATTENTION
	//ESSE METODO ESTÁ APONTANDO PARA PRODUÇÃO

	var isOpenLightbox = PagSeguroLightbox('8616A9BAD9D9F4B2246E1FB787166E8F', {
	    success : function(transactionCode) {
	    	//continuou
	        alert("success - " + transactionCode);
	    },
	    abort : function() {}
	});

	// Redirecionando o cliente caso o navegador não tenha suporte ao Lightbox
	if (!isOpenLightbox){
	    location.href="https://pagseguro.uol.com.br/v2/checkout/payment.html?code="+code;
	}
}