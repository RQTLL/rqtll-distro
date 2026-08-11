# Security Policy - rqtll-components

Si encuentras una vulnerabilidad o un problema de seguridad relacionado con los recursos estáticos, fuentes o temas en `rqtll-components`, por favor repórtalo siguiendo este procedimiento.

## Reporte responsable

1. Envía un reporte detallado al mantenedor del proyecto:
   - **adnKSharp** <adnksharp@gmail.com>

2. Incluye en tu correo:
   - Descripción de la vulnerabilidad (por ejemplo, vulnerabilidades en fuentes TTF/OTF modificadas, inyecciones CSS/QSS maliciosas o archivos vectoriales SVG con exploits XML/XSS).
   - Pasos detallados para reproducir o verificar el fallo de seguridad.
   - Posible impacto en la ejecución de la IDE (`rqtll-ide`) al procesar los archivos de componentes.

3. Evita publicar detalles de la vulnerabilidad en foros o redes públicas hasta que hayamos publicado una corrección.

## Respuesta y Tiempos

- Confirmaremos la recepción de tu mensaje en un plazo de **36 horas**.
- Evaluaremos el impacto y publicaremos una mitigación o actualización del submódulo en un plazo máximo de **7 días hábiles**.

## Políticas de seguridad específicas para rqtll-components

- **Validación de XML en SVGs**: Dado que PySide6 y Qt renderizan SVGs, cualquier icono o recurso vectorial aportado por la comunidad no debe contener scripts de procesamiento externos ni referencias a entidades externas (XXE) que puedan explotar el motor XML de Qt.
- **Sanitización de Fuentes**: Toda tipografía incorporada al proyecto en formato TTF o OTF debe provenir de fuentes oficiales y seguras para evitar desbordamientos de búfer en los cargadores de fuentes del sistema operativo.
