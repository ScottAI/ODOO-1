# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Sale Revision',
    'version': '1.1',
    'summary': 'Create Revision and Apply Revision',
    'author': 'FOSS INFOTECH',
    'category': 'Sale',
    'website': 'http://www.fossinfotech.com',
    'description': """ 
                This module adds a functionality to manage different revisions and can be rolled back to any revision at anytime in Sales order.
                """,
    'depends': [
        'sale',
    ],
    'data': [
        'views/sale_view.xml',
    ],
    'images': [
        'static/description/icon.png',
        'static/description/index.html',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
