
#this manifest file tells about App information details
{
    #user readble module name
    'name': 'Student Management',  #mendatory, user can see it
    'version':'2.0',
    'category':'management',   #category by default it is unknown
    'summary':'Student Management',
    'description':'This app helps to manage the student data management',  #description for user
    'sequence':'2',   #priortize sequence in app store
    'author':'Deepak Verma',
    'maintainer':'Deepak Verma',
    'website':'deepakverma.com',
    #depends,demo,data is of list type
    'depends':['base','website'], #module which must load before this module
    'demo':[],
    #xml and csv file are define in data   'folder/file.xml'
    'data':['views/student_class.xml',
            'views/student_subject.xml',
            'views/student_hobby.xml',
            'views/page_template.xml',
            'views/student_fee.xml',
            'security/ir.model.access.csv',
            'security/student_security_rule.xml'],
            #'reports/patient_appointment_report.xml', 'reports/student_card.xml',

    'installble':True,            #this makes it installable
    'application':True,            #this makes this manifest as an app
    'auto_install':False,
}