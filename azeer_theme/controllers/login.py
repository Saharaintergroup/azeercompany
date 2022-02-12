# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request
from datetime import date, timedelta
from odoo.tools.translate import _
from odoo.addons.web.controllers.main import *
_logger = logging.getLogger(__name__)

class Home(Home):

	@http.route('/web/login', type='http', auth="none")
	def web_login(self, redirect=None, **kw):
	    ensure_db()
	    request.params['login_success'] = False
	    if request.httprequest.method == 'GET' and redirect and request.session.uid:
	        return request.redirect(redirect)

	    if not request.uid:
	        request.uid = odoo.SUPERUSER_ID

	    values = request.params.copy()
	    try:
	        values['databases'] = http.db_list()
	    except odoo.exceptions.AccessDenied:
	        values['databases'] = None

	    if request.httprequest.method == 'POST':
	        old_uid = request.uid
	        try:
	            uid = request.session.authenticate(request.session.db, request.params['login'], request.params['password'])
	            request.params['login_success'] = True
	            return request.redirect(self._login_redirect(uid, redirect=redirect))
	        except odoo.exceptions.AccessDenied as e:
	            request.uid = old_uid
	            if e.args == odoo.exceptions.AccessDenied().args:
	                values['error'] = _("Wrong login/password")
	            else:
	                values['error'] = e.args[0]
	    else:
	        if 'error' in request.params and request.params.get('error') == 'access':
	            values['error'] = _('Only employees can access this database. Please contact the administrator.')

	    if 'login' not in values and request.session.get('auth_login'):
	        values['login'] = request.session.get('auth_login')

	    if not odoo.tools.config['list_db']:
	        values['disable_database_manager'] = True

	    #ews edit
	    values['login_image'] = ""
	    values['login_image_title'] = "Welcome To El-Azeer"
	    values['login_image_description'] = "Welcome To El -Azeer Group, We Are Happy To See You Here, We Can Help You With The Best Medical Choices."
	    values['login_image_button_lable'] = "Get Started"
	    values['login_image_button_link'] = "\\"
	    company_id = request.env.company.id
	    values['company_id']= "/logo.png?company="+str(company_id)
	    
	    param_obj = request.env['ir.config_parameter'].sudo()
	    background_image = param_obj.get_param('login_background.login_image')
	    if background_image:
	    	login_image_model = request.env['login.image']
	    	image_object = login_image_model.sudo().search([('id','=',int(background_image))])
	    	base_url = param_obj.get_param('web.base.url')
	    	image_url = base_url + '/web/image?' + 'model=login.image&id=' + background_image + '&field=image'
	    	values['login_image'] = image_url or ''
	    	if image_object.title:
	    		values['login_image_title'] = image_object.title
	    	if image_object.description:
	    		values['login_image_description'] = image_object.description
	    	if image_object.button_lable:
	    		values['login_image_button_lable'] = image_object.button_lable
	    	if image_object.button_link:
	    		values['login_image_button_link'] = image_object.button_link
	    #ews edit end

	    response = request.render('web.login', values)
	    #ews edit
	    #response.qcontext.update(self.get_auth_signup_config())
	    #ews edit end
	    response.headers['X-Frame-Options'] = 'DENY'
	    return response


