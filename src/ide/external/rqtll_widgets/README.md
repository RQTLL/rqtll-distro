# rqtll-widgets

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-light.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-dark.svg">
  <img alt="RQTLL Logo" src="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-color.svg" width="50px">
</picture>

Formularios de interfaz de usuario (compilados a partir de archivos Qt Designer `.ui`) y utilidades visuales compartidas para RQTLL. Este repositorio proporciona la colección de widgets del ecosistema, diseñados bajo el esquema estético de Blender y los estilos QSS definidos en [rqtll-components](https://github.com/RQTLL/rqtll-components).

## Table of Contents
- [rqtll-widgets](#rqtll-widgets)
  - [Table of Contents](#table-of-contents)
  - [Quickstart](#quickstart)
    - [Requisitos](#requisitos)
    - [Consumir rqtll-widgets](#consumir-rqtll-widgets)
      - [Añadir como Submódulo de Git](#añadir-como-submódulo-de-git)
  - [Estructura del Repositorio](#estructura-del-repositorio)
  - [Ventanas y UI Forms](#ventanas-y-ui-forms)
    - [1. Asistente de Instalación (`f7_wizard_install_config.ui`)](#1-asistente-de-instalación-f7_wizard_install_configui)
    - [2. Gestor de Paquetes (`f4_package_manager.ui`)](#2-gestor-de-paquetes-f4_package_managerui)
    - [3. Panel Principal (`f0_main.ui`)](#3-panel-principal-f0_mainui)
    - [4. Editor de Texto, Compilador y Lanzadores (`g1_text_editor.ui`, `g2_compiler.ui` y `g6_gz_sim.ui`)](#4-editor-de-texto-compilador-y-lanzadores-g1_text_editorui-g2_compilerui-y-g6_gz_simui)
  - [Utilidades del Sistema (utils)](#utilidades-del-sistema-utils)
  - [Cómo contribuir](#cómo-contribuir)
  - [Security](#security)
  - [License](#license)
  - [Maintainers](#maintainers)

## Quickstart

### Requisitos

- `Python 3.10+`
- `PySide6`

### Consumir rqtll-widgets

#### Añadir como Submódulo de Git
```bash
git submodule add https://github.com/RQTLL/rqtll-widgets.git external/rqtll_widgets
git submodule update --init --recursive
```

---

## Estructura del Repositorio

```text
./
├── forms/                   # Plantillas UI compiladas de Qt Designer
├── utils/                   # Clases visuales auxiliares y extensiones de PySide6
├── LICENSE
└── README.md
```

---

## Ventanas y UI Forms

Las ventanas principales se alojan en la carpeta `forms/` y definen la estructura visual de la IDE:

### 1. Asistente de Instalación (`f7_wizard_install_config.ui`)
Configura de forma interactiva las dependencias requeridas para la instalación y carga progresiva de ROS 2.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-1D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-1L.webp">
  <img alt="Asistente de Instalación" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-1D.webp" width="100%" height="auto">
</picture>

### 2. Gestor de Paquetes (`f4_package_manager.ui`)
Administra los paquetes instalados del sistema operativo mediante una cuadrícula de estado.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-2D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-2L.webp">
  <img alt="Gestor de Paquetes" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-2D.webp" width="100%" height="auto">
</picture>

### 3. Panel Principal (`f0_main.ui`)
Panel inicial que permite crear, abrir y clonar espacios de trabajo.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-1D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A2-START-1L.webp">
  <img alt="Gestor de Espacios de Trabajo" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-1D.webp" width="100%" height="auto">
</picture>

### 4. Editor de Texto, Compilador y Lanzadores (`g1_text_editor.ui`, `g2_compiler.ui` y `g6_gz_sim.ui`)
Controles para la edición de código, compilación y lanzamiento de aplicaciones de ROS 2.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-2D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-2L.webp">
  <img alt="Editor de Texto" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-2D.webp" width="100%" height="auto">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-3D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-3L.webp">
  <img alt="Editor de Texto" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-3D.webp" width="100%" height="auto">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-7D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-7L.webp">
  <img alt="Editor de Texto" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-7D.webp" width="100%" height="auto">
</picture>

---

## Utilidades del Sistema (utils)

La lógica visual y extensiones de controles se implementan en `utils/`:

* **base_window.py**: Frameless window base que proporciona soporte para cabecera custom, redimensionado dinámico, acoplamiento de paneles y recarga dinámica del stylesheet.
* **titlebar.py**: Barra de título personalizada que permite mover la ventana, y dispone de atajos rápidos para colapsar, reiniciar el daemon de ROS o dividir la terminal.
* **frame_button.py / frame_option_button.py**: Widgets de botón personalizados que implementan hover, clics y almacenamiento del path de icono original (`_rqtll_icon_path`).
* **graph.py**: Implementa el visualizador interactivo del grafo de ROS 2 (heredado en `NodesVisualizerController`). Administra los objetos gráficos para dibujar nodos (`RosNode`) y tópicos (`RosTopic`), controlando de forma inteligente la escala y el modo de caché gráfico (`DeviceCoordinateCache`).
* **icon_loader.py**: Carga y recolorea dinámicamente los iconos vectoriales SVG sobre la marcha basándose en el color de acento del tema seleccionado.
* **theme_manager.py**: Proveedor global que emite la señal `themeChanged` para sincronizar todas las ventanas secundarias y layouts al cambiar el esquema de color.

---

## Cómo contribuir

- Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar un Pull Request.
- **Flujo de Diseño**:
  1. Diseña o modifica las vistas editando los archivos `.ui` mediante Qt Designer.
  2. Compila el archivo `.ui` a Python usando `uic`:
     ```bash
     pyside6-uic forms/fX_nombre.ui -o forms/fX_ui_nombre.py
     ```
  3. Comprueba que las referencias relativas importen los widgets correctos y añade los archivos correspondientes en tu commit.

## Security

Consulta [SECURITY.md](SECURITY.md) para conocer el procedimiento de reporte de vulnerabilidades.

## License

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Maintainers

* **adnKSharp** <adnksharp@gmail.com>
