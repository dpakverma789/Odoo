from odoo import http
from odoo.http import request


class management(http.Controller):

   @http.route('/management', type='http', auth='public', website=True)
   def management_details(self, **kwargs):
       return request.render('Student_Management.controller_page', {})