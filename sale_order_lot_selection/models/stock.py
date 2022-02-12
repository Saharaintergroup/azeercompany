from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
from odoo.tools import float_round, float_compare


class StockMove(models.Model):
    _inherit = "stock.move"

    lot_sale_line = fields.Many2one("stock.production.lot", "Lot Name", related='sale_line_id.lot_id')


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'

    @api.onchange('lot_id','qty_done')
    def _check_lot_name(self):
        if self.lot_id.id != self.move_id.lot_sale_line.id:
            raise ValidationError(
                _("You Should set Lot/Serial Number same Lot Name ( %s )") % (
                    self.move_id.lot_sale_line.name))
