# -*- coding: utf-8 -*-

from odoo import api, fields, models
from odoo.addons.http_routing.models.ir_http import slug
from odoo.tools.translate import html_translate


class WebsiteResPartner(models.Model):
    _name = 'res.partner'
    _inherit = ['res.partner', 'website.seo.metadata']

    about_azeer_partner_title1 = fields.Text('About Azeer Partner', translate=True)
    about_azeer_partner_title2 = fields.Text('About Azeer Partner title', translate=True)
    azeer_partner_description = fields.Html('Description about Azeer partner', strip_style=True, translate=html_translate)

    azeer_partner_choose_us = fields.Text('Azeern partner choose us', translate=True)
    azeer_partner_choose_us_description = fields.Html('Azeer partner choose us description', strip_style=True, translate=html_translate)
    detail_image_512 = fields.Image("partner detail image", max_width=512, max_height=512)
