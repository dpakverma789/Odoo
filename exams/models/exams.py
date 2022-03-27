
from odoo import models, fields


class student(models.Model):
    _name = 'student.data'
    _description = 'student.data'
    _rec_name    = 'studentName'

    studentName = fields.Char('Name')
    studentClass = fields.Integer('Class')

    subject_id = fields.Many2one('student.sub',string='subjects')
    marks_id = fields.Many2one('student.exams',string='marks')


class exams (models.Model):
    _name = 'student.exams'
    _description = 'student.exams'
    _rec_name = 'mark_subject_1'

    mark_subject_1 = fields.Integer('subject marks')
    student_ids = fields.One2many('student.data', inverse_name='marks_id', string='student')


class subject(models.Model):
    _name = 'student.sub'
    _description = 'student.sub'
    _rec_name = 'subject1'

    subject1 = fields.Char('Subject')

    student_marks_ids = fields.One2many('student.data',inverse_name='subject_id',string='studentMarks')











