# -*- coding: utf-8 -*-
{
    'name': "App one",
    'license': 'LGPL-3',
    'application': True,
    'sequence':1,
    'summary': "Short summary",
    'author': "Ayman Gamal",
    'category': 'Uncategorized',
    'version': '17.0.0.1.0',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/property_views.xml',
        'views/owner_views.xml',
        'views/menu.xml',
    ],
    # 'assets': {
    #     'web.assets_backend': ['app_one/static/src/css/property.css']
    # },
    'demo': [
        'demo/demo.xml',
    ],
}

