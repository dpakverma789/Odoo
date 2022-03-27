
#models are define here

from odoo import models, fields
class student(models.Model):
    _name='first.student'    #name should be in lower case seperated by . operator
    _description='First student'   # model description

    #variableName =fields.datatype(argument)
    studentfirstName=fields.Char(string='Name',required=True) #it can not be empty
    studentlastName=fields.Char('surName')
    studentId=fields.Integer('Id')
    studentRemark=fields.Text('remark')
