# rqtll-distro

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-light.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-dark.svg">
  <img alt="RQTLL Logo" src="https://github.com/RQTLL/rqtll-components/blob/main/assets/branding/logo-main-color.svg" width="50px">
</picture>

Repositorio de metadatos de distribución y empaquetado para el ecosistema RQTLL. Este repositorio centraliza la configuración de versiones oficiales, dependencias aprobadas y recetas de distribución para diferentes derivadas de Ubuntu compatibles con ROS2.
<!-- instrucciones para compilar rqtll-ide y rqtll-service a partir de los submodulos de git-->

<!-- gen `install.sh`: Mueve los binarios de rqtll-ide (python) y rqtll-service (Rust) a /opt/rqtll, crea enlaces simbólicos a /usr/local/bin, crea los servicios en /etc/systemd/user, establece las variables de entorno necesarias en /etc/profile.d, crea enlaces simbólicos a /usr/share/applications y /usr/share/icons, genera un script de desinstalación. -->

## Table of Contents
- [rqtll-distro](#rqtll-distro)
  - [Table of Contents](#table-of-contents)
  - [Quickstart](#quickstart)
    - [Requisitos](#requisitos)
    - [Descargar el código](#descargar-el-código)
    - [Compilar rqtll-ide](#compilar-rqtll-ide)
  - [Compilar rqtll-service](#compilar-rqtll-service)
    - [Verificar script de instalación](#verificar-script-de-instalación)
  - [Estructura de Distribución](#estructura-de-distribución)
  - [Cómo contribuir](#cómo-contribuir)
  - [Security](#security)
  - [License](#license)
  - [Maintainers](#maintainers)

## Quickstart

Este repositorio contiene los metadatos y scripts para construir y publicar los binarios de RQTLL (`rqtll-ide` y `rqtll-service`).

### Requisitos
- Un sistema operativo basado en Ubuntu 20.04 o superior.
- Python3
- Cargo

### Descargar el código
```bash
git clone https://github.com/RQTLL/rqtll-distro.git
cd rqtll-distro
git submodule update --init --recursive
```

### Compilar rqtll-ide

```bash
# Entrar al submodulo rqtll-ide
cd external/rqtll-ide

# Instalar dependencias de Python
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
```
Dentro de `py-compile.sh`:

```bash
export PTHONPATH=./py-install
LIBS=(
PySide6.QtWidgets, PySide6.QtCore, PySide6.QtSvg, PySide6.QtGui, sys, os, protobuf, urllib.request, io, typing, __future__, uuid, dataclasses, tempfile, xml.etree.ElementTree, grpc, warnings, google.protobuf, re, importlib, time, subprocess, hashlib, shlex, codecs, json, html, base64
)
DIRS=(
rqtll_ide, rqtll_api, rqtll_components, rqtll_widgets
)
OPTS=(
--standalone 
--output-dir=./dist \
--include-package=rqtll_ide \
--include-package=rqtll_api \
--include-package=rqtll_components \
--include-package=rqtll_widgets \
--include-module=grpc._channel
--include-module=google.protobuf.json_format
)
for i in ${LIBS[@]}
do
	OPTS+=("--include-module=$i")
done
python3 -m nuitka3 ${OPTS} ${DIRS}
```

## Compilar rqtll-service

```bash
# Entrar al submodulo rqtll-service
cd external/rqtll-service

# Construir el binario
cargo build --release
```

### Verificar script de instalación
```bash
bash install.sh
```

---

## Estructura de Distribución

Este repositorio gestiona el empaquetado final agrupando todos los componentes del ecosistema:

```text
./
├── LICENSE
├── README.md
├── CONTRIBUTING.md
└── SECURITY.md
```

## Cómo contribuir

- Lee [CONTRIBUTING.md](CONTRIBUTING.md) antes de enviar un Pull Request.
- Para proponer actualizaciones en recetas de empaquetado o configuraciones de instalación, abre un issue detallando los cambios de dependencias del sistema operativo.
- Las contribuciones deben pasar las validaciones de construcción del paquete de distribución local antes de ser integradas.

## Security

Consulta [SECURITY.md](SECURITY.md) para conocer el procedimiento de reporte de vulnerabilidades.

## License

Este proyecto está bajo la licencia **MIT**. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Maintainers

* **adnKSharp** <adnksharp@gmail.com>
