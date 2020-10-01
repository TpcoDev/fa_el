# -*- coding: utf-8 -*-
{
    'name': "TPCO Project Template",
    'category': 'TPCO',
    'version': '1.0.1',
    'author': "tpco",
    'website': 'www.tpco.cl',
    "support": "tpco@tpco.cl",
    'summary': """
        TPCO Project""",
    'description': """
        TPCO Project
    """,
    "images": [],
    "depends": [
        "website_sale","sh_request_quote_multiple"
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/as_template.xml',
        'views/assets.xml',
    ],
    'qweb': [
    ],
    # 'demo': [
    #     'demo/demo.xml',
    # ],
    'installable': True,
    'auto_install': False,
    
}