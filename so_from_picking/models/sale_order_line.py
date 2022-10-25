from odoo import fields, models, api


class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    product_uom = fields.Many2one('uom.uom', string='Unit of Measure', )

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
