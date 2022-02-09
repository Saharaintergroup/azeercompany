# -*- coding: utf-8 -*-
# from odoo import http


# class AzeerLog(http.Controller):
#     @http.route('/azeer_log/azeer_log/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azeer_log/azeer_log/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('azeer_log.listing', {
#             'root': '/azeer_log/azeer_log',
#             'objects': http.request.env['azeer_log.azeer_log'].search([]),
#         })

#     @http.route('/azeer_log/azeer_log/objects/<model("azeer_log.azeer_log"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azeer_log.object', {
#             'object': obj
#         })
