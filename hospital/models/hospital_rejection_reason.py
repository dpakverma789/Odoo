
from odoo import api, fields, models, tools, _


class AppointmentRejectionReason(models.Model):
    _name = 'appointment.rejection.reason'
    _rec_name = 'rejection_reason'

    rejection_reason = fields.Char('Rejection Reason')
