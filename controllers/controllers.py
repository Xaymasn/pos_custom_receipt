# -*- coding: utf-8 -*-
from odoo import http

# class CustomPosReceipt(http.Controller):
#     @http.route('/custom_pos_receipt/custom_pos_receipt/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_pos_receipt/custom_pos_receipt/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_pos_receipt.listing', {
#             'root': '/custom_pos_receipt/custom_pos_receipt',
#             'objects': http.request.env['custom_pos_receipt.custom_pos_receipt'].search([]),
#         })

#     @http.route('/custom_pos_receipt/custom_pos_receipt/objects/<model("custom_pos_receipt.custom_pos_receipt"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_pos_receipt.object', {
#             'object': obj
#         })