{
    "name": "Sale Order Lot Selection",
    "version": "15.0.2.0.0",
    "category": "Sales Management",
    "author": "Odoo Community Association (OCA), Agile Business Group",
    "website": "https://github.com/OCA/sale-workflow",
    "license": "AGPL-3",
    "depends": ['sale',"sale_stock"],
    "data": ["view/sale_view.xml",
             "view/stock_move_line.xml"],
    "maintainers": ["bodedra"],
    "installable": True,
}
