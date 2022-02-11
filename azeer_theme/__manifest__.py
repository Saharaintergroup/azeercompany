# -*- coding: utf-8 -*-
{
    'name': "azeer_theme",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    #'category': 'Theme/eCommerce',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','auth_signup','base_setup','website'],

    # always loaded
    'data': [
        
        #Security file
        'security/ir.model.access.csv',

        #templates
        'templates/assets.xml',
        'templates/auth_user_pw_reset.xml',
        'templates/auth_user_signup.xml',
        'templates/site_user_login.xml',
        'templates/web_layout.xml',
        'templates/footer.xml', 
        'templates/header.xml',
        'templates/website_portal_language_selector.xml',

        #snippets
        'views/snippets/azeer_snippet_3.xml',
        'views/snippets/workflow_snippets.xml',
        'views/snippets/our_partners_snippets.xml',
        'views/snippets/form_snippets.xml',
        #'views/snippets/carousel.xml', 
        'views/snippets/working_process.xml',
        'views/snippets/snippets.xml',
        'views/snippets/carousel_duplicate.xml',

        #Views
        'views/login_image_view.xml',
        'views/res_config_settings_views.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'azeer_theme/static/src/css/style.css',
            'azeer_theme/static/src/css/custom_style.css',
            'azeer_theme/static/src/css/bootstrap.min.css',    
            'azeer_theme/static/src/css/bootstrap.min.css.map', 
            'azeer_theme/static/src/css/bootstrap/mixins/_badge.css',   
            'azeer_theme/static/src/css/bootstrap/mixins/_box-shadow.css',  
            'azeer_theme/static/src/css/bootstrap/mixins/_reset-text.css',  
            'azeer_theme/static/src/css/bootstrap/_media.css',  
            'azeer_theme/static/src/fonts/icomoon/style.css',   
            'azeer_theme/static/src/css/owl.carousel.min.css',  
            'azeer_theme/static/src/fonts/icomoon/fonts/icomoon.eot',   
            'azeer_theme/static/src/fonts/icomoon/fonts/icomoon.svg',   
            'azeer_theme/static/src/fonts/icomoon/fonts/icomoon.ttf',   
            'azeer_theme/static/src/fonts/icomoon/fonts/icomoon.woff',  
            # 'azeer_theme/static/src/js/jquery-3.3.1.min.js',  
            'azeer_theme/static/src/js/owl.carousel.min.js',    
            'azeer_theme/static/src/js/popper.min.js',  
            'azeer_theme/static/src/js/bootstrap.min.js',   
            'azeer_theme/static/src/js/jquery.sticky.js',   
            'azeer_theme/static/src/js/main.js',
        ]
    }
}
