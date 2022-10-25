import math

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class SaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    lot_id = fields.Many2one("stock.production.lot", "Lot", copy=False)
    lot_expiration_date = fields.Datetime(related='lot_id.expiration_date', string="Expiration Date")
    product_uom = fields.Many2one('uom.uom', string='Unit of Measure',)

    def get_uom(self):
        for rec in self:
            return rec.product_id.uom_po_id.id

    @api.onchange('product_id')
    def get_uom_domain(self):
        ids = []
        if self.product_id:
            ids.append(self.product_id.uom_id.id)
            ids.append(self.product_id.uom_po_id.id)

        return {
            'domain':
                {
                    'product_uom': [('id', 'in', ids)]
                },
        }

    @api.onchange("product_id")
    def product_id_change(self):
        super().product_id_change()
        self.product_uom = self.product_id.uom_po_id.id
        self.lot_id = False

    @api.onchange("product_id")
    def _onchange_product_id_set_lot_domain(self):
        available_lot_ids = []
        if self.order_id.warehouse_id and self.product_id:
            quants = self.env["stock.quant"].read_group(
                [
                    ("product_id", "=", self.product_id.id),
                    # ("location_id", "child_of", location.id),
                    ("quantity", ">", 0),
                    ("lot_id", "!=", False),
                ],
                ["lot_id"],
                "lot_id",
            )

            available_lot_ids = [quant["lot_id"][0] for quant in quants]

        self.lot_id = False
        return {"domain": {"lot_id": [("id", "in", available_lot_ids)]}}
