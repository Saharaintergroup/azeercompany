# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from datetime import date, timedelta
from odoo.tools.translate import _
from odoo.addons.auth_signup.controllers.main import *
_logger = logging.getLogger(__name__)

class AuthSignupHome(AuthSignupHome):

	@http.route('/web/signup', type='http', auth='public', website=True, sitemap=False)
	def web_auth_signup(self, *args, **kw):
	    qcontext = self.get_auth_signup_qcontext()

	    if not qcontext.get('token') and not qcontext.get('signup_enabled'):
	        raise werkzeug.exceptions.NotFound()

	    if 'error' not in qcontext and request.httprequest.method == 'POST':
	        try:
	            self.do_signup(qcontext)
	            # Send an account creation confirmation email
	            if qcontext.get('token'):
	                User = request.env['res.users']
	                user_sudo = User.sudo().search(
	                    User._get_login_domain(qcontext.get('login')), order=User._get_login_order(), limit=1
	                )
	                template = request.env.ref('auth_signup.mail_template_user_signup_account_created', raise_if_not_found=False)
	                if user_sudo and template:
	                    template.sudo().send_mail(user_sudo.id, force_send=True)
	            return self.web_login(*args, **kw)
	        except UserError as e:
	            qcontext['error'] = e.args[0]
	        except (SignupError, AssertionError) as e:
	            if request.env["res.users"].sudo().search([("login", "=", qcontext.get("login"))]):
	                qcontext["error"] = _("Another user is already registered using this email address.")
	            else:
	                _logger.error("%s", e)
	                qcontext['error'] = _("Could not create a new account.")

	    #ews edit
	    qcontext['signup_image'] = ""
	    qcontext['signup_image_title'] = "Welcome To El-Azeer"
	    qcontext['signup_image_description'] = "Welcome To El -Azeer Group, We Are Happy To See You Here, We Can Help You With The Best Medical Choices."
	    qcontext['signup_image_button_lable'] = "Get Started"
	    qcontext['signup_image_button_link'] = "\\"
	    param_obj = request.env['ir.config_parameter'].sudo()
	    company_id = request.env.company.id
	    qcontext['company_id']= "/logo.png?company="+str(company_id)
	    background_image = param_obj.get_param('login_background.signup_image')
	    if background_image:
	    	login_image_model = request.env['login.image']
	    	image_object = login_image_model.sudo().search([('id','=',int(background_image))])
	    	base_url = param_obj.get_param('web.base.url')
	    	image_url = base_url + '/web/image?' + 'model=login.image&id=' + background_image + '&field=image'
	    	qcontext['signup_image'] = image_url or ''
	    	if image_object.title:
	    		qcontext['signup_image_title'] = image_object.title
	    	if image_object.description:
	    		qcontext['signup_image_description'] = image_object.description
	    	if image_object.button_lable:
	    		qcontext['signup_image_button_lable'] = image_object.button_lable
	    	if image_object.button_link:
	    		qcontext['signup_image_button_link'] = image_object.button_link
	    #ews edit end
	    
	    response = request.render('auth_signup.signup', qcontext)
	    response.headers['X-Frame-Options'] = 'DENY'
	    return response

	@http.route('/web/reset_password', type='http', auth='public', website=True, sitemap=False)
	def web_auth_reset_password(self, *args, **kw):
	    qcontext = self.get_auth_signup_qcontext()

	    if not qcontext.get('token') and not qcontext.get('reset_password_enabled'):
	        raise werkzeug.exceptions.NotFound()

	    if 'error' not in qcontext and request.httprequest.method == 'POST':
	        try:
	            if qcontext.get('token'):
	                self.do_signup(qcontext)
	                return self.web_login(*args, **kw)
	            else:
	                login = qcontext.get('login')
	                assert login, _("No login provided.")
	                _logger.info(
	                    "Password reset attempt for <%s> by user <%s> from %s",
	                    login, request.env.user.login, request.httprequest.remote_addr)
	                request.env['res.users'].sudo().reset_password(login)
	                qcontext['message'] = _("An email has been sent with credentials to reset your password")
	        except UserError as e:
	            qcontext['error'] = e.args[0]
	        except SignupError:
	            qcontext['error'] = _("Could not reset your password")
	            _logger.exception('error when resetting password')
	        except Exception as e:
	            qcontext['error'] = str(e)

	    #ews edit
	    qcontext['pw_reset_image'] = ""
	    qcontext['pw_reset_image_title'] = "Welcome To El-Azeer"
	    qcontext['pw_reset_image_description'] = "Welcome To El -Azeer Group, We Are Happy To See You Here, We Can Help You With The Best Medical Choices."
	    qcontext['pw_reset_image_button_lable'] = "Get Started"
	    qcontext['pw_reset_image_button_link'] = "\\"
	    param_obj = request.env['ir.config_parameter'].sudo()
	    company_id = request.env.company.id
	    qcontext['company_id']= "/logo.png?company="+str(company_id)
	    background_image = param_obj.get_param('login_background.pw_reset_image')
	    if background_image:
	        login_image_model = request.env['login.image']
	        image_object = login_image_model.sudo().search([('id','=',int(background_image))])
	        base_url = param_obj.get_param('web.base.url')
	        image_url = base_url + '/web/image?' + 'model=login.image&id=' + background_image + '&field=image'
	        qcontext['pw_reset_image'] = image_url or ''
	        if image_object.title:
	        	qcontext['pw_reset_image_title'] = image_object.title
	        if image_object.description:
	        	qcontext['pw_reset_image_description'] = image_object.description
	        if image_object.button_lable:
	        	qcontext['pw_reset_image_button_lable'] = image_object.button_lable
	        if image_object.button_link:
	        	qcontext['pw_reset_image_button_link'] = image_object.button_link

	    #ews edit end

	    response = request.render('auth_signup.reset_password', qcontext)
	    response.headers['X-Frame-Options'] = 'DENY'
	    return response
