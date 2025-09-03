# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteSalePricelistCustom(http.Controller):

    @http.route(['/shop/change_pricelist/<int:pricelist_id>'], type='http', auth="public", website=True, sitemap=False)
    def change_pricelist_custom(self, pricelist_id, **kwargs):
        """
        Controlador personalizado para cambiar la lista de precios.
        Utiliza el método correcto (sesión) para establecer la nueva lista de precios.
        """
        pricelist = request.env['product.pricelist'].browse(pricelist_id).exists()
        if not pricelist:
            return request.redirect('/shop')

        # --- INICIO DE LA CORRECCIÓN ---
        # La forma correcta en Odoo 16 es guardar el ID en la sesión del usuario.
        request.session['website_sale_current_pl'] = pricelist.id
        # --- FIN DE LA CORRECCIÓN ---

        # La lógica de redirección robusta que ya teníamos.
        redirect_url = kwargs.get('redirect', request.httprequest.referrer or '/shop')

        return request.redirect(redirect_url)