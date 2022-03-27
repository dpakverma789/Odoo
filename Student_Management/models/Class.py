# class model
from odoo import models, fields, api
from odoo.exceptions import AccessError, RedirectWarning, UserError
from odoo import exceptions
import pytz
from datetime import datetime


class Student(models.Model):
    _name = 'student.student'
    _description = 'Student-Student'
    _rec_name = 'studentName'
    _order = 'rollNumber'

    # class model variable
    studentName = fields.Char('Name', required=True, default=lambda self: self.env.user.name)
    studentClass = fields.Integer('Class', required=True, default=10)
    rollNumber = fields.Char('RollNumber')
    note = fields.Boolean('Student Note?')
    date = fields.Datetime('date')
    description = fields.Text('Description')

    # Many2one('co-model-name', string='label')
    stream_id = fields.Many2one('student.subject', 'Stream')
    fee_id = fields.Many2one('student.fee', 'Fee')


    # Many2many('model2-name', 'model1_model2_rel','column_from_model1,column_from_model2')
    hobby_ids = fields.Many2many('student.hobby', 'student_hobby_rel', 'student_id', 'hobby_id')

    # def create_new(self):
    #     val = {'studentName': self.studentName,
    #            'studentClass': self.studentClass,
    #            'stream_id': self.stream_id.id,
    #            'fee_id': self.fee_id.id}
    #     new_record = self.env['student.student']
    #     if not new_record.exists():
    #         new_record.create(val)
    #     else:
    #         raise exceptions.ValidationError('This Record do not exist!')
    #     return

    def delete_new(self):
        new_record = self.env['student.student'].search([('id', '=', self.id)])
        if new_record.exists():
            new_record.unlink()
        else:
            raise exceptions.Warning('Already Deleted!')
        return

    def wizard(self):
        return {
            'name': 'Hobby',
            'type': 'ir.actions.act_window',
            'res_model': 'student.hobby',
            'view_type': 'form',
            'view_mode': 'form',
            'target': 'new'}

# Overriding create button function in student.student model
class InheritStudent(models.Model):
    _inherit = 'student.student'

    # @api.model
    def create(self, vals_list):
        res = super(Student, self).create(vals_list)
        res=self.env['student.student'].browse(res.id)
        print(res)
        return res

    def write(self, vals_list):
        print(vals_list)
        res = super(Student, self).write(vals_list)
        print(res)
        return res

    # Mapped Function (to get the specific field from model)
    # def create_new(self):
    #     record  = self.env['student.student'].search([])
    #     mapp=record.mapped('stream_id.studentSubject')
    #     print(mapp)

    # # Sorted Function (sort the record bases on key passed)
    # def create_new(self):
    #     record  = self.env['student.student'].search([])
    #     sort=record.sorted(key=lambda x:x.id)
    #     print(sort)

    # Filtered Function (filter based on passed key or condition)
    def create_new(self):
        record = self.env['student.student'].search([])
        filt = record.filtered(lambda x: x.stream_id.studentSubject == 'Science')
        print(filt)
        return filt

    # Mixed function (sorted,mapped,filter)
    # def create_new(self):
    #     record = self.env['student.student'].search([])
    #     rec=record.sorted(key=lambda n:n.studentName)
    #     filt = rec.filtered(lambda x: x.stream_id.studentSubject == 'Science').mapped('studentName')
    #     print(filt)

class Subject(models.Model):
    _name = 'student.subject'
    _description = 'Student-Subject'
    _rec_name = 'studentSubject'
    _order = 'studentSubject'

    # class model variable
    studentSubject = fields.Char('Stream', required=True)  # subject: science/commerce/bio

    # One2many('co-model-name' , inverse_name = 'field_name(Many2one)' , string='label' )
    student_ids = fields.One2many('student.student', inverse_name='stream_id', string='student details')

class Fee(models.Model):
    _name = 'student.fee'
    _description = 'Student-Fee'
    _rec_name = 'studentFee'

    # class model variable
    studentFee = fields.Integer('Fee', required=True)

    # One2many('co-model-name' , inverse_name = 'field_name(Many2one)' , string='label' )
    class_ids = fields.One2many('student.student', inverse_name='fee_id', string='student details')

class Hobby(models.Model):
    _name = 'student.hobby'
    _order = 'hobby'
    _rec_name = 'hobby'

    student_name = fields.Char('Name')
    hobby = fields.Char('Hobby')



