# Roadmap del Módulo

Este documento describe las futuras mejoras y características planificadas para el módulo **Website Pricelist Visibility Manager**.

---

## Versión 1.1 (Mejoras a Corto Plazo)

* **Selección Múltiple de Grupos:**
    * Modificar el campo `Many2one` a `Many2many` para permitir la selección de múltiples grupos de usuarios autorizados.

* **Cambio de Precios con AJAX:**
    * Refactorizar el cambio de lista de precios para que se realice mediante una llamada AJAX en lugar de una recarga de página completa. Esto mejoraría drásticamente la experiencia de usuario al mostrar los nuevos precios de forma instantánea.

* **Mejoras de Estilo (UI/UX):**
    * Añadir opciones para mejorar la apariencia del selector de precios, como mostrar el símbolo de la moneda (`Q`) junto al nombre de la lista.

---

## Versión 2.0 (Funcionalidades Mayores)

* **Motor de Reglas de Visibilidad:**
    * Crear un nuevo modelo para definir reglas de visibilidad más complejas. Por ejemplo:
        * Mostrar/ocultar el selector basado en la **categoría del producto**.
        * Mostrar ciertas listas de precios solo para **productos de una marca específica**.
        * Activar reglas de visibilidad solo durante un **rango de fechas** determinado.

* **Visibilidad por Cantidad de Producto:**
    * Mostrar una lista de precios de "Mayoreo" automáticamente si el usuario añade más de 'X' unidades de un producto al carrito.

---

## Backlog / Ideas Futuras 💡

* **Informe de Uso:** Crear una vista en el backend que muestre estadísticas sobre qué listas de precios son las más utilizadas en el sitio web.
* **Botón de Limpieza de Caché:** Añadir un botón en los ajustes del módulo para forzar la limpieza de las cachés de las vistas QWeb relacionadas, facilitando la depuración.
* **Integración con Cupones:** Investigar la posibilidad de mostrar listas de precios específicas si el usuario tiene un cupón de descuento activo.