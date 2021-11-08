# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class alazeer_accounting(models.Model):
#     _name = 'alazeer_accounting.alazeer_accounting'
#     _description = 'alazeer_accounting.alazeer_accounting'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
