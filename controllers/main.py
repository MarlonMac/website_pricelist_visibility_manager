# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class WebsiteSalePricelistCustom(http.Controller):

    @http.route(['/shop/change_pricelist/<int:pricelist_id>'], type='http', auth="public", website=True, sitemap=False)
    def change_pricelist_custom(self, pricelist_id, **kwargs):
        pricelist = request.env['product.pricelist'].browse(pricelist_id).exists()
        if not pricelist:
            return request.redirect('/shop')

        request.website.sale_set_pricelist(pricelist.id)
        redirect_url = kwargs.get('redirect', request.httprequest.referrer or '/shop')
        return request.redirect(redirect_url)