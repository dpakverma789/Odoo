
from odoo import api, fields, models, tools, _


class HospitalDoctor(models.Model):
    _name = "hospital.doctor"
    _rec_name = 'name'
    _description = "hospital.doctor"
    _order = 'name'

    name = fields.Char('Doctor Name', required=True)
    image = fields.Binary("Image")
    specialization = fields.Char('Specialization', required=True)
    total_appointment = fields.Integer('Total Appointment', compute='_compute_total_appointment')
    active = fields.Boolean('Active', default=True)
    patient_appointment_ids = fields.One2many('hospital.appointment', inverse_name='doctor_id',
                                              string='Appointments', readonly=True)

    @api.depends('patient_appointment_ids')
    def _compute_total_appointment(self):
        if self.patient_appointment_ids:
            appointment_count = self.patient_appointment_ids.filtered(lambda rec: rec.appointment_state == 'confirmed')
            if appointment_count:
                self.total_appointment = len(appointment_count.ids)
                return
        self.total_appointment = 0

    def copy(self, default=None):
        default = dict(default or {})
        default.update(name=_("%s (copy)") % (self.name or ''))
        return super(HospitalDoctor, self).copy(default)

