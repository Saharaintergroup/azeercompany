# -*- coding: utf-8 -*-

from odoo import http

from odoo.addons.website.controllers.main import Website


class Website(Website):
    @http.route(auth='public')
    def index(self, **kw):
        super(Website, self).index()
        return http.request.render('theme_azeer.azeer_home', {})

    @http.route(['/web/aboutus'], auth='public', type="http", website=True)
    def aboutus(self, **kw):
        return http.request.render('theme_azeer.azeer_aboutus_page', {})

    @http.route(['/web/contactus'], auth='public', type="http", website=True)
    def contactus(self, **kw):
        return http.request.render('theme_azeer.azeer_contactus_page', {})