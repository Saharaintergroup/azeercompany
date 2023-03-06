# -*- coding: utf-8 -*-

from odoo import models, fields, api


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    sale_term_ids = fields.One2many(
        'sale.term', 'sale_order_id', string='Sale term')


class SaleTerm(models.Model):
    _name = "sale.term"
    _description = 'Sale Term'

    sale_order_id = fields.Many2one(
        'sale.order', string='Sale Order Reference')
    name = fields.Many2one("sale.term.name", 'Terms', required=True)
    description = fields.Text('Description', required=False, readonly=False)

    @api.onchange('name')
    def _onchange_description_id(self):
        self.description = self.name.description


class SaleTermName(models.Model):
    _name = "sale.term.name"
    _rec_name = 'name'

    name = fields.Char('Name', required=True)
    description = fields.Text("Description")
