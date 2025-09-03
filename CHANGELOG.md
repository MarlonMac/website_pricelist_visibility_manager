# Changelog

Todos los cambios notables en este proyecto serán documentados en este archivo.

El formato se basa en [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [16.0.1.0.0] - 2025-09-03

### Añadido ✨

* **Configuración por Sitio Web:** Se añadió una nueva sección en los ajustes del Sitio Web (`Ajustes > Sitio Web`) para gestionar la visibilidad del selector de listas de precios.
* **Visibilidad por Grupo de Usuarios:** Se agregó un campo `Many2one` a `res.groups` para permitir que solo los usuarios de un grupo de seguridad específico puedan ver el selector.
* **Controlador Personalizado:** Se implementó un controlador en la ruta `/shop/change_pricelist/` para manejar la lógica de cambio de precios.
* **Campo XML ID Calculado:** Se añadió un campo `compute` en el modelo `website` para obtener de forma segura el XML ID del grupo de seguridad seleccionado, simplificando las plantillas QWeb.

### Corregido 🐛

* **Error de Redirección:** Se solucionó el error fundamental por el cual los usuarios eran redirigidos a la página `/shop` al cambiar de lista de precios. La nueva lógica asegura que el usuario permanezca en la página de producto o de catálogo actual, funcionando correctamente en todos los navegadores (Chrome, Firefox, Edge).
* **Visibilidad del Selector:** Se corrigió el error que causaba la desaparición intermitente del selector de precios, así como el bug que ocultaba la barra de búsqueda junto con el selector.
* **Errores de `XPath`:** Se resolvieron múltiples errores de `XPath` durante la instalación y actualización del módulo, implementando selectores más robustos y compatibles con otras personalizaciones.
* **Errores de JavaScript (Owl):** Se solucionó el `HierarchyRequestError` en la página de Ajustes, reestructurando la herencia de la vista para seguir el patrón esperado por el framework Owl de Odoo 16.