
from odoo import models, fields, api


class AppointmentRequestWizard(models.TransientModel):
    _name = 'hospital.appointment.request.wizard'

    rejection_reason = fields.Many2one('appointment.rejection.reason', 'Rejection Reason')

    def reject_appointment(self):
        rejection_id = self.env['hospital.appointment'].browse(self._context.get("active_id"))
        if rejection_id:
            rejection_id.rejection_id = self.rejection_reason
            rejection_id.appointment_state = 'rejected'
