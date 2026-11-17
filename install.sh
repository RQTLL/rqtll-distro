#!/usr/bin/env bash
# RQTLL Installer
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m'

if [ "$(id -u)" -ne 0 ]; then
    printf "${RED}RQTLL Installer: ${NC}Este script debe ser ejecutado con privilegios de administrador (sudo).\n"
    exit 1
fi

RAW_ARCH=$(dpkg --print-architecture 2>/dev/null || uname -m)
case "${RAW_ARCH}" in
    x86_64|amd64)
        TARGET_ARCH="amd64"
        ;;
    aarch64|arm64)
        TARGET_ARCH="arm64"
        ;;
    *)
        printf "${RED}RQTLL Installer: ${NC}Arquitectura no soportada: %s\n" "${RAW_ARCH}"
        exit 1
        ;;
esac

SRC_BASE="src/${TARGET_ARCH}"
TEMP_DIR=""
STAGING_DIR=""

cleanup_installer() {
    if [ -n "${TEMP_DIR}" ] && [ -d "${TEMP_DIR}" ]; then
        rm -rf "${TEMP_DIR}"
    fi
    if [ -n "${STAGING_DIR}" ] && [ -d "${STAGING_DIR}" ]; then
        rm -rf "${STAGING_DIR}"
    fi
}
trap cleanup_installer EXIT INT TERM

printf "${BLUE}RQTLL Installer: ${NC}Arquitectura detectada: ${GREEN}${TARGET_ARCH}${NC}\n"
printf "${BLUE}RQTLL Installer: ${NC}Verificando dependencias del sistema...\n"

NEEDED_PKGS=()
if ! dpkg -s libxcb-cursor0 >/dev/null 2>&1; then
    NEEDED_PKGS+=("libxcb-cursor0")
fi

NEED_CLONE=0
if [ ! -d "${SRC_BASE}/ide" ] || [ ! -d "${SRC_BASE}/service" ]; then
    NEED_CLONE=1
    if ! command -v git >/dev/null 2>&1; then
        NEEDED_PKGS+=("git")
    fi
fi

if [ "${#NEEDED_PKGS[@]}" -gt 0 ]; then
    apt-get update -qq
    DEBIAN_FRONTEND=noninteractive apt-get install -y -qq "${NEEDED_PKGS[@]}"
fi

if [ "${NEED_CLONE}" -eq 1 ]; then
    TEMP_DIR=$(mktemp -d /tmp/rqtll-distro-XXXXXX)
    printf "${BLUE}RQTLL Installer: ${NC}Clonando rqtll-distro en entorno temporal aislado...\n"
    if ! git clone --depth 1 --recursive https://github.com/RQTLL/rqtll-distro.git "${TEMP_DIR}"; then
        printf "${RED}RQTLL Installer: ${NC}Error de red al clonar el repositorio. La instalación previa no fue modificada.\n"
        exit 1
    fi
    cd "${TEMP_DIR}"
fi

# Validación completa de artefactos antes de modificar la instalación existente
if [ ! -f "${SRC_BASE}/ide/main" ] || [ -z "$(ls -A "${SRC_BASE}/ide" 2>/dev/null)" ]; then
    printf "${RED}RQTLL Installer: ${NC}No se encontraron los binarios de la IDE para ${TARGET_ARCH} en ${SRC_BASE}/ide.\n"
    exit 1
fi

SERVICE_SOURCE=""
if [ -f "${SRC_BASE}/service/rqtll_service" ]; then
    SERVICE_SOURCE="${SRC_BASE}/service/rqtll_service"
elif [ -f "${SRC_BASE}/service/rqtll_rcl_utils" ]; then
    SERVICE_SOURCE="${SRC_BASE}/service/rqtll_rcl_utils"
else
    printf "${RED}RQTLL Installer: ${NC}No se encontró el binario del backend en ${SRC_BASE}/service.\n"
    exit 1
fi

BRIDGE_SOURCE=""
if [ -f "${SRC_BASE}/service/image_bridge.py" ]; then
    BRIDGE_SOURCE="${SRC_BASE}/service/image_bridge.py"
elif [ -f "../rqtll-service/src/services/image_bridge.py" ]; then
    BRIDGE_SOURCE="../rqtll-service/src/services/image_bridge.py"
else
    printf "${RED}RQTLL Installer: ${NC}No se encontró image_bridge.py.\n"
    exit 1
fi

LOGO_SOURCE=""
for path in "../rqtll-components/assets/branding/logo-main-color.svg" \
            "${SRC_BASE}/ide/external/rqtll_components/assets/branding/logo-main-color.svg"; do
    if [ -f "${path}" ]; then
        LOGO_SOURCE="${path}"
        break
    fi
done

if [ -z "${LOGO_SOURCE}" ]; then
    printf "${RED}RQTLL Installer: ${NC}No se encontró el logotipo oficial.\n"
    exit 1
fi

# Preparación completa en área temporal antes de reemplazar la instalación actual
printf "${BLUE}RQTLL Installer: ${NC}Preparando paquetes de instalación...\n"
STAGING_DIR=$(mktemp -d /tmp/rqtll-stage-XXXXXX)
mkdir -p "${STAGING_DIR}/opt_rqtll" "${STAGING_DIR}/share_rqtll"

cp -r "${SRC_BASE}/ide" "${STAGING_DIR}/opt_rqtll/ide"
chmod +x "${STAGING_DIR}/opt_rqtll/ide/main"

cp "${SERVICE_SOURCE}" "${STAGING_DIR}/rqtll-service"
chmod +x "${STAGING_DIR}/rqtll-service"

cp "${BRIDGE_SOURCE}" "${STAGING_DIR}/share_rqtll/image_bridge.py"
chmod +x "${STAGING_DIR}/share_rqtll/image_bridge.py"

cp "${LOGO_SOURCE}" "${STAGING_DIR}/rqtll.svg"

INSTALL_DIR="/opt/rqtll"
IDE_BIN_LINK="/usr/bin/rqtll-ide"
SERVICE_BIN="/usr/sbin/rqtll-service"
SHARE_DIR="/usr/share/rqtll"
ICON_SYSTEM_DIR="/usr/share/icons/hicolor/scalable/apps"
DESKTOP_SYSTEM_DIR="/usr/share/applications"
USER_HOME="${SUDO_USER_HOME:-/home/${SUDO_USER:-root}}"
USER_ICON_DIR="${USER_HOME}/.local/share/icons"
USER_DESKTOP_DIR="${USER_HOME}/.local/share/applications"

printf "${BLUE}RQTLL Installer: ${NC}Desplegando archivos en el sistema...\n"

mkdir -p "${ICON_SYSTEM_DIR}" "${DESKTOP_SYSTEM_DIR}"
rm -rf "${INSTALL_DIR}" "${SERVICE_BIN}" "${SHARE_DIR}"

mv "${STAGING_DIR}/opt_rqtll" "${INSTALL_DIR}"
mv "${STAGING_DIR}/rqtll-service" "${SERVICE_BIN}"
mv "${STAGING_DIR}/share_rqtll" "${SHARE_DIR}"
cp "${STAGING_DIR}/rqtll.svg" "${ICON_SYSTEM_DIR}/rqtll.svg"

if [ -n "${SUDO_USER:-}" ]; then
    mkdir -p "${USER_ICON_DIR}" "${USER_DESKTOP_DIR}"
    cp "${STAGING_DIR}/rqtll.svg" "${USER_ICON_DIR}/rqtll.svg"
    chown -R "${SUDO_USER}:${SUDO_USER}" "${USER_ICON_DIR}/rqtll.svg" || true
fi

if command -v gtk-update-icon-cache >/dev/null 2>&1; then
    gtk-update-icon-cache -f -t /usr/share/icons/hicolor || true
fi

printf "${BLUE}RQTLL Installer: ${NC}Creando script de arranque...\n"

cat << 'EOF' > "${IDE_BIN_LINK}"
#!/usr/bin/env bash
# Wrapper script para rqtll-ide con verificación activa del servidor gRPC
export PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python

SERVICE_PID=""
GRPC_HOST="127.0.0.1"
GRPC_PORT=50051
MAX_RETRIES=100

cleanup() {
    if [ -n "${SERVICE_PID}" ] && kill -0 "${SERVICE_PID}" 2>/dev/null; then
        kill "${SERVICE_PID}" 2>/dev/null
        wait "${SERVICE_PID}" 2>/dev/null
    fi
}

trap cleanup EXIT INT TERM

is_service_ready() {
    (echo >/dev/tcp/"${GRPC_HOST}"/"${GRPC_PORT}") >/dev/null 2>&1
}

if ! is_service_ready; then
    /usr/sbin/rqtll-service >/dev/null 2>&1 &
    SERVICE_PID=$!

    READY=0
    for ((i=0; i<MAX_RETRIES; i++)); do
        if ! kill -0 "${SERVICE_PID}" 2>/dev/null; then
            printf "Error: rqtll-service finalizó inesperadamente durante el arranque.\n" >&2
            exit 1
        fi
        if is_service_ready; then
            READY=1
            break
        fi
        sleep 0.1
    done

    if [ "${READY}" -ne 1 ]; then
        printf "Error: Tiempo de espera agotado (10 s) esperando a rqtll-service en %s:%s.\n" "${GRPC_HOST}" "${GRPC_PORT}" >&2
        exit 1
    fi
fi

cd /opt/rqtll/ide || exit 1
./main "$@"
EOF
chmod +x "${IDE_BIN_LINK}"

printf "${BLUE}RQTLL Installer: ${NC}Creando lanzadores...\n"

DESKTOP_CONTENT="[Desktop Entry]
Type=Application
Name=RQTLL IDE
Comment=Entorno de Desarrollo para ROS 2
Exec=${IDE_BIN_LINK}
Icon=rqtll
Terminal=false
Categories=Development;IDE;Robotics;
StartupWMClass=rqtll-ide
"

echo "${DESKTOP_CONTENT}" > "${DESKTOP_SYSTEM_DIR}/rqtll.desktop"
chmod 644 "${DESKTOP_SYSTEM_DIR}/rqtll.desktop"

if [ -n "${SUDO_USER:-}" ]; then
    echo "${DESKTOP_CONTENT}" > "${USER_DESKTOP_DIR}/rqtll.desktop"
    chmod 644 "${USER_DESKTOP_DIR}/rqtll.desktop"
    chown "${SUDO_USER}:${SUDO_USER}" "${USER_DESKTOP_DIR}/rqtll.desktop" || true
fi

cd /
printf "${GREEN}RQTLL Installer: ${NC}Instalación completada con éxito para ${TARGET_ARCH}\n"
