# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'school2.wizard'
    _description = "Wizard: Quick Registration of Exam to Sessions"

    student_id = fields.Many2one(comodel_name="school2.student", string="Student", required=True, )
    class_id = fields.Many2one(comodel_name="school2.class", string="Class", readonly=False, required=True)
    subjects_ids = fields.Many2one(comodel_name="school2.subjects", string="Subjects", required=True, )
    marks = fields.Float(string="Marks",  required=True)

    @api.onchange('student_id')
    def _onchange_ids(self):
        self.class_id = self.student_id.class_id
        # self._fields.get('class_id').readonly = True
        return {
                     'domain': {
                         'subjects_ids': [('id', 'in', self.class_id.subjects_ids.ids)]
                     },
                }

    def copyy(self):
        self.env['school2.exam'].create({
            'student_id': self.student_id.id,
            'class_id': self.class_id.id,
            'subjects_ids': self.subjects_ids.id,
            'marks': self.marks,
        })
        return