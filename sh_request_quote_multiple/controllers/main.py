# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import fields, http, SUPERUSER_ID, tools, _
from odoo.http import request
from odoo.addons.website_form.controllers.main import WebsiteForm


class WebsiteSaleForm(WebsiteForm):
    
   # inherit controller to check visibility of process checkout and submit rfq button
    @http.route(['/shop/check_submit_rfq'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def check_rfq_button(self, line_id=None, value=False):
        if request.website.sale_get_order():
            order = request.website.sale_get_order()
            value_dic = {}
            show_submit_rfq_button = 1
            show_payment_button = 1
            if order.order_line:
                for line in order.order_line:
                    if line.id==line_id and value>0:
                        if line.product_id.request_for_quotation == False:
                            show_submit_rfq_button = 0
                        if line.product_id.request_for_quotation == True:
                            show_payment_button = 0
                    elif line.id!=line_id:
                        if line.product_id.request_for_quotation == False:
                            show_submit_rfq_button = 0
                        if line.product_id.request_for_quotation == True:
                            show_payment_button = 0
            value_dic['show_submit_rfq_button']=show_submit_rfq_button
            value_dic['show_payment_button']=show_payment_button
        return value_dic
    
    @http.route(['/shop/cart/empty_json'], type='json', auth="public", methods=['POST'], website=True, csrf=False)
    def empty_cart_json(self,ip):
        """This route is called when submit to Quote button called."""
        order = request.website.sale_get_order()
        not_allowed = False
        # get logged in user:
        if ip:
            if order and order.company_id and order.company_id.enable_spam_protection:
                if request.website.is_public_user():# is public user
                    public_user_count = request.env['logged.user.data'].sudo().search_count([('date','=',fields.Date.today()),
                                                                                             ('ip_address','=',str(ip)),
                                                                                             ('type','=','public')])
                    
                    allowed_public_user_count = order.company_id.max_quotation_public_user
                    if(allowed_public_user_count<=public_user_count): # restrict if counter exceed
                        not_allowed = True
                    else:
                        request.env['logged.user.data'].sudo().create({'ip_address':str(ip),
                                                                       'date':fields.Date.today(),
                                                                       'partner_id':request.env.user.partner_id.id,
                                                                       'type':'public'})
                else:
                    
                    logged_user_count = request.env['logged.user.data'].sudo().search_count([('date','=',fields.Date.today()),
                                                                                             ('ip_address','=',str(ip)),
                                                                                             ('type','=','logged_in')])
                    allowed_logged_user_count = order.company_id.max_quotation_logged_user
                    if(allowed_logged_user_count<=logged_user_count):
                        not_allowed = True  # restrict if counter exceed
                    else:
                        request.env['logged.user.data'].sudo().create({'ip_address':str(ip),
                                                                       'date':fields.Date.today(),
                                                                       'partner_id':request.env.user.partner_id.id,
                                                                       'type':'logged_in'})
        
        if not not_allowed:
            order.write({'request_for_quotation':True})
            
            partner = request.env.user.partner_id
            if partner and partner.last_website_so_id:
                partner.write({'last_website_so_id':False})
            
            request.website.sale_reset() # reset Cart
            
        return {'not_allowed':not_allowed}