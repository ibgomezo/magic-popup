# -*- coding: utf-8 -*-
{
    'name': "Magic Popup",

    'summary': """
        Set of popup windows to show messages and control the code flow on user actions""",

    'description': """
        This module provide a set of views and models targeted to developers that wants show popup messages
        on wizards and control the code flow depending on user's action.
    """,

    'author': "Ibrian Gomez Ortiz",
    'website': "http://www.geneos.com.ar",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/11.0/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Development',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/confirm_cancel_popup_views.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}