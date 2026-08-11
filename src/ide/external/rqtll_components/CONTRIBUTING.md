# Contribuyendo a rqtll-components

¡Gracias por ayudar a construir la identidad visual de RQTLL! Este repositorio es el corazón estético del proyecto. Para mantener la coherencia y el rendimiento, sigue estos pasos.

## Ciclo de Contribución

1. **Crea un Issue:** Antes de añadir un nuevo icono o estilo, abre un issue para discutir la necesidad y el diseño propuesto.
2. **Haz un Fork:** Trabaja en tu propia copia y crea una rama descriptiva (ej: `feat/new-ros2-icon`).
3. **Pull Request:** Envía tu PR hacia la rama `main` detallando los cambios y adjuntando imagenes.

---

## Estándares de Diseño

### 1. Iconografía (SVG)
Para asegurar que los iconos se rendericen correctamente en PySide6 y escalen sin distorsión:
- **Dimensiones:** El canvas debe ser de **1920x1920px**.
- **Trazos:** Convierte todos los trazos (*strokes*) a caminos (*paths*).

### 2. Nomenclatura de Archivos
- **kebab-case**

---

## Cómo añadir un nuevo Icono

Si vas a añadir un icono:
1. MOdifica el archivo de GIMP [window-buttons](https://github.com/RQTLL/rqtll-components/tree/main/assets/icons/window-buttons.xcf):
   1. Crea una nueva carpeta con el nombre del icono.
   2. Agrega las capas necesarias para las variantes del icono **default**, **hover** y **active**/**click**.
   3. Exporta las variantes del icono como archivos SVG.
2. Crea la carpeta con el nombre del icono dentro de `assets/icons`
   1. Añade el archivo base y sus variantes: `default.svg`, `hover.svg`, `click.svg`.

---

## Modificando Colores o Estilos
Si necesitas ajustar un color en `palette.json`:
1. Asegúrate de que el cambio se vea bien tanto en **Tema Claro** como en **Oscuro**.
3. Si modificas un archivo `.qss`, utiliza la regla del **18.75%** para los bordes redondeados de nuevos widgets.

---

## Nuevas fuentes de texto
Es necesario que las nuevas fuentes uncluyan su respectiva licencia **OFL**, **UFL** o **MIT**.

## Verificación antes de enviar
Antes de hacer el commit, verifica:
- [ ] ¿El archivo SVG se abre correctamente en un navegador?
- [ ] ¿El nombre del archivo sigue el estándar kebab-case?
- [ ] ¿Las fuentes nuevas (si las hay) incluyen su respectiva licencia OFL/UFL/MIT?

---

## Comunicación
Si tienes dudas sobre el estilo, contacta con los mantenedores a través de las discusiones del repositorio principal [.github](https://github.com/RQTLL/.github/).
