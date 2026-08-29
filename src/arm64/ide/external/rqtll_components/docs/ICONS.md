# Catálogo de Iconos (RQT2)

Este documento detalla la librería de iconos utilizados en el ecosistema **RQT2**. Todos los iconos son archivos **SVG** optimizados para ser escalables y ligeros.


## Categorias

- [Catálogo de Iconos (RQT2)](#catálogo-de-iconos-rqt2)
	- [Categorias](#categorias)
	- [Estándares](#estándares)
	- [Organización de carpetas](#organización-de-carpetas)
		- [Botones de Ventana](#botones-de-ventana)
		- [Barra de navegación](#barra-de-navegación)
		- [Varios](#varios)

## Estándares
- **Formato:** SVG v1.1
- **Dimensiones Base:** 1920x1920
- **Margenes**: 228

---

## Organización de carpetas
Cada icono se encuentra dentro de su propia subcarpeta en `assets/icons/`:
```text
assets/icons/<icon>/
├── default.svg
├── hover.svg
└── disabled.svg
```

---

### Botones de Ventana

| Icono | Nombre | Comando relacionado | Rol |
| :---: | :--- | :--- | :--- |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/close/default.svg"></kbd> | **close** | Window button | Cerrar ventana. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/minimize/default.svg"></kbd> | **minimize** | Window button | Minimizar ventana. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/restore/default.svg"></kbd> | **maximize** | Window button | Maximizar ventana. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/maximize/default.svg"></kbd> | **restore** | Window button | Restaura el tamaño de la ventana. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/tab/default.svg"></kbd> | **split** | Window button | Abre un emulador de la terminal. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/split/default.svg"></kbd> | **tab** | Window button | Cierra el emulador de la terminal. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/daemon/default.svg"></kbd> | **daemon** | Window button | Reinicia el daemon de ROS2. |

### Barra de navegación

| Icono | Nombre | Ventana de la IDE |
| :---: | :----- | :------------------ | 
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/code/default.svg"></kbd> | **code** | Editor de texto y emulador de terminal |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/launch/default.svg"></kbd> | **launch** | Compilador de paquetes de ROS2 |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/nodes/default.svg"></kbd> | **nodes** | Gráfico de nodos |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/teleop/default.svg"></kbd> | **teleop** | Control de robot mediante /geometry_msgs/Twist |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/3d/default.svg"></kbd> | **3d** | Lanzador de RViz2 |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/emulator/default.svg"></kbd> | **emulator** | Lanzador de Gazebo Sim |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/widgets/default.svg"></kbd> | **widgets** | Lanzador de rqt | 
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/ssh/default.svg"></kbd> | **ssh** | Lanzador de conexión SSH a un robot remoto |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/package/default.svg"></kbd> | **package** | Gestor de paquetes de Linux |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/list/default.svg"></kbd> | **list** | [Obsoleto] Ventana de nodos y topicos en ejecución. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/load/default.svg"></kbd> | **load** | Abre el dialogo de carga de espacios de trabajo. |

### Varios

| Icono | Nombre | Comando relacionado | Rol |
| :---: | :--- | :--- | :--- |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/ros-core/default.svg"></kbd> | **ros-core** | `simbólico` | Símbolo de ROS2 Core |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/ros-desktop/default.svg"></kbd> | **ros-desktop** | `simbólico` | Símbolo de ROS2 Desktop |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/ros-full/default.svg"></kbd> | **ros-full** | `simbólico` | Símbolo de ROS2 Desktop Full |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/compile/default.svg"></kbd> | **compile** | `rosdep install ; colcon build` | Resuelve dependencias con `rosdep install` y construir el espacio de trabajo con `colcon build`. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/clean/click.svg"></kbd> | **clean** | `rm -rf build install log` | Elimina los directorios `build`, `install` y `log` creados por `colcon build`. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/folder/default.svg"></kbd> | **folder** | `file-dialog` | Abre el dialogo de archivos. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/record/default.svg"></kbd> | **record** | `ros2 bag record` | Graba los datos transmitidos con`ros2 bag`. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/play/default.svg"></kbd> | **play** | `ros2 bag play` | Reproduce los datos grabados con `ros2 bag`. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/settings/default.svg"></kbd> | **settings** | Configuración de la IDE | Abre submenus de configuración. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/params/default.svg"></kbd> | **params** | Configuración de la IDE | [Obsoleto] Abre submenus de configuración. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/arrows/right.svg"></kbd> | **arrows** | --- | Flechas izquierda, derecha, arriba y abajo. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/unsynchronize/default.svg"></kbd> | **synchronize** | `ros2 erun`/`ros2 launch` | Lanza nodos o lanzadores. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/synchronize/default.svg"></kbd> | **unsynchronize** | '`ros2 kill`/`pkill` | [Obsoleto] Detiene nodos o lanzadores en ejecución. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/new/default.svg"></kbd> | **new** | `ros2 pkg create` | Crea elementos nuevos (paquetes/lanzadores/nodos). |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/run/default.svg"></kbd> | **run** | `-1` | Ejecutor de elementos. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/stop/default.svg"></kbd> | **stop** | `-1` | Detiene la ejecución de elementos. |
| <kbd><img align="left" width="22px" alt="." src="../assets/icons/bug/default.svg"></kbd> | **bug** | `-1` | Obtener backtrace de errores de ejecución. |
