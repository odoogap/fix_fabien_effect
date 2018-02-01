# -*- coding: utf-8 -*-
{
    'name': 'Fix Fabien MRP',
    'version': '11.0.1.0',
    'author': 'Odoo Gap',
    'website': 'https://www.odoogap.com',
    'summary': 'Fix Fabien MRP',
    'description': """
Fix Fabien MRP
==============
- Fix work orders option in MRP settings
    """,
    'category': 'Manufacturing',
    'depends': ['mrp'],
    'data': [
        'views/res_config_settings_views.xml',
    ],
    'demo': [
    ],
    'test': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
