
from odoo import api, fields, models, tools, _


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = 'name'
    _description = "hospital.patient"
    _order = 'name'

    name = fields.Char('Patient Name', required=True, default=lambda self: self.env.user.name)
    image = fields.Binary("Image")
    age = fields.Integer('Patient Age')
    contact = fields.Char('Patient Contact')
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    appointment_ids = fields.One2many('hospital.appointment', inverse_name='patient_id',
                                      string='Appointments', readonly=True)
