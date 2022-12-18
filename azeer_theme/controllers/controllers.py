# -*- coding: utf-8 -*-
# from odoo import http


# class AzeerTheme(http.Controller):
#     @http.route('/azeer_theme/azeer_theme/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/azeer_theme/azeer_theme/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('azeer_theme.listing', {
#             'root': '/azeer_theme/azeer_theme',
#             'objects': http.request.env['azeer_theme.azeer_theme'].search([]),
#         })

#     @http.route('/azeer_theme/azeer_theme/objects/<model("azeer_theme.azeer_theme"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('azeer_theme.object', {
#             'object': obj
#         })
