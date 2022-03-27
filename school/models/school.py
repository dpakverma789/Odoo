import datetime
from odoo import models, fields, api
# with one2many it is mandatory to make many2one
# we can use many2one without one2many fields
# Many2many(co_model_name, new_table_name_rel, 'column1' ,'column2')


#  SUBJECT MODEL
class Subject(models.Model):
    _name = 'school.subject'
    _rec_name = 'subject_name'

    subject_name = fields.Char('Subject Name')
    subject_code = fields.Char('Subject Code')
    toggle = fields.Boolean('toggle')

    # _sql_constraints = [('Any_name', 'unique (your_field_name)', 'Your message!')]
    _sql_constraints = [('unique_subject_code', 'unique (subject_code)', 'Subject code already exist!')]


# CLASS MODEL
class Class(models.Model):
    _name = 'school.class'
    _rec_name = 'class_name'

    class_name = fields.Char('Class Name')
    class_code = fields.Char('Class Code')


# CLASS- SUBJECT MODEL
class subjectClass(models.Model):
    _name = 'school.class.subject'
    _rec_name ='subject_id'

    subject_id = fields.Many2one('school.subject', string='Subject')
    class_id = fields.Many2one('school.class', string='Class')
    division_id = fields.Many2one('school.division', string='Division_Id')
    maximum_marks = fields.Integer('Maximum Marks')


# DIVISION MODEL
class Division(models.Model):
    _name = 'school.division'
    _rec_name = 'division_name'

    division_name = fields.Char('Division Name')
    class_id = fields.Many2one('school.class', string='class_Id')
    subject_ids = fields.One2many('school.class.subject', inverse_name='division_id', string='subject_ids')


# STUDENT-SUBJECT MODEL
class studentSubject(models.Model):
    _name = 'school.student.subject'
    _rec_name = 'subject_id'

    subject_id = fields.Many2one('school.subject', string='Subject')
    subject_class_id = fields.Many2one('school.student.class', string='Student Class Id')


# SCHOOL-YEAR MODEL
class schoolYear(models.Model):
    _name = 'school.year'
    _rec_name = 'start_date'

    student_name = fields.Char('Student Name')
    start_date = fields.Date('Start-date')
    end_date = fields.Date('End-date')
    is_current = fields.Char('Current Studing', compute='check_is_current')

    @api.depends('start_date','end_date')
    def check_is_current(self):
        today_date = datetime.date.today()
        for x in self:
            if x.start_date and x.end_date and (today_date >= x.start_date) and (today_date <= x.end_date):
                x.is_current ='Still Studing'
            elif (today_date <= x.start_date) and not x.end_date:
                x.is_current = 'Still Studing'
            else:
                x.is_current = 'Not Studing'


# EXAM MODEL
class Exams(models.Model):
    _name = 'school.exams'
    _rec_name = 'exam_name'

    exam_name = fields.Char('Exam Name')
    class_subject = fields.Many2one('school.class.subject', string='Exam for class')
    school_year = fields.Char('Current year',compute='current_year')

    def current_year(self):
        today_date = datetime.date.today().year
        for i in self:
            i.school_year = today_date


# STUDNET-EXAM MODEL
class studentExam(models.Model):
    _name = 'school.student.exam'
    _rec_name = 'subject_id'
    _order = 'student_name asc'

    student_name = fields.Char('Student Name')
    subject_id = fields.Many2one('school.class.subject', string='subject')
    Student_Class_id = fields.Many2one('school.student.class', string='Class')
    marks = fields.Integer('Marks')


# STUDENT MODEL
class Student(models.Model):
    _name = 'school.student'
    _rec_name = 'student_name'

    roll_no = fields.Char('Roll No.')
    student_name = fields.Char('Student Name')
    date_of_birth = fields.Date('D.O.B')
    age = fields.Char('Age', compute='get_age_from_student')
    street = fields.Char('Street')
    zip = fields.Char('Zip')
    city = fields.Char('City')
    state_id = fields.Many2one("res.country.state", string='State')
    country_id = fields.Many2one('res.country', string='Country')
    parent_name = fields.Many2many('res.partner',string='parent-name')
    student_history_ids = fields.One2many('school.student.class', inverse_name='history_id',string='history-id')

    # D.O.B to age converter
    @api.depends('date_of_birth')
    def get_age_from_student(self):
        today_date = datetime.date.today()
        for student in self:
            if student.date_of_birth:
                date_of_birth = fields.Datetime.to_datetime(student.date_of_birth).date()
                get_age = str(int((today_date - date_of_birth).days / 365))
                student.age = get_age
            else:
                student.age = 'D.O.B not provided'


 # STUDENT-CLASS MODEL   (create new xml)
class studentClass(models.Model):
    _name = 'school.student.class'
    _rec_name = 'student_id'

    student_id = fields.Many2one('school.student', string='student_student_id')
    class_id = fields.Many2one('school.class', string='class-id')
    division_id = fields.Many2one('school.division', string='division-id')
    subject_ids = fields.One2many('school.student.subject', inverse_name='subject_class_id',string='student-subject-id')
    history_id = fields.Many2one('school.student',string='history-id')





