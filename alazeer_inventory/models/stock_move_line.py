# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime

class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    ex_date = fields.Datetime("Ex Date")

    @api.depends('product_id', 'picking_type_use_create_lots', 'lot_id.expiration_date','ex_date')
    def _compute_expiration_date(self):
        for move_line in self:
            if move_line.ex_date:
                move_line.expiration_date = move_line.ex_date
            elif not move_line.expiration_date and move_line.lot_id.expiration_date:
                move_line.expiration_date = move_line.lot_id.expiration_date
            elif move_line.picking_type_use_create_lots:
                if move_line.product_id.use_expiration_date:
                    if not move_line.expiration_date:
                        move_line.expiration_date = fields.Datetime.today() + datetime.timedelta(
                            days=move_line.product_id.expiration_time)
                else:
                    move_line.expiration_date = False