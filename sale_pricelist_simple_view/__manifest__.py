# -*- coding: utf-8 -*-
{
    'name': "ECOD3 - Ativa exibição de lista de preço no produto",
    'summary': """Ativa a exibição de todos preços calculado pela 
     lista de preço nas visualizações do produto.""",
    'description': """   """,

    "author": "ECOD3",
    "website": "https://ecod3.com",
    "license": "LGPL-3",
    'contributors': [
        'Gabriel Conceição <gsouza@ecod3.com>',
    ],

    'category': 'sale',
    'version': '0.1',

    'depends': [
          'sale',
    ],
    'data': [
        'views/sale_pricelist_simple_pricelist_view.xml',
        'views/sale_pricelist_simple_product_view.xml',
        'security/security.xml',
    ]
}
