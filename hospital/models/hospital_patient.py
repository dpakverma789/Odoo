
from odoo import api, fields, models, tools, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = 'patient_name'
    _description = "hospital.patient"

    patient_name = fields.Char('Patient Name', required=True, default='Odoo')
    patient_age = fields.Integer('Patient Age')
    patient_contact = fields.Char('Patient Contact')
    patient_gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    appointment_ids = fields.One2many('hospital.appointment', inverse_name='patient_id',
                                      string='Appointments', readonly=True)
    patient_image = fields.Binary("Image")
