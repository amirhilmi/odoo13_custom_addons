# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'School Management',
    'version': '13.0.0.0.1',
    'category': 'Extra Tools',
    'summary': 'School record',
    'sequence': '2',
    'author': 'Aamir',
    'license': 'LGPL-3',
    'company': 'TCM',
    'maintainer': 'TCM',
    'support': 'amir.hi575@gmail.com',
    'website': '',
    'depends': ['base','mail'],
    'live_test_url': '',
    'demo': [],
    'data': [
        # 'security/ir.model.access.csv',
        'views/student.xml'


    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    # 'images': ['images/accounts.jpeg'],
    'qweb': [],
}