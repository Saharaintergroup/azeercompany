# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    is_features = fields.Boolean(string="Visible Features",default=False)
    product_features = fields.One2many('product.features', 'product_temps', string="Add Product feature")
    image_features = fields.Image()
    

class ProductFeatures(models.Model):
    _name = 'product.features'
    _rec_name = 'title_1'
    

    product_temps = fields.Many2one('product.template', 'Product Template')
    title_1 = fields.Char(string="Title")
    description_1 = fields.Text(string = "Description")