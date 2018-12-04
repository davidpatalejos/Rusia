# -*- coding: utf-8 -*-
from odoo import http

# class Rusia(http.Controller):
#     @http.route('/rusia/rusia/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rusia/rusia/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rusia.listing', {
#             'root': '/rusia/rusia',
#             'objects': http.request.env['rusia.rusia'].search([]),
#         })

#     @http.route('/rusia/rusia/objects/<model("rusia.rusia"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rusia.object', {
#             'object': obj
#         })