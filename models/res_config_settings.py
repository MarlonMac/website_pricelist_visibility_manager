# -*- coding: utf-8 -*-
from odoo import fields, models

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    is_pricelist_selector_active = fields.Boolean(
        related='website_id.is_pricelist_selector_active',
        readonly=False
    )
    pricelist_visibility_group_id = fields.Many2one(
        related='website_id.pricelist_visibility_group_id',
        readonly=False
    )