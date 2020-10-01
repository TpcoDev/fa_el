odoo.define('valida_empresa_template.website_sale', function (require) {
'use strict';
	var ajax = require('web.ajax');
    require('website_sale.website_sale');
	
	
	$(document).ready(function() 
	{
		// Submit RFQ button CLicked
		$('#submit_for_quote').on('click', function() 
		{	  
			var ip_address = '';
			$.getJSON('https://api.ipify.org?format=json', function(data){
			ip_address = data.ip
				ajax.jsonRpc('/shop/confirmation/empty_json', 'call', {ip:data.ip}).then(function (data) {
					if(data['not_allowed']==true){
						return window.location = '/shop/confirmation?warning=Quotation Limit Exceed for Today!';
					}else{
						return window.location = '/shop/confirmation?message=Your RFQ submitted successfully!';
					}
	          	});
			});
		});
	});		
	 var clickwatch = (function(){
         var timer = 0;
         return function(callback, ms){
           clearTimeout(timer);
           timer = setTimeout(callback, ms);
         };
   })();

    $('.oe_website_sale').on("change", ".oe_cart input.js_quantity[data-product-id]", function (event) {
    	event.preventDefault();
    	
      	var $input = $(this);
          if ($input.data('update_change')) {
              return;
          }
        var value = parseInt($input.val() || 0, 10);
        if (isNaN(value)) {
            value = 1;
        }
        var $dom = $(this).closest('tr');
        //var default_price = parseFloat($dom.find('.text-danger > span.oe_currency_value').text());
        var $dom_optional = $dom.nextUntil(':not(.optional_product.info)');
        var line_id = parseInt($input.data('line-id'),10);
        var product_ids = [parseInt($input.data('product-id'),10)];
       
        
        ajax.jsonRpc("/shop/check_submit_rfq",'call',{
           	 'line_id': line_id,
           	 'value':value
        }).then(function (data) {
       	 if ('show_submit_rfq_button' in data && data['show_submit_rfq_button']==1){
       		 $('#a_submit_for_quote').css('display','block');
       		 $('#a_submit_for_quote2').css('display','block');
       	 }else{
       		 $('#a_submit_for_quote').css('display','none');
       		 $('#a_submit_for_quote2').css('display','none');
       	 }
       	 if ('show_payment_button' in data && data['show_payment_button']==1){
       		 $('#a_proceed_checkout').css('display','block');
       		 $('#a_proceed_checkout2').css('display','block');
       	 }else{
       		 $('#a_proceed_checkout').css('display','none');
       		 $('#a_proceed_checkout2').css('display','none');
       	 }
       	 if ( data['show_submit_rfq_button']==1 || data['show_payment_button']==1){
       		 $('.both_product_alert').css('display','none');
       	 }
       	 if ( data['show_submit_rfq_button']==0 && data['show_payment_button']==0){
       		 $('.both_product_alert').css('display','block');
       	 }
       	 if ( data['show_submit_rfq_button']==1 && data['show_payment_button']==1){
       		 $('#a_submit_for_quote').css('display','none');
       		 $('#a_proceed_checkout').css('display','none');
       		 $('#a_submit_for_quote2').css('display','none');
       		 $('#a_proceed_checkout2').css('display','none');
       	 }
        });
        
        clickwatch(function(){
          $dom_optional.each(function(){
              $(this).find('.js_quantity').text(value);
              product_ids.push($(this).find('span[data-product-id]').data('product-id'));
          });
          $input.data('update_change', true);

          ajax.jsonRpc("/shop/cart/update_json", 'call', {
              'line_id': line_id,
              'product_id': parseInt($input.data('product-id'), 10),
              'set_qty': value
          }).then(function (data) {
              $input.data('update_change', false);
              var check_value = parseInt($input.val() || 0, 10);
              if (isNaN(check_value)) {
                  check_value = 1;
              }
              if (value !== check_value) {
                  $input.trigger('change');
                  return;
              }
              var $q = $(".my_cart_quantity");
              if (data.cart_quantity) {
                  $q.parents('li:first').removeClass("hidden");
              }
              else {
                  $q.parents('li:first').addClass("hidden");
                  $('a[href*="/shop/checkout"]').addClass("hidden");
              }

              $q.html(data.cart_quantity).hide().fadeIn(600);
              $input.val(data.quantity);
              $('.js_quantity[data-line-id='+line_id+']').val(data.quantity).html(data.quantity);

              $(".js_cart_lines").first().before(data['website_sale.cart_lines']).end().remove();

              if (data.warning) {
                  var cart_alert = $('.oe_cart').parent().find('#data_warning');
                  if (cart_alert.length === 0) {
                      $('.oe_cart').prepend('<div class="alert alert-danger alert-dismissable" role="alert" id="data_warning">'+
                              '<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button> ' + data.warning + '</div>');
                  }
                  else {
                      cart_alert.html('<button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button> ' + data.warning);
                  }
                  $input.val(data.quantity);
              }
          });
        }, 500);
        
      });
    
    });
