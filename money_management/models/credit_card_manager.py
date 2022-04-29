from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class CreditCardManager(models.Model):
    _name = "credit.card.manager"
    _rec_name = 'name'
    _description = "credit.card.manager"
    _order = 'name'

    name = fields.Char(string='Credit Card', required=True)
    currency_id = fields.Many2one('res.currency', string='Amount Currency')
    amount = fields.Monetary(string='Amount Due')
    due_date = fields.Date('Due Date', required=True)
    paid_date = fields.Datetime('Paid Date', default=lambda self: fields.Datetime.now())
    payment_state = fields.Selection([('pending', "Pending"), ('done', 'Completed')],
                                     string="Payment Status", default='pending')

    @api.constrains('amount')
    def expense_amount_check(self):
        if self.amount <= 0:
            raise ValidationError(_('Amount can not be zero for transaction'))

    def confirm_payment(self):
        self.payment_state = 'done'

