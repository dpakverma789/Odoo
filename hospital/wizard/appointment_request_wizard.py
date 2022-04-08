
from odoo import models, fields, api
from datetime import datetime, timedelta


class AppointmentRequestWizard(models.TransientModel):
    _name = 'hospital.appointment.request.wizard'

    rejection_reason = fields.Many2one('appointment.rejection.reason', 'Rejection Reason', required=True)

    def reject_appointment(self):
        rejection_id = self.env['hospital.appointment'].browse(self._context.get("active_id"))
        if rejection_id:
            rejection_id.rejection_id = self.rejection_reason
            rejection_id.appointment_state = 'rejected'
        else:
            now = datetime.now()
            discard_appointments = self.env['hospital.appointment'].search([('appointment_state', '=', 'draft')])
            rejection_reason = self.env['appointment.rejection.reason'].search([('rejection_reason', '=', 'Discard by Bot')])
            for rec in discard_appointments:
                if rec.create_date + timedelta(days=2) < now:
                    rec.rejection_id = rejection_reason.id
                    rec.appointment_state = 'rejected'

