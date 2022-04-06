
from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _rec_name = 'name'
    _description = "hospital.patient"
    _order = 'name'

    name = fields.Char('Patient Name', required=True, default=lambda self: self.env.user.name)
    image = fields.Binary("Image", copy=False)
    age = fields.Integer('Patient Age', default=1)
    contact = fields.Char('Patient Contact', copy=False)
    email = fields.Char('Patient Email', copy=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')])
    appointment_ids = fields.One2many('hospital.appointment', inverse_name='patient_id',
                                      string='Appointments', readonly=True)

    def copy(self, default=None):
        default = dict(default or {})
        default.update(name=_("%s (copy)") % (self.name or ''))
        return super(HospitalPatient, self).copy(default)

    @api.constrains('name')
    def _check_patient_contact(self):
        patient_contact = self.search([('contact', '=', self.contact)])
        if patient_contact:
            raise ValidationError(_('You cannot create recursive patient with same contact.'))

    # @api.depends('name', 'age')
    # def name_get(self):
    #     res = []
    #     for record in self:
    #         new_name = record.name + ' | ' + str(record.age)
    #         res.append((record.id, new_name))
    #     return res
