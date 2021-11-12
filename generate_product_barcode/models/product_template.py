from odoo import fields, models, api, _


class ProductBrand(models.Model):
    _inherit = 'product.template'

    def generate_barcode(self):
        for rec in self:
            seq = self.env['ir.sequence'].next_by_code('product.template.barcode')
            rec.barcode = 'AZ' + seq + str(fields.Date.today().day) + str(fields.Datetime.today().month) + str(
                fields.Datetime.today().year)


class ProductVarientBrand(models.Model):
    _inherit = 'product.product'

    def generate_barcode(self):
        for rec in self:
            seq = self.env['ir.sequence'].next_by_code('product.template.barcode')
            rec.barcode = 'AZ' + seq + str(fields.Date.today().day) + str(fields.Datetime.today().month) + str(
                fields.Datetime.today().year)
