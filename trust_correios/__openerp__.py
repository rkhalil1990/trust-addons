# -*- coding: utf-8 -*-
# © 2016 Alessandro Fernandes Martini, Trustcode
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': "Trust Correios",
    'summary': """Integração com os Correios""",
    'description': """Módulo para gerar etiquetas de rastreamento de \
encomendas""",
    'version': '8.0',
    'category': 'MRP',
    'author': 'Trustcode',
    'license': 'AGPL-3',
    'website': 'http://www.trustcode.com.br',
    'contributors': ['Mackilem Van der Laan Soares <mack.vdl@gmail.com>',
                     'Danimar Ribeiro <danimaribeiro@gmail.com>',
                     'Alessandro Fernandes Martini \
<alessandrofmartini@gmail.com>'
                     ],
    'depends': ['stock', ],
    'data': [
        'views/trust_correios.xml',
    ],
    'application': True,
}