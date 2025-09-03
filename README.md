# Website Pricelist Visibility Manager

**Módulo para Odoo 16 Community Edition**

## Resumen

Este módulo permite un control avanzado sobre la visibilidad del selector de listas de precios en el eCommerce de Odoo. Permite activar o desactivar el selector por sitio web y restringir su visibilidad a un grupo de usuarios específico. Adicionalmente, corrige el comportamiento de redirección al cambiar una lista de precios, asegurando que el usuario permanezca en la misma página (producto o catálogo) en todos los navegadores.

---

## Características Principales ✨

* **Configuración por Sitio Web:** Activa o desactiva la funcionalidad de forma independiente para cada sitio web en tu instancia de Odoo.
* **Control de Acceso por Grupo:** Define qué grupo de usuarios (ej. Vendedores, Distribuidores VIP, etc.) puede ver y utilizar el selector de listas de precios.
* **Redirección Robusta:** Soluciona el problema por el cual los usuarios eran redirigidos a `/shop` al cambiar de lista de precios. La nueva lógica asegura que el usuario se mantenga en la página actual, mejorando la experiencia de usuario (UX).
* **Integración Limpia:** El módulo hereda las vistas estándar de Odoo y añade la funcionalidad de forma no intrusiva, siguiendo las mejores prácticas de desarrollo.

---

## Configuración ⚙️

Una vez instalado el módulo, la configuración es muy sencilla:

1.  Asegúrate de tener el **modo desarrollador activado**.
2.  Navega a **Sitio Web > Configuración > Ajustes**.
3.  En la esquina superior de la página de ajustes, selecciona el sitio web que deseas configurar.
4.  Busca la nueva sección llamada **"Selector de Listas de Precios"**.

    

5.  Marca la casilla **"Activar Selector de Listas de Precios"** para habilitar la funcionalidad en el sitio web seleccionado.
6.  En el campo **"Grupo Autorizado para ver Listas de Precios"**, selecciona el grupo de usuarios que tendrá permiso para ver el selector. Si dejas este campo vacío, todos los usuarios verán el selector (siempre y cuando la opción principal esté activa).
7.  Haz clic en **"Guardar"**.
8.  Repite el proceso para cada sitio web que necesites configurar.

---

## Detalles Técnicos 👨‍💻

* **Ruta Sobrescrita:** El módulo implementa un nuevo controlador para la ruta `/shop/change_pricelist/<int:pricelist_id>` que reemplaza la lógica de redirección por defecto.
* **Modelos Extendidos:**
    * `website`: Se añaden los campos `is_pricelist_selector_active` y `pricelist_visibility_group_id` para almacenar la configuración.
    * `res.config.settings`: Se heredó para exponer los nuevos campos en la vista de Ajustes.
* **Vistas Heredadas:**
    * `website_sale.pricelist_list`: Modificada para añadir un parámetro `redirect` a los enlaces del selector.
    * `website_sale.product`: Heredada para aplicar la lógica de visibilidad condicional sobre el selector existente.
    * `website_sale.products`: Heredada para aplicar la misma lógica de visibilidad en la página de catálogo.

---

**Autor:** Tu Nombre / Tu Empresa
**Versión:** 16.0.1.0.0