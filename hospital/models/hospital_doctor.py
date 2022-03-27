
from odoo import api, fields, models, tools, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _rec_name = 'doctor_name'
    _description = "hospital.doctor"

    doctor_name = fields.Char('Doctor Name', required=True)
    doctor_specialization = fields.Char('Specialization', required=True)
    patient_appointment_ids = fields.One2many('hospital.appointment', inverse_name='doctor_id',
                                              string='Appointments', readonly=True)
