'''
Author: 27
LastEditors: 27
Date: 2024-03-12 12:35:43
LastEditTime: 2024-03-12 16:45:51
FilePath: /odoo/third_party/xbh_supplier/__manifest__.py
description: type some description
'''
# -*- coding: utf-8 -*-
{
    'name': "xbh_supplier",

    'summary': "鑫博海供应商",

    'description': """
Long description of module's purpose
    """,

    'author': "F27",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    # 'category': 'Uncategorized',
    'category': 'Customer',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'base'
    ],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/templates.xml',
        'views/category.xml',
        # 'views/views.xml',
        # 'views/xbh_supplier_views.xml',
        'views/xbh_supplier_views2.xml',
    ],
    # only loaded in demonstration mode
    # 'demo': [
    #     'demo/demo.xml',
    # ],
}

