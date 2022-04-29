from odoo import api, fields, models, tools, _
from odoo.exceptions import ValidationError


class ExpenseTransaction(models.Model):
    _name = "expense.transaction"
    _rec_name = 'name'
    _description = "expense.transaction"
    _order = 'name'

    name = fields.Char('Expense on')
    category = fields.Many2one('expense.category', string='Expense Transaction', required=True)
    amount = fields.Integer('Amount', required=True)
    expense_type = fields.Selection([('need', 'Need'), ('want', 'Want')], default='want', required=True)
    note = fields.Text('Note for the Transaction')
    date = fields.Datetime('Transaction Date', default=lambda self: fields.Datetime.now())

    @api.constrains('amount')
    def expense_amount_check(self):
        if self.amount <= 0:
            raise ValidationError(_('Amount can not be zero for transaction'))


class ExpenseCategory(models.Model):
    _name = "expense.category"
    _rec_name = 'name'
    _description = "expense.category"
    _order = 'name'

    name = fields.Char(string='Expense Category', required=True)
    expense_ids = fields.One2many('expense.transaction', 'category', 'Transaction from this Category', readonly=True)


class CreditCardManager(models.Model):
    _name = "credit.card.manager"
    _rec_name = 'name'
    _description = "credit.card.manager"
    _order = 'name'

    name = fields.Char(string='Credit Card', required=True)
    currency_id = fields.Many2one('res.currency', string='Amount Currency')
    amount = fields.Monetary(string='Amount Due')
    due_date = fields.Date('Due Date')
    payment_state = fields.Selection([('pending', "Pending"), ('done', 'Completed')],
                                     string="Payment Status", default='pending')

    @api.constrains('amount')
    def expense_amount_check(self):
        if self.amount <= 0:
            raise ValidationError(_('Amount can not be zero for transaction'))

    def confirm_payment(self):
        self.payment_state = 'done'



