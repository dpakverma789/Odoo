{
    "name": "Hospital Management",
    'summary': "Hospital Management.",
    'description': """Hospital Management""",
    'author': "Deepak Verma",
    'website': "",
    'maintainer': 'Deepak Verma',
    'support': 'Deepak Verma',
    'version': '1.0.0',
    'depends': ['base', 'website', 'mail'],
    'data': [
        # security files
        'security/security.xml',
        'security/ir.model.access.csv',

        # wizard files
        'wizard/appointment_request_wizard.xml',

        # reports files
        'reports/patient_appointment_report.xml',
        'reports/patient_appointment_email_template.xml',

        # data files
        'data/appointment_sequence.xml',
        'data/cron.xml',

        # views files
        'views/patient_form_template.xml',
        'views/hospital_patient.xml',
        'views/hospital_appointment.xml',
        'views/hospital_doctor.xml',
        'views/rejection_reason.xml',
        'views/patient_class_status.xml',
    ],
    'demo': [
        # demo data files
        'demo/base_data.xml',
        'demo/demo_data.xml'
    ],
    'qweb': [],
    'sequence': '1',
    'installable': True,
    'application': True,
    'auto_install': False,
}