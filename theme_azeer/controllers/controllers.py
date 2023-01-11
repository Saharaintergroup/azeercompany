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

    @http.route(['/contactus'], auth='public', type="http", website=True)
    def contactus(self, **kw):
        return http.request.render('theme_azeer.azeer_contactus_page', {})

    @http.route(['/web/laboratorymedicine'], auth='public', type="http", website=True)
    def laboratorymedicine(self, **kw):
        return http.request.render('theme_azeer.laboratory_medicine_page', {})

    @http.route(['/web/cinicalservies'], auth='public', type="http", website=True)
    def cinicalservies(self, **kw):
        return http.request.render('theme_azeer.cinicalservies_page', {})

    @http.route(['/web/radiology'], auth='public', type="http", website=True)
    def radiology(self, **kw):
        return http.request.render('theme_azeer.radiology_page', {})

    @http.route(['/web/pathology'], auth='public', type="http", website=True)
    def pathology(self, **kw):
        return http.request.render('theme_azeer.pathology_page', {})

    @http.route(['/web/signup'], auth='public', type="http", website=True)
    def signup(self, **kw):
        return http.request.render('theme_azeer.signup_page', {})

