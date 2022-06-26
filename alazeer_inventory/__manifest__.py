# -*- coding: utf-8 -*-
{
    'name': "Alazeer Inventory",

    'depends': ['base','stock','product_expiry','stock_barcode'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/product_barcode.xml',
        'views/stock_move_line.xml',

    ],

}
