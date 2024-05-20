# -*- coding: utf-8 -*-
# from odoo import http


# class .\azeer\alazeerQuotationReport(http.Controller):
#     @http.route('/.\azeer\alazeer_quotation_report/.\azeer\alazeer_quotation_report', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/.\azeer\alazeer_quotation_report/.\azeer\alazeer_quotation_report/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('.\azeer\alazeer_quotation_report.listing', {
#             'root': '/.\azeer\alazeer_quotation_report/.\azeer\alazeer_quotation_report',
#             'objects': http.request.env['.\azeer\alazeer_quotation_report..\azeer\alazeer_quotation_report'].search([]),
#         })

#     @http.route('/.\azeer\alazeer_quotation_report/.\azeer\alazeer_quotation_report/objects/<model(".\azeer\alazeer_quotation_report..\azeer\alazeer_quotation_report"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('.\azeer\alazeer_quotation_report.object', {
#             'object': obj
#         })
