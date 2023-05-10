# TODO do not forget to update file in init of the model!

from odoo import api, exceptions, fields, models, _
from datetime import timedelta, datetime, date


class GymMembers(models.Model):
    _name = "gymwale.members"
    _description = "GymWale Members"
    _rec_name = "serial_number"
    _order = "serial_number"

    serial_number = fields.Char('Serial Number')
    image = fields.Binary("Image", copy=False)
    name = fields.Char('Name', required=True)
    age = fields.Integer('Age')
    contact = fields.Char('Contact', required=True, copy=False)
    aadhaar_number = fields.Integer('Aadhaar Number')
    address = fields.Text('Address')
    email = fields.Char('Email', copy=False)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string='Gender', required=True)
    emergency_contact = fields.Char('Emergency Contact', required=True, copy=False)
    emergency_contact_name = fields.Char('Emergency Person Name and Relation')
    prior_health_issue = fields.Selection([('yes', 'Yes'), ('no', 'No'), ('long', 'Long Time Ago')],
                                          required=True, string='Any Prior Health Issue?')
    objective = fields.Selection([('cardio', 'Cardio'), ('strength', 'Strength'), ('both', 'Both')],
                                 required=True, string='Objective')
    membership_plan = fields.Many2one('gymwale.membership_plan')
    amount_to_be_paid = fields.Integer(string='Amount to be Paid')
    is_amount_paid = fields.Boolean(string='Is Amount Paid?', compute='expiry_check')
    membership_assigned = fields.Date('Membership Assigned')
    membership_expire = fields.Date('Membership Expire')
    discount = fields.Integer('Discount')
    referral = fields.Many2one('gymwale.members')

    @api.depends('membership_expire')
    def expiry_check(self):
        for rec in self:
            rec.is_amount_paid = None
            if rec.membership_expire < date.today():
                rec.is_amount_paid = False

    @api.onchange('membership_plan', 'membership_assigned')
    def compute_expiry_date(self):
        self.membership_expire = False
        membership_period = self.membership_plan.membership_period
        if membership_period:
            self.membership_expire = self.membership_assigned + timedelta(days=membership_period)

    @api.onchange('membership_plan', 'discount')
    def compute_price(self):
        self.amount_to_be_paid = 0
        amount = self.membership_plan.membership_amount
        if amount:
            self.amount_to_be_paid = amount * (100 - self.discount) * 0.01

    @api.model
    def create(self, vals):
        """
        this function generates the unique appointment ids for each new appointment created
        :param vals:
        :return:
        """
        if not vals.get('serial_number'):
            vals['serial_number'] = self.env['ir.sequence'].next_by_code('gymwale.members') or _('New')
        res = super(GymMembers, self).create(vals)
        return res


