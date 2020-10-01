# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name": "Request for quotation Multiple products",
    
    "author": "Softhealer Technologies",
    
    "website": "https://www.softhealer.com",
        
    "support": "support@softhealer.com",

    "version": "11.0.1",
    
    "category": "eCommerce",
    
    "summary": """ If you want to hide price for a particular product in the shop and set that product for 'RFQ'? Sometimes the company wants more than one product's quote. Currently, odoo does not provide any kind of feature for make request for RFQ in a website, so don't worry, here we made a module, customer can request for more than one product's RFQ. You can set the product for RFQ in the shop, just tick the right 'Request for Quotation' option in the product and that product price will not display in the shop if the user needs that product then they will have to make an RFQ for that product. For spam protection, you can control a request with logged or None logged the user. Set several requests for logged or Non logged users, just go into website config setting and enable 'Enable Spam Protection', and you can see the list of users who sent a request, with IP address in 'Logged User Data'. You can see the list of RFQ in the 'Request for Quotation' sub-menu in the 'Quotation' menu.
 Request For Quotation - Multi Product Advance Odoo
 Hide Particular Product Price,Set Product For Request For Quotation, Make RFQ For Product Module, Invisible Product Price,Request For Quotation Multi Product Shop Odoo.
 Hide Product Price App, Set Product RFQ Module, Set Product Request For Quotation, RFQ Multi Product Shop Odoo.
 Request For Quotation - Multiple Product Advance	询价-多种产品预付款	Demande de devis - Avance de plusieurs produits	Angebotsanfrage - Mehrfacher Produktvorschuss	Richiesta di preventivo - Anticipo su più prodotti	Solicitud de presupuesto - Avance de producto múltiple	Solicitação de cotação - Avanço múltiplo do produto

 """,
        
    "description": """ If you want to hide price for a particular product in the shop and set that product for 'RFQ'? Sometimes the company wants more than one product's quote. Currently, odoo does not provide any kind of feature for make request for RFQ in a website, so don't worry, here we made a module, customer can request for more than one product's RFQ. You can set the product for RFQ in the shop, just tick the right 'Request for Quotation' option in the product and that product price will not display in the shop if the user needs that product then they will have to make an RFQ for that product. For spam protection, you can control a request with logged or None logged the user. Set several requests for logged or Non logged users, just go into website config setting and enable 'Enable Spam Protection', and you can see the list of users who sent a request, with IP address in 'Logged User Data'. You can see the list of RFQ in the 'Request for Quotation' sub-menu in the 'Quotation' menu.
 Request For Quotation - Multi Product Advance Odoo
 Hide Particular Product Price,Set Product For Request For Quotation, Make RFQ For Product Module, Invisible Product Price,Request For Quotation Multi Product Shop Odoo.
 Hide Product Price App, Set Product RFQ Module, Set Product Request For Quotation, RFQ Multi Product Shop Odoo.""",
     
    "depends": ["sale_management", "product", "website_sale"],
    
    "data": [
        "security/ir.model.access.csv",
        "views/res_config.xml",
        "views/logged_user_data.xml",
        "views/assets.xml",
        "views/views.xml",
        "views/website_sale_product.xml",
    ],
    
    "images": ["static/description/background.png",],              
    "installable": True,
    "auto_install": False,
    "application": True,
    "price": "40",
    "currency": "EUR"      
}    
