# -*- coding: utf-8 -*-

from odoo import models, fields, api


class xbh_supplier(models.Model):
    _inherit = 'base.res.partner'
    # _name = 'xbh_supplier.xbh_supplier'
    _description = '鑫博海供应商-客户'

    xbh_supplier_code = fields.Char(string='供应商编码', compute="_gen_code")
    
    # _exclude = ['channel_ids']  # 排除多对多关系字段
    # channel_ids = fields.Many2many('discuss.channel', 'discurss_channel_partner', 'partner_id', 'channel_id', copy=False)



    # name = fields.Char()
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 2

    def _value_pc(self):
        for record in self:
            record.value2 = float(record.value) / 2

