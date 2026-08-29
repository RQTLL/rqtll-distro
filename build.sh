#!/usr/bin/env bash
# RQTLL Distribution Build Script
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0;37m'

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
WORKSPACE_DIR="$(cd "${SCRIPT_DIR}/.." && pwd)"
DIST_DIR="${WORKSPACE_DIR}/rqtll-distro"
IDE_DIR="${WORKSPACE_DIR}/rqtll-ide"
SERVICE_DIR="${WORKSPACE_DIR}/rqtll-service"


printf "${BLUE}RQTLL Build: ${NC}Verificando directorios de trabajo...\n"

for repo in rqtll-api rqtll-components rqtll-widgets rqtll-ide rqtll-service; do
    REPO_PATH="${WORKSPACE_DIR}/${repo}"
    if [ ! -d "${REPO_PATH}" ]; then
        printf "${BLUE}RQTLL Build: ${NC}Clonando repositorio ${repo}...\n"
        git clone "https://github.com/RQTLL/${repo}.git" "${REPO_PATH}"
        cd "${REPO_PATH}"
        git submodule update --init --recursive || true
    fi
done

NEED_APT=0
for cmd in curl make gcc g++ python3 pip3 patchelf; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        if [ "$cmd" = "pip3" ] && command -v pip >/dev/null 2>&1; then
            continue
        fi
        NEED_APT=1
        break
    fi
done

if [ $NEED_APT -eq 1 ]; then
    printf "${BLUE}RQTLL Build: ${NC}Instalando dependencias de compilación del sistema (apt)...\n"
    sudo apt update
    sudo apt install -y curl build-essential python3 python3-pip patchelf
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
    echo source "$HOME/.cargo/env" > .bashrc
    rustup update
fi

if ! command -v cargo >/dev/null 2>&1; then
    printf "${BLUE}RQTLL Build: ${NC}Instalando Rust y Cargo via rustup...\n"
    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y
    if [ -f "$HOME/.cargo/env" ]; then
        source "$HOME/.cargo/env"
    fi
    echo 'source "$HOME/.cargo/env"' >> "$HOME/.bashrc"
    echo 'source "$HOME/.cargo/env"' >> "$HOME/.zshrc"
else
    rustup update || true
fi

NEED_PYTHON_LIBS=0
for pkg in PySide6 grpc_tools google.protobuf; do
    if ! python3 -c "import ${pkg/google.protobuf/google.protobuf}" >/dev/null 2>&1; then
        NEED_PYTHON_LIBS=1
        break
    fi
done

NUITKA_EXEC="nuitka"
if ! command -v nuitka >/dev/null 2>&1; then
    if [ -f "$HOME/.local/bin/nuitka" ]; then
        NUITKA_EXEC="$HOME/.local/bin/nuitka"
    else
        NEED_PYTHON_LIBS=1
    fi
fi

if [ $NEED_PYTHON_LIBS -eq 1 ]; then
    printf "${BLUE}RQTLL Build: ${NC}Instalando dependencias de Python via pip...\n"
    pip3 install --user --break-system-packages nuitka pyside6 grpcio-tools protobuf || \
    pip3 install --user nuitka pyside6 grpcio-tools protobuf || true
    
    if [ "$NUITKA_EXEC" = "nuitka" ] && [ -f "$HOME/.local/bin/nuitka" ]; then
        NUITKA_EXEC="$HOME/.local/bin/nuitka"
    fi
fi

rm -rf "${DIST_DIR}/src"
mkdir -p "${DIST_DIR}/src/ide"
mkdir -p "${DIST_DIR}/src/service"


printf "${BLUE}RQTLL Build: ${NC}Compilando backend de Rust (rqtll-service)...\n"
cd "${SERVICE_DIR}"
if [ -d "external/rqtll-api/proto" ]; then
    cargo build --release
else
    cargo build --release
fi

cp "target/release/rqtll_service" "${DIST_DIR}/src/service/rqtll_service"
cp "src/services/image_bridge.py" "${DIST_DIR}/src/service/image_bridge.py"
chmod +x "${DIST_DIR}/src/service/rqtll_service"
chmod +x "${DIST_DIR}/src/service/image_bridge.py"


printf "${BLUE}RQTLL Build: ${NC}Compilando frontend (rqtll-ide) con Nuitka...\n"
cd "${IDE_DIR}"
rm -rf main.build main.dist

if [ -f "external/rqtll_api/py.sh" ]; then
    cd external/rqtll_api
    chmod +x py.sh || true
    bash ./py.sh
    cd "${IDE_DIR}"
fi

PYTHONPATH=external/rqtll_api/py "${NUITKA_EXEC}" --standalone --enable-plugin=pyside6 main.py
if [ -f "main.dist/main.bin" ]; then
    mv "main.dist/main.bin" "main.dist/main"
fi

mkdir -p "main.dist/external"
cp -r "external/rqtll_components" "main.dist/external/"
cp -r "external/rqtll_widgets" "main.dist/external/"
cp -r "external/rqtll_api" "main.dist/external/"

rm -rf "${DIST_DIR}/src/ide"
mkdir -p "${DIST_DIR}/src/ide"
cp -a main.dist/. "${DIST_DIR}/src/ide/"
chmod +x "${DIST_DIR}/src/ide/main"
rm -rf main.build main.dist

printf "${GREEN}RQTLL Build: ${NC}Construcción finalizada con éxito\n"
