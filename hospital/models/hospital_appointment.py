
from odoo import api, fields, models, tools, _
from datetime import timedelta
from odoo.exceptions import ValidationError


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'patient_id'
    _description = "hospital.appointment"

    name = fields.Char('Appointment', required=True, copy=False, readonly=True, default=lambda self: _('New'))
    patient_id = fields.Many2one('hospital.patient', 'Patient Name', required=True)
    patient_gender = fields.Char('Gender')
    doctor_id = fields.Many2one('hospital.doctor', 'Doctor Name', required=True)
    doctor_specialization = fields.Char('Specialization', related='doctor_id.doctor_specialization')
    appointment_time = fields.Datetime('Appointment Time', required=True)
    appointment_state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"),
                                          ('rejected', "Rejected")], string="Appointment Status", default='draft')
    rejection_id = fields.Many2one('appointment.rejection.reason', 'Rejection Reason', readonly=True)
    patient_description = fields.Text('Description')

    def confirm_appointment(self):
        all_appointment_ids = self.search([('id', '!=', self.id), ('appointment_state', '=', 'confirmed'),
                                           ('doctor_id', '=', self.doctor_id.id)])
        for rec in all_appointment_ids:
            conditions = (
                    self.appointment_time > rec.appointment_time + timedelta(minutes=15),
                    rec.appointment_time < self.appointment_time - timedelta(minutes=15)
            )
            if not all(conditions):
                raise ValidationError(_('Already have Appointment!, Try 15 min Later'))
        self.appointment_state = 'confirmed'

    # overriding delete function to check condition before deleting records
    def unlink(self):
        for rec in self:
            if rec.appointment_state == 'confirmed':
                raise ValidationError(_('Can not Delete Confirmed Appointment'))
        return super(HospitalAppointment, self).unlink()

    # overriding create method [vals are all fields from current model]
    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name'] = self.env['ir.sequence'].next_by_code('hospital.appointment') or _('New')
        res = super(HospitalAppointment, self).create(vals)
        return res

    # printing report
    def print_patient_appointment_card(self):
        return self.env.ref('hospital.patient_appointment_report').report_action(self)

    # onchange function which depends on patient_id to change patient gender
    @api.onchange('patient_id')
    def _onchange_patient_gender(self):
        if self.patient_id and self.patient_id.patient_gender:
            self.patient_gender = self.patient_id.patient_gender

    # wizard call using python function
    def rejection_reason_wizard(self):
        wizard_view = {
            'name': _('Rejection Reason'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'view_type': 'form',
            'res_model': 'hospital.appointment.request.wizard',
            'view_id': self.env.ref('hospital.hospital_appointment_request_wizard').id,
            'target': 'new',
        }
        return wizard_view
