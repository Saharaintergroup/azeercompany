# -*- coding: utf-8 -*-
{
    'name': "Azeer Theme",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Sahara International Group",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Theme',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website', 'web', 'portal', 'auth_signup'],

    # always loaded
    'data': [
        'views/assets.xml',
        'views/nav.xml',
        'views/index.xml',
        'views/aboutus.xml',
        'views/laboratorymedicine.xml',
        'views/cinicalservies.xml',
        'views/radiology.xml',
        'views/pathology.xml',
        # 'views/full_screen.xml',

        'views/contact_us.xml',
        'views/footer.xml',
        'views/auth/login.xml',
        'views/auth/signup.xml',
        'views/auth/reset_password.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            '/theme_azeer/static/src/css/bootstrap.css',
            "https://fonts.googleapis.com/css2?family=Roboto:wght@400;500;700;900&display=swap",
            '/theme_azeer/static/src/css/font-awesome.min.css',
            '/theme_azeer/static/src/css/style.css',
            '/theme_azeer/static/src/css/responsive.css',
            '/theme_azeer/static/src/css/custom.css',
            '/theme_azeer/static/src/css/recustom.css',
            "https://fonts.cdnfonts.com/css/nexa-bold",
        ],


    },
    'images': [
        'static/src/description/icon.png',
    ],

}
