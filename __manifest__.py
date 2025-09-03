# -*- coding: utf-8 -*-
{
    'name': "Website Pricelist Visibility Manager",
    'summary': """
        Permite configurar la visibilidad del selector de listas de precios
        por sitio web y por grupo de usuarios.
    """,
    'description': """
        Añade las siguientes funcionalidades:
        - Opción en los ajustes de cada sitio web para activar el selector de listas de precios.
        - Opción para seleccionar qué grupo de seguridad puede ver el selector.
        - Corrige el bug de redirección al cambiar de lista de precios en todos los navegadores.
    """,
    'author': "Marlon Macario",
    'website': "https://link-gt.com",
    'category': 'Website/eCommerce',
    'version': '16.0.1.0.0',
    'depends': ['website_sale'],
    'data': [
        'views/res_config_settings_views.xml',
        'views/templates.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}