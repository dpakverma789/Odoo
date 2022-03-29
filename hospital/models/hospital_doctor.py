
from odoo import api, fields, models, tools, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _rec_name = 'doctor_name'
    _description = "hospital.doctor"
    _order = 'doctor_name'

    doctor_name = fields.Char('Doctor Name', required=True)
    doctor_specialization = fields.Char('Specialization', required=True)
    patient_appointment_ids = fields.One2many('hospital.appointment', inverse_name='doctor_id',
                                              string='Appointments', readonly=True)
    total_appointment = fields.Integer('Total Appointment', compute='_compute_total_appointment')
    doctor_image = fields.Binary("Image")

    @api.depends('patient_appointment_ids')
    def _compute_total_appointment(self):
        if self.patient_appointment_ids:
            appointment_count = self.patient_appointment_ids.filtered(lambda rec: rec.appointment_state == 'confirmed')
            if appointment_count:
                self.total_appointment = appointment_count.ids.__len__()
        else:
            self.total_appointment = 0
