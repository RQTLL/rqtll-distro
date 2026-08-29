# rqtll-widgets

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-light.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-dark.svg">
  <img alt="RQTLL Logo" src="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-color.svg" width="50px">
</picture>

Biblioteca de formularios de interfaz de usuario (compilados a partir de archivos Qt Designer `.ui`) y utilidades visuales compartidas para RQTLL. Este repositorio proporciona la colección de widgets del ecosistema, diseñados bajo el esquema estético de Blender y los estilos QSS definidos en [rqtll-components](https://github.com/RQTLL/rqtll-components).

## Table of Contents
- [rqtll-widgets](#rqtll-widgets)
  - [Table of Contents](#table-of-contents)
  - [Quickstart](#quickstart)
    - [Requisitos](#requisitos)
    - [Consumir rqtll-widgets](#consumir-rqtll-widgets)
      - [Añadir como Submódulo de Git](#añadir-como-submódulo-de-git)
  - [Estructura del Repositorio](#estructura-del-repositorio)
  - [Componentes Core](#componentes-core)
    - [1. TitleBar (Barra de Título Personalizada)](#1-titlebar-barra-de-título-personalizada)
    - [2. DemoWindow (Contenedor Base Frameless)](#2-demowindow-contenedor-base-frameless)
  - [Capturas de Pantallas y Ventanas](#capturas-de-pantallas-y-ventanas)
    - [I. Asistente de Instalación (Wizard)](#i-asistente-de-instalación-wizard)
      - [`f5_wizard_init`](#f5_wizard_init)
      - [`f6_wizard_opt`](#f6_wizard_opt)
      - [`f7_wizard_install_config`](#f7_wizard_install_config)
      - [`f8_wizard_installed`](#f8_wizard_installed)
      - [`f9_wizard_close`](#f9_wizard_close)
    - [II. Pantalla de Bienvenida e Inicio](#ii-pantalla-de-bienvenida-e-inicio)
      - [`f0_main`](#f0_main)
      - [`f1_new_ws`](#f1_new_ws)
      - [`f3_clone_ws`](#f3_clone_ws)
      - [`f4_package_manager`, `g8_package_manager`](#f4_package_manager-g8_package_manager)
    - [III. Espacio de Trabajo Principal (Workspace)](#iii-espacio-de-trabajo-principal-workspace)
      - [`g1_text_editor`](#g1_text_editor)
      - [`g2_compiler`](#g2_compiler)
      - [`g3_twist_controller`](#g3_twist_controller)
      - [`g4_ssh`, `g5_rviz2`, `g6_gz_sim`, `g7_rqt`](#g4_ssh-g5_rviz2-g6_gz_sim-g7_rqt)
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
├── forms/                   # Plantillas UI (.ui) y stubs compilados de PySide6
│   ├── test-widgets.py      # Runner auxiliar para previsualizar todas las ventanas
│   └── f*_ui_*.py           # Modulos compilados de Qt Designer
├── utils/                   # Clases de utilidad y extensiones de componentes PySide6
│   ├── base_window.py       # Ventana frameless y contenedor DemoWindow
│   ├── titlebar.py          # Barra de título personalizada estilo Blender
│   └── graph.py             # Motor del grafo interactivo de ROS 2
├── LICENSE
└── README.md
```

---

## Componentes Core

### 1. TitleBar (Barra de Título Personalizada)
La clase `TitleBar` (`utils/titlebar.py`) reemplaza la barra de título nativa del sistema operativo, proporcionando un diseño oscuro integrado con la IDE:
- **Botones Configurables**: Permite habilitar o deshabilitar dinámicamente botones específicos mediante parámetros booleanos en su constructor:
  - `show_daemon`: Muestra u oculta el botón para reiniciar el daemon/servicio de ROS 2 (`_btn_daemon`).
  - `show_tab`: Muestra u oculta el botón para dividir el panel de terminal (`_btn_tab`).
  - **Botón de Maximizar**: Se oculta automáticamente si la ventana tiene dimensiones fijas (`minimumSize == maximumSize`).
- **Efecto en el Layout**: Habilitar o deshabilitar estos botones altera la distribución interna del encabezado. La barra adapta dinámicamente el espaciador elástico (`QSpacerItem`) manteniendo los controles de cierre, maximizado y minimizado alineados perfectamente a la derecha.

### 2. DemoWindow (Contenedor Base Frameless)
La clase `DemoWindow` (`utils/base_window.py`) es la base de todas las ventanas flotantes y modales de RQTLL. Hereda de `QWidget` e implementa:
- **Decoración de Ventana**: Fuerza las banderas `Qt.FramelessWindowHint` y `Qt.WA_TranslucentBackground` para permitir esquinas redondeadas y bordes limpios sin marcos nativos.
- **Redimensionado Dinámico**: Filtra eventos del mouse en las esquinas y bordes del contenedor principal, traduciéndolos a llamadas del sistema para iniciar operaciones de redimensionado nativas (`startSystemResize`).
- **Uso Estándar**: Para crear cualquier ventana en general con el marco estético de RQTLL, se instancia `DemoWindow` pasando el stub de setup UI compilado como primer argumento:
```python
from utils.base_window import DemoWindow
from forms.f1_ui_new_ws import Ui_Form

# Crea una ventana flotante para configurar un nuevo espacio de trabajo
ventana = DemoWindow(ui_class=Ui_Form, title="Nuevo Workspace", show_daemon=False)
ventana.show()
```

---

## Capturas de Pantallas y Ventanas

A continuación se presenta la secuencia completa de ventanas (disponibles en [rqtll-components](https://github.com/RQTLL/rqtll-components/tree/main/releases/dark/web)):

### I. Asistente de Instalación (Wizard)

#### `f5_wizard_init`

Pantalla iniical del asistente de RQTLL para la instalación de ROS 2

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-1D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-1L.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-1D.webp" width="50%" height="auto">
</picture>

#### `f6_wizard_opt`

Pantalla para elegir instalar ROS 2 o no.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-2D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-2L.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-2D.webp" width="50%" height="auto">
</picture>

Al optar por instalar ROS 2 se mostrará una alerta sobre la ejecución de tareas con permisos de superusuario.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-2D-A.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-2L-A.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-2D-A.webp" width="25%" height="auto">
</picture>

#### `f7_wizard_install_config`

Pantalla para elegir la versión de ROS 2 a instalar, usando la lista de distribuiciones publicadas por el sistema operativo. La ventana cuenta con una pestaña extra para instalar paquetes adicionales relacionados con ROS2, Python y rti.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-3D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-3L.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-3D.webp" width="50%" height="auto">
</picture>

#### `f8_wizard_installed`

Una vez elegida la distribución, se muestra una barra de progreso mientras se instalan los paquetes y se configure microROS.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-4D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-4L.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-4D.webp" width="50%" height="auto">
</picture>

Una vez finalizada la instalación, se muestra una pantalla con el resumen de la instalación y la posibilidad de cargar las herramientas de ROS2 al abrir una nueva terminal ademas de configurar el firewall de Ubuntu para permitir la comunicación con otras máquinas con ROS2.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-5D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-5L.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-5D.webp" width="50%" height="auto">
</picture>

#### `f9_wizard_close`

Al finalizar el asistente de instalación, se muestra una pantalla de despedida para proceder a abrir la pantalla de Bienvenida.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-6D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A1-WIZARD-6L.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A1-WIZARD-6D.webp" width="50%" height="auto">
</picture>

### II. Pantalla de Bienvenida e Inicio

#### `f0_main`

Inspirado en las páginas de inicio como Android Studio o Visual Studio, esta pantalla permite al usuario abrir un espacio de trabajo existente o crear uno nuevo, ademas de acceder a la página de gestión de paquetes apt. 

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-1D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A2-START-1L.webp">
  <img alt="Pantalla de bienvenida e inicio" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-1D.webp" width="60%" height="auto">
</picture>

#### `f1_new_ws`

Formulario para la creacion de un nuevo espacio de trabajo, a su vez incluye la opción de crear paquetes de ROS2, nodos y lanzadores.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-3D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A2-START-3L.webp">
  <img alt="Creacion de un nuevo espacio de trabajo" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-2D.webp" width="70%" height="auto">
</picture>

#### `f3_clone_ws`

Ventana para clonar espacios de trabajo via git.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-4D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A2-START-4L.webp">
  <img alt="Clonacion de espacios de trabajo" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-2D.webp" width="40%" height="auto">
</picture>

#### `f4_package_manager`, `g8_package_manager`

Ventana para gestionar paquetes de Ubuntu (apt) relacionados con ROS 2, Python y Rti.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-2D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A2-START-2L.webp">
  <img alt="Gestor de paquetes apt" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A2-START-2D.webp" width="100%" height="auto">
</picture>


### III. Espacio de Trabajo Principal (Workspace)

#### `g1_text_editor`

Explorador de archivos, editor de texto y emulador de terminal integrado.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-1D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-1L.webp">
  <img alt="Explorador de archivos" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-1D.webp" width="100%" height="auto">
</picture>

#### `g2_compiler`

En esta ventana se tiene la opción de limpiar y compilar el espacio de trabajo actual, una vez compilado, se muestran los nodos y lanzadores disponibles acorde al espacio de trabajo. También se listan los tópicos disponibles, permitiendo interactuar con ellos desde la misma ventana.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-2D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-2L.webp">
  <img alt="Compilador de espacios de trabajo" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-2D.webp" width="100%" height="auto">
</picture>

#### `g3_twist_controller`

Parecido al paquete de ros2 `twist_teleop_keyboard`, se puede manejar la velocidad angular y lineal del robot mediante el teclado, ademas de enviar señales de parada. Esta ventana permite configurar el topico al que se envian las instrucciones y las teclas asignadas para cada comando.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-4D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-4L.webp">
  <img alt="Twist controller" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-4D.webp" width="100%" height="auto">
</picture>

#### `g4_ssh`, `g5_rviz2`, `g6_gz_sim`, `g7_rqt`

Shortcuts para abrir ventanas de ssh, rviz2, gz-sim y rqt. En base a las opciones disponibles para cada comando se muestra en una lista las opciones.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-5D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-5L.webp">
  <img alt="Shortcuts para abrir ventanas" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-5D.webp" width="100%" height="auto">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-6D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-6L.webp">
  <img alt="Shortcuts para abrir ventanas" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-6D.webp" width="100%" height="auto">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-7D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-7L.webp">
  <img alt="Shortcuts para abrir ventanas" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-7D.webp" width="100%" height="auto">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-8D.webp">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/releases/light/web/A3-WORKSPACE-8L.webp">
  <img alt="Shortcuts para abrir ventanas" src= "https://github.com/RQTLL/rqtll-components/blob/main/releases/dark/web/A3-WORKSPACE-8D.webp" width="100%" height="auto">
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
