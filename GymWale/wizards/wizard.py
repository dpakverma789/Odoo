# TODO do not forget to update file in init of the wizard!

from odoo import api, exceptions, fields, models, _


class AppointmentRequestWizard(models.TransientModel):
    _name = "module.name"
    _inherit = ['module.name']
    _description = "module description"

