# -*- coding: utf-8 -*-
{
    'name': "Alazeer Accounting",

    'depends': ['base','account','sale', 'purchase'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_invoice_report.xml',
        'views/sale_invoice_report.xml',

    ],

}
