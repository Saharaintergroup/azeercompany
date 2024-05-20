# -*- coding: utf-8 -*-
{
    'name': "Alazeer Quotation Report",

    'summary': """
        custom report""",

    'description': """
    """,

    'author': "Leo ateniese",
    'website': "http://www.etanish.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Customizations',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'assets': {
        'web.report_assets_common': [
              'alazeer_quotation_report/static/src/img/**/*'
        ],
        'web.report_assets_pdf': [
              'alazeer_quotation_report/static/src/img/**/*'
         ]
    },
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
