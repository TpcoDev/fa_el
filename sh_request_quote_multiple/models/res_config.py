# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.

from odoo import api, fields, models, _
from odoo.exceptions import UserError, AccessError

class ResCompany(models.Model):
    _inherit = 'res.company'
    
    enable_spam_protection = fields.Boolean("Enable Spam Protection",default=1)
    max_quotation_logged_user = fields.Integer("Logged User Max Quotation (Per Day)",default=1)
    max_quotation_public_user = fields.Integer("Non Logged User Max Quotation (Per Day)",default=1)

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'
    
    enable_spam_protection = fields.Boolean("Enable Spam Protection",
                                             related='company_id.enable_spam_protection',readonly=False)
    max_quotation_logged_user = fields.Integer("Logged User Max Quotation (Per Day)",
                                             related='company_id.max_quotation_logged_user',readonly=False)
    max_quotation_public_user = fields.Integer("Non Logged User Max Quotation (Per Day)",
                                             related='company_id.max_quotation_public_user',readonly=False)
    
    
    