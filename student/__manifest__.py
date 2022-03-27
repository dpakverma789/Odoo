
#this manifest file tells about App information details

{
    #user readble module name
    'name': 'Student details',  #mendatory
    'version':'1.0',
    'category':'distribution',   #category by default it is unknown
    'summary':'student data',
    'description':'This module helps in storing student data in schools',  #description for user
    'sequence':'1',   #priortize sequence in app store
    'author':'Deepak Verma',
    'maintainer':'Deepak Verma',
    'website':'demo.com',
    #depends,demo,data is of list type
    'depends':['base'], #module which must load before this module
    'demo':[],
    #xml and csv file are define in data   'folder/file.xml'
    'data':[
            'views/student.xml',
            'security/ir.model.access.csv',
            ],
    'installble':True,          #this makes it installable
    'application':True,            #this makes this manifest as an app
    'auto_install':False,
}