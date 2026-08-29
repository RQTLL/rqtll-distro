# Contribuyendo a rqtll-api

Gracias por contribuir a los contratos y definiciones de API de RQTLL. Este repositorio define los `.proto` que enlazan frontends (IDE) y backends.

## Flujo de contribución

1. Crea un *issue* describiendo la necesidad del cambio en el contrato.
2. Trabaja en una rama con nombre descriptivo (`feat/proto-xyz`, `fix/proto-compat`).
3. Actualiza los `.proto` en `proto/` y añade tests o ejemplos cuando sea posible.
4. Ejecuta `cargo build` y verifica que los stubs se generan correctamente.
5. Abre un PR describiendo los cambios y los riesgos de compatibilidad.

## Normas para modificar `.proto`

- Nunca reasignes números de campo de mensajes existentes. Si debes eliminar un campo, márcalo como `reserved` y no reutilices el número.
- Añade campos nuevos al final con nuevos números.
- Para cambios incompatibles (breaking changes), incrementa la versión del paquete o documenta el cambio en el PR.
- Usa tipos explícitos: preferir `google.protobuf.Timestamp` para fechas, enums para conjuntos cerrados y mensajes en lugar de cadenas libres cuando el formato está definido.
- Documenta el propósito de cada servicio y cada RPC en el archivo `.proto` con comentarios.

## Generar y probar localmente

```bash
cd rqtll-api
# compila y genera stubs con tonic_build
cargo build
```

## Revisión de PR

- Incluye ejemplos de cliente/servidor mínimos si el cambio añade un servicio nuevo.
- Marcar claramente cualquier cambio que requiera acciones en `rqtll-service` o en la IDE.

## Estilo y formato

- Mantén los mensajes `.proto` y nombres en `snake_case` para campos y `PascalCase` para mensajes/enums.

## Comunicación

Para dudas, propone en el *issue* o contacta a los mantenedores en las discusiones del repositorio principal [.github](https://github.com/RQTLL/.github/).
