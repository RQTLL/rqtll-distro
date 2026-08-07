# Contribuyendo a rqtll-distro

¡Gracias por contribuir a la distribución y empaquetado de RQTLL!

## Flujo de Trabajo para Lanzamientos y Empaquetado

1. **Apertura de Issues**: Discute cualquier cambio en la estructura de dependencias o scripts de empaquetado antes de trabajar en ello.
2. **Modificación de Recetas**:
   - Asegúrate de actualizar los metadatos de versiones en las recetas correspondientes.
   - Las dependencias del sistema deben estar claramente tipificadas para arquitecturas `amd64`.
3. **Prueba Local**: Realiza una construcción local del script de empaquetado y verifica su instalación limpia en un sistema `amd64` limpio.
4. **Pull Requests**: Abre un PR hacia `main`. Describe los cambios en el instalador o receta de empaque.

## Normas de Distribución

- Todo debe estar hecho para `amd64`. 
- Evitar dependencias externas. Si es estrictamente necesario, justificar su inclusion y obtener aprobacion.
- Mantener las versiones de los submódulos sincronizadas.
