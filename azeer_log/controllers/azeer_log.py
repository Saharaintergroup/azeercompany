# -*- coding: utf-8 -*-
from odoo.http import Controller, request, Response, route


class AzeerLog(Controller):
    @route('/azeer_log', type='http', auth='public', sitemap=False)
    def azeerLog(self, **kw):
        context = {}
        print("-----------------------Azeer Logs-------------------")
        return request.render('azeer_log.azeer_log_page', context)
