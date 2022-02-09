# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class azeer_log(models.Model):
#     _name = 'azeer_log.azeer_log'
#     _description = 'azeer_log.azeer_log'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
