from odoo import models, fields, api


# STUDENT WIZARD
class StudentClass(models.TransientModel):
    _name = 'student.class.wizard'

    student_id = fields.Many2one('school.student', string='student_student')
    class_id = fields.Many2one('school.class', string='class')
    division_id = fields.Many2one('school.division', string='division')

    def add_subject(self):
        self.env['school.student.class'].create({
            'student_id': self.student_id.id,
            'class_id': self.class_id.id,
            'division_id': self.division_id.id
        })
        return True


class StudentDivision(models.TransientModel):
    _name = 'student.exam.wizard'

    student_name = fields.Char('Student Name')
    subject_id = fields.Many2one('school.class.subject', string='subject_id')
    Student_Class_id = fields.Many2one('school.student.class', string='Student_Class_id')
    marks = fields.Integer('Marks')

    def add_exam(self):
        self.env['school.student.exam'].create({
            'student_name': self.student_name,
            'subject_id': self.subject_id.id,
            'Student_Class_id': self.Student_Class_id.id,
            'marks': self.marks,
        })
        return True
