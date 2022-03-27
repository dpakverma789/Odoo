# -*- coding: utf-8 -*-

from odoo import models, fields, api

class student(models.Model):
    _name = 'school2.student'
    _rec_name = 'name'

    name = fields.Char(string="Name", required=True)
    roll_no = fields.Integer(string="Roll no", required=True)
    dob = fields.Date(string="DOB", required=True, )
    class_id = fields.Many2one(comodel_name="school2.class", string="Class", required=True, )

    # @api.depends('value')
    # def _value_pc(self):
    #   self.value2 = float(self.value) / 100

class Class(models.Model):
    _name = 'school2.class'
    _rec_name = 'name'

    name = fields.Char(string="Class", required=True, )
    subjects_ids = fields.Many2many(comodel_name="school2.subjects", string="Subjects", )

class subjects(models.Model):
    _name = 'school2.subjects'
    _rec_name = 'name'

    name = fields.Char(string="Subject", required=True, )

class exams(models.Model):
    _name = 'school2.exam'
    _rec_name = 'student_id'
    student_id = fields.Many2one(comodel_name="school2.student", string="Student", required=True, )
    class_id = fields.Many2one(comodel_name="school2.class", string="Class", readonly=False, required=True, )
    subjects_ids = fields.Many2one(comodel_name="school2.subjects", string="Subjects", required=True, )
    marks = fields.Float(string="Marks",  required=True)