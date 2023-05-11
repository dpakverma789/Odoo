{
    'name': 'GymWale',
    'version': '1.0',
    'summary': 'GymWale',
    'sequence': 1,
    'description': """This module is for GymWale""",
    'category': 'Extra Tools',
    'website': 'https://gymwale.vercel.app/',
    'images': [],
    'depends': ['base'],
    'data': [
        # security
        'security/ir.model.access.csv',

        # views
        'views/gymwale_members.xml',
        'views/gymwale_membership_plan.xml',
        'views/menus.xml',

        # wizard

        # data
        'data/members_serial_code.xml',

        # demo data files
    ],
    'qweb': [
        # qweb templates
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
