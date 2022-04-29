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