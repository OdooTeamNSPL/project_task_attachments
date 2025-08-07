{
    "name": " Project & Task File Attachments",
    "version": "17.0",
    'summary': """This module Allows User to View the Attached Project and Task Documents Separately.""",
    'description': """
        This module  Allows User to View the Attached Project and Task Documents Separately.
        
        ✔ Project and Task Documents are available under separate menus in Project module.
        ✔ New files can be directly attached to Projects and Tasks from the new Documents menu.
        ✔ Attachments are available in List, Kanban and Form view.
    """,
    'category': 'Project',
    'sequence': 2,
    'author': 'Namah Softech Private Limited',
    'website': 'http://namahsoftech.com/',
    'license': 'OPL-1',
    'price': 9.99,
    'currency': 'USD',
    'support': 'support@namahsoftech.com',
    'contributors': ["Rutik Patil"],
    'depends': ['project'],

    "data": [
        'views/ir_attachment_views.xml',
    ],
    'images': ['static/description/img/banner.png'],
    'installable': True,
    'auto_install': False,
    'application': False,

}
