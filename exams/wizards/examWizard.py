
from odoo import models, fields, api

class examWizard(models.TransientModel):
    _name = 'exam.wizard'

    student_name = fields.Char('name')
    student_class = fields.Char('class')
    student_subject = fields.Char('subject')


    def print_report(self):
        data = {'model':'exam.wizard',"form" : self.read()[0]}
        print('data',data)
        print('student Name =',data['form']['student_name'])
        print('student Class =',data['form']['student_class'])
        print('student Subbject =',data['form']['student_subject'])
        return self.env.ref("exams.exam_marks_card").report_action(self, data=data)

    # def print_report(self):
    #     data = {
    #         'ids': self.ids,
    #         'model': self._name,
    #         'form':
    #             {
    #                 'student_name': self.student_name,
    #                 'student_class': self.student_class,
    #                 'student_subject': self.student_subject,
    #             }, }
    #     print('data', data)
    #     return self.env.ref("exams.exam_marks_card").report_action(self, data=data)


