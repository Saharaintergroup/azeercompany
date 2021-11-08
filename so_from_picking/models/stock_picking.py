# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError



class StockPicking(models.Model):
    _inherit = 'stock.picking'


    def create_sale_order(self):
        if not self.partner_id:
            raise ValidationError(_('Please Set Customer !'))

        sale_id = self._prepare_sale_order_data()
        group = self.env['procurement.group'].create({
            'name': sale_id.name,
            'partner_id': self.partner_id.id,
            'sale_id': sale_id.id
        })
        self.group_id = group.id

    def _prepare_sale_order_data(self):
        data = {
            'partner_id': self.partner_id.id,
            'picking_ids': [(4, self.id)],
        }
        sale_id = self.env['sale.order'].sudo().create(data)
        self._create_sale_order_line_data(sale_id)
        sale_id.action_confirm()
        return sale_id

    def _create_sale_order_line_data(self, sale_id):
        for line in self.move_ids_without_package:
            line_id = self.env['sale.order.line'].sudo().create(
                {
                    'product_id': line.product_id.id,
                    'product_uom': line.product_uom.id,
                    'product_uom_qty': line.quantity_done,
                    'qty_delivered': line.quantity_done,
                    'price_unit': line.product_id.list_price,
                    'qty_delivered_method': 'stock_move',
                    'order_id': sale_id.id,
                }
            )
            line.sale_line_id = line_id.id



    def action_view_sale_order(self):
        self.ensure_one()
        ctx = self.env.context.copy()
        ctx.pop("default_picking_id", False)
        return self.with_context(ctx).sale_id.get_formview_action()