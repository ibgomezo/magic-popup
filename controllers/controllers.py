# -*- coding: utf-8 -*-
from odoo import http

# class Magic-popups(http.Controller):
#     @http.route('/magic-popups/magic-popups/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/magic-popups/magic-popups/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('magic-popups.listing', {
#             'root': '/magic-popups/magic-popups',
#             'objects': http.request.env['magic-popups.magic-popups'].search([]),
#         })

#     @http.route('/magic-popups/magic-popups/objects/<model("magic-popups.magic-popups"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('magic-popups.object', {
#             'object': obj
#         })