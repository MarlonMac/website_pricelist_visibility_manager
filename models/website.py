# -*- coding: utf-8 -*-
from odoo import fields, models, api

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
    # --- NUEVO CAMPO CALCULADO ---
    pricelist_visibility_group_xml_id = fields.Char(
        string="Grupo Autorizado (XML ID)",
        compute='_compute_pricelist_visibility_group_xml_id'
    )

    @api.depends('pricelist_visibility_group_id')
    def _compute_pricelist_visibility_group_xml_id(self):
        for website in self:
            group = website.pricelist_visibility_group_id
            if group:
                # get_external_id devuelve un diccionario, tomamos el valor.
                external_id_dict = group.get_external_id()
                website.pricelist_visibility_group_xml_id = external_id_dict.get(group.id, '')
            else:
                website.pricelist_visibility_group_xml_id = ''