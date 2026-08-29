# Security Policy

Si encuentras una vulnerabilidad de seguridad en el código que forma parte de `rqtll-api` por favor reportalo siguiendo los siguientes pasos.

## Reporte responsable

1. Abre un *issue* marcado como `security` o, si tu reporte contiene información sensible, contacta directamente a:

   * **adnKSharp** <adnksharp@gmail.com>

2. Incluye en el reporte:
   - Descripción clara del problema y pasos para reproducirlo.
   - Versiones afectadas (commit SHA, tag o rama).
   - Impacto estimado y prioridad sugerida.

3. Evita publicar detalles de explotación públicamente hasta que exista un parche disponible.

## Respuesta y tiempos

- Confirmaremos recepción en una maximo de 36 horas.
- Evaluando el impacto y propondremos un plan de mitigación/patch en un plazo de 7 días hábiles cuando sea posible.

## Divulgación coordinada

En conjunto con el reportante; publicaremos los detalles una vez que la mayoría de los usuarios puedan actualizar a una versión segura.

## Políticas de seguridad específicas para rqtll-api

- En `TerminalService`, asegurar control de sesiones, evitar inyección de comandos en parámetros que no sean datos de entrada de PTY.  
- En `SecurityService`, nunca enviar contraseñas en texto plano por canales inseguros; preferir mecanismos de autenticación basados en tokens y transportar por TLS.

## Actualizaciones

Esta política puede actualizarse; consulta siempre este archivo en el repositorio.
