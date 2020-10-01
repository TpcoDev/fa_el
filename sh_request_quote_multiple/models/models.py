# -*- coding: utf-8 -*-
# Copyright (C) Softhealer Technologies.

from odoo import fields,models,api
from odoo.addons.website.models import ir_http
from odoo.http import request
                
class ProductTemplate(models.Model):
    _inherit = 'product.template'
            
    request_for_quotation = fields.Boolean("Request for Quotation ?")
    
class SaleOrder(models.Model):
    _inherit = 'sale.order'
            
    request_for_quotation = fields.Boolean("Request for Quotation ?")

    def get_amount_untaxed(self):
        amount_untaxed = 0.0
        if self.order_line:
            for line in self.order_line.filtered(lambda c:c.product_id.request_for_quotation == False):
                amount_untaxed += line.price_subtotal
        
        return amount_untaxed
    
    def get_amount_tax(self):
        amount_taxed = 0.0
        if self.order_line:
            for line in self.order_line.filtered(lambda c:c.product_id.request_for_quotation == False):
                amount_taxed += line.price_tax
        return amount_taxed
    
    def get_amount_total(self):
        amount_untaxed = 0.0
        amount_taxed = 0.0
        if self.order_line:
            for line in self.order_line.filtered(lambda c:c.product_id.request_for_quotation == False):
                amount_taxed += line.price_tax
                amount_untaxed += line.price_subtotal
                
        return (amount_taxed+amount_untaxed)
                
class LoggedUserData(models.Model):
    _name = 'logged.user.data'
    
    ip_address = fields.Char("IP Address")
    date = fields.Date("Date")
    partner_id = fields.Many2one('res.partner',string="Partner")
    type=fields.Selection([('logged_in','Logged In'),('public','Public User')],string="Type",dafault='public')
    
                