# -*- coding: utf-8 -*-
from odoo import fields, models

class Website(models.Model):
    _inherit = 'website'

    is_pricelist_selector_active = fields.Boolean(
        string="Activar Selector de Listas de Precios"
    )
    pricelist_visibility_group_id = fields.Many2one(
        'res.groups',
        string='Grupo Autorizado para ver Listas de Precios',
        help="Si se especifica, solo los usuarios de este grupo verán el selector de listas de precios."
    )