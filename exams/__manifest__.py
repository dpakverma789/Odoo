

#this manifest file tells about App information details
{
    #user readble module name
    'name': 'Exams',  #mendatory, user can see it
    'version': '1.0',
    'category': 'management',   #category by default it is unknown
    'summary': 'Student Exams Management',
    'description': 'This app helps to manage the student exams marks',  #description for user
    'sequence': '1',   #priortize sequence in app store
    'author': 'Deepak Verma',
    'maintainer': 'Deepak Verma',
    'website': 'deepakverma.com',
    #depends,demo,data is of list type
    'depends': ['base'], #module which must load before this module
    'demo': [],
    #xml and csv file are define in data 'folder/file.xml'
    'data': [
        'views/exams.xml',
        'views/student.xml',
        'views/subject.xml',
        'security/ir.model.access.csv',
        'wizard/examWizard.xml',
        'reports/exam_card.xml',
        'reports/patient_appointment_report.xml',
            ],
    'installble': True,            #this makes it installable
    'application': True,            #this makes this manifest as an app
    'auto_install': False,
}