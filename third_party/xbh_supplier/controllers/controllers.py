# -*- coding: utf-8 -*-
# from odoo import http


# class XbhSupplier(http.Controller):
#     @http.route('/xbh_supplier/xbh_supplier', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/xbh_supplier/xbh_supplier/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('xbh_supplier.listing', {
#             'root': '/xbh_supplier/xbh_supplier',
#             'objects': http.request.env['xbh_supplier.xbh_supplier'].search([]),
#         })

#     @http.route('/xbh_supplier/xbh_supplier/objects/<model("xbh_supplier.xbh_supplier"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('xbh_supplier.object', {
#             'object': obj
#         })

