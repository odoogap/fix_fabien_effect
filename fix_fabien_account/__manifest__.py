# -*- coding: utf-8 -*-
{
    'name': 'Fix Fabien Account',
    'version': '11.0.1.0',
    'author': 'Odoo Gap',
    'website': 'https://www.odoogap.com',
    'summary': 'Fix Fabien Account',
    'description': """
Fix Fabien Account
==================
- Enable full accounting features by default
- Change Invoicing menu name to Accounting
    """,
    'category': 'Accounting',
    'depends': ['account'],
    'data': [
        'data/res_config_settings_data.xml',
        'views/account_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
