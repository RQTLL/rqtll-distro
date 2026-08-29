# rqtll-components

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/branding/logo-main-light.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/branding/logo-main-dark.svg">
  <img alt="RQTLL Logo" src="./assets/branding/logo-main-color.svg" width="50px">
</picture>

Sistema de diseño y librería de recursos visuales para **[RQTLL](https://github.com/RQTLL)**.

> [!CAUTION]
> Este es un repositorio núcleo. Cualquier cambio en la paleta o iconos se propagará a todos los módulos que lo consumen.

## Table of Contents
- [rqtll-components](#rqtll-components)
  - [Table of Contents](#table-of-contents)
  - [Quickstart](#quickstart)
    - [Añadir a un módulo nuevo](#añadir-a-un-módulo-nuevo)
    - [Sincronizar cambios](#sincronizar-cambios)
  - [Estructura del Repositorio](#estructura-del-repositorio)
  - [Recursos Visuales](#recursos-visuales)
  - [Tipografía](#tipografía)
  - [Uso de Estilos (QSS)](#uso-de-estilos-qss)
    - [Integración Estética](#integración-estética)
  - [Cómo contribuir](#cómo-contribuir)
  - [License](#license)
  - [Maintainers](#maintainers)

## Quickstart

Este repositorio está diseñado para ser consumido como un **Git Submodule**. Esto permite que los recursos estén disponibles *offline*

### Añadir a un módulo nuevo
```bash
# Dentro del directorio del proyecto que va a consumir rqtll-components
git submodule add https://github.com/RQTLL/rqtll-components.git external/rqtll_components
git submodule update --init --recursive

```

### Sincronizar cambios

```bash
git submodule update --remote --merge
```

## Estructura del Repositorio

```text
./
├── assets/
│   ├── branding/       # Identidad de marca (Isotipos)
│   ├── fonts/          # Fuentes Nunito Sans y Ubuntu Mono/Nerd Font Mono
│   └── icons/          # Iconos de la IDE
├── styles/
│   ├── themes/         # Hojas de estilo .qss
│   └── palette.json    # Definición maestra de colores
└── releases/           # Capturas para documentación
└── README.md

```

## Recursos Visuales

Para mantener la agilidad del repositorio, la documentación detallada se ha segmentado:

* **Catálogo de Iconos ([ICONS.md](./docs/ICONS.md))**: Tabla completa de iconos, comandos asociados y sus roles.
* **Identidad de Marca ([BRANDING.md](./docs/BRANDING.md))**: Guía de uso del isotipo, márgenes de seguridad para iconos y exportación.
* **Paleta Detallada ([PALETTE.md](./docs/PALETTE.md))**: Muestrario completo de colores para temas Claro y Oscuro.

## Tipografía

El proyecto utiliza fuentes locales para garantizar consistencia sin conexión a internet.

| Fuente | Uso | Licencia |
| --- | --- | --- |
| **Nunito Sans** | Interfaz de Usuario (UI) | OFL |
| **Ubuntu Nerd Font Mono** | Glifos técnicos e iconos integrados | UFL |

## Uso de Estilos (QSS)

Los estilos siguen un formato **Flat Modern Minimalist** con bordes redondeados calculados al **18.75%** de la dimensión mínima.

```python
# Ejemplo de carga en PySide6 para un recurso almacenado en
# external/rqtll_components
...
components_path = os.path.join(os.path.dirname(__file__), "external/rqtll_components")
fonts_path = os.path.join(components_path, "assets/fonts")
for root, dirs, files in os.walk(fonts_path):
    for file in files:
        if file.endswith((".ttf", ".otf")):
            QFontDatabase.addApplicationFont(os.path.join(root, file))

qss_file = os.path.join(components_path, f"styles/themes/{theme}")
if os.path.exists(qss_file):
    with open(qss_file, "r") as f:
        app.setStyleSheet(f.read())
...
```

### Integración Estética
La IDE consume la paleta definida en `palette.json` para:

1. Replicar el esquema visual de Blender en un gráfico de nodos:
    - **Cabeceras de color según tipo**: Nodos de color azul oscuro (`#0090ff`) y tópicos de color verde azulado (`#068989`).
    - **Cuerpo neutral**: Fondos grises (`#2b2b2b`) para mantener la concentración del usuario.
    - **Resaltado de Selección**: Bordes coloridos para indicar elementos seleccionados.
2. Resaltar palabras reservadas del lenguaje de programación en el editor de texto y terminales con colores del tema.

## Cómo contribuir

- Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar PR.
- Para añadir un icono nuevo:
  1. Añadir capas para los estatus `default`, `hover` y `click` a **assets/icons/window-buttons.xcf**
  2. Añadir SVGs a **assets/icons/[nombre_del_icono]/[estado].svg**.
  3. Actualizar [ICONS.md](docs/ICONS.md) con el icono, nombre y rol.
  4. Crear PR con descripción y captura.

## License

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Maintainers

* **adnKSharp** <adnksharp@gmail.com>

