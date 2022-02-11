# -*- coding: utf-8 -*-
from odoo import api, fields, models, modules

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    #background_image = fields.Many2one('login.image', string="Image", help='Select Background Image For Login Page')
    
    login_image = fields.Many2one('login.image', string="Login Page Image" )
    pw_reset_image = fields.Many2one('login.image', string="Password Reset Page Image" )
    signup_image =  fields.Many2one('login.image', string="Signup Page Image")
    
    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        #image_id = int(self.env['ir.config_parameter'].sudo().get_param('login_background.background_image'))

        image_id_login_image = int(self.env['ir.config_parameter'].sudo().get_param('login_background.login_image'))
        image_id_pw_reset_image = int(self.env['ir.config_parameter'].sudo().get_param('login_background.pw_reset_image'))
        image_id_signup_image = int(self.env['ir.config_parameter'].sudo().get_param('login_background.signup_image'))

        res.update(
            #background_image=image_id,
            login_image = image_id_login_image,
            pw_reset_image= image_id_pw_reset_image ,
            signup_image = image_id_signup_image,

        )
        return res

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        param = self.env['ir.config_parameter'].sudo()

        #set_image = self.background_image.id or False

        set_login_image = self.login_image.id or False
        set_pw_reset_image = self.pw_reset_image.id or False
        set_signup_image = self.signup_image.id or False

        #param.set_param('login_background.background_image', set_image)

        param.set_param('login_background.login_image', set_login_image)
        param.set_param('login_background.pw_reset_image', set_pw_reset_image)
        param.set_param('login_background.signup_image', set_signup_image)
