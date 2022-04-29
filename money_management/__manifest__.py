{
    "name": "Money Management",
    'summary': "Money Management.",
    'description': """Money Management""",
    'author': "Deepak Verma",
    'website': "",
    'maintainer': 'Deepak Verma',
    'support': 'Deepak Verma',
    'version': '1.0.0',
    'depends': ['base', 'website', 'mail'],
    'data': [
        # security files
        'security/ir.model.access.csv',

        # wizard files


        # reports files


        # data files

        # views files
        'views/expense_category.xml',
        'views/expense_transaction.xml',
        'views/credit_card_manager.xml'

    ],
    'demo': [
        # demo data files

    ],
    'qweb': [],
    'sequence': '1',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3'
}