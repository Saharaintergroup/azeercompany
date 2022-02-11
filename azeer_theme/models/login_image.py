# -*- coding: utf-8 -*-
from odoo import models, fields, api, _


class LoginImage(models.Model):
    _name = 'login.image'
    _rec_name = 'name'

    image = fields.Binary(string="Image")
    name = fields.Char(string="Name")
    title = fields.Char(string="Title")
    description = fields.Text(string = "Description")
    button_lable = fields.Char(string="Button Lable")
    button_link = fields.Char(string="Button Link")

