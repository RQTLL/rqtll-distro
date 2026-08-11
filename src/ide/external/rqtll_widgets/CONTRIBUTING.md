# Contribuyendo a rqtll-widgets

¡Gracias por ayudar a construir la biblioteca de controles de RQTLL!

## Flujo para Interfaces Visuales (Qt Designer)

1. **Edición de UI**: Utiliza siempre Qt Designer para crear o modificar los archivos `.ui` dentro de `forms/`.
2. **Compilación de stubs**: Tras modificar un archivo `.ui`, debes generar su contraparte en Python utilizando `pyside6-uic`:
   ```bash
   pyside6-uic forms/fX_widget.ui -o forms/fX_ui_widget.py
   ```
3. **Widgets Personalizados**: Si necesitas añadir nuevos controles interactivos complejos, colócalos en `utils/`.
4. **Pull Requests**: Envía tus cambios detallando qué componentes visuales fueron modificados y confirma que los archivos `.py` compilados están incluidos en el PR.
