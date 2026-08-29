# Security Policy - rqtll-widgets

Si detectas un problema de seguridad, vulnerabilidad visual o defecto de entrada en `rqtll-widgets`, por favor repórtalo siguiendo este procedimiento.

## Reporte responsable

1. Envía un reporte detallado al mantenedor del proyecto:
   - **adnKSharp** <adnksharp@gmail.com>

2. Evita divulgar públicamente los detalles sensibles hasta contar con un parche oficial.

## Respuesta y Tiempos

- Confirmaremos recepción del mensaje en un plazo de **36 horas**.
- Evaluaremos e integraremos la corrección del componente en un plazo máximo de **7 días hábiles**.

## Políticas de seguridad específicas para rqtll-widgets

- **Sanitización de Entradas en Diálogos**: Al diseñar campos de entrada de texto (`QLineEdit`, `QTextEdit`) en los formularios `.ui`, valida que las entradas no tengan límites desbordables o caracteres especiales no permitidos que puedan provocar desbordamientos de búfer en Qt o comandos del shell en el backend.
- **Inyección de Scripts en Recurso SVG**: Los cargadores de iconos dinámicos (`icon_loader.py`) deben filtrar y comprobar que los archivos SVG locales cargados no contengan código malicioso ejecutable.
