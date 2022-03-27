# -*- coding: utf-8 -*-
from odoo import http

# class School2(http.Controller):
#     @http.route('/school2/school2/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/school2/school2/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('school2.listing', {
#             'root': '/school2/school2',
#             'objects': http.request.env['school2.school2'].search([]),
#         })

#     @http.route('/school2/school2/objects/<model("school2.school2"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('school2.object', {
#             'object': obj
#         })