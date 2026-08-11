#!/usr/bin/env bash
# RQTLL Installer
set -euo pipefail

RED='\033[0;31m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0;37m'

if [ "$(id -u)" -ne 0 ]; then
    printf "${RED}RQTLL Installer: ${NC}Este script debe ser ejecutado con privilegios de administrador (sudo).\n"
    exit 1
fi


printf "${BLUE}RQTLL Installer: ${NC}Verificando directorios de trabajo\n"

CLONED_TEMP=0
TEMP_DIR="/tmp/rqtll-distro-temp"

if [ ! -d "src/ide" ] || [ ! -d "src/service" ]; then
    printf "${BLUE}RQTLL Installer: ${NC}Clonando rqtll-distro para obtener los binarios...\n"
    rm -rf "${TEMP_DIR}"
    git clone --recursive https://github.com/RQTLL/rqtll-distro.git "${TEMP_DIR}"
    cd "${TEMP_DIR}"
    CLONED_TEMP=1
fi

INSTALL_DIR="/opt/rqtll"
IDE_BIN_LINK="/usr/bin/rqtll-ide"
SERVICE_BIN="/usr/sbin/rqtll-service"
SHARE_DIR="/usr/share/rqtll"
ICON_SYSTEM_DIR="/usr/share/icons/hicolor/scalable/apps"
DESKTOP_SYSTEM_DIR="/usr/share/applications"
USER_HOME="${SUDO_USER_HOME:-/home/${SUDO_USER:-root}}"
USER_ICON_DIR="${USER_HOME}/.local/share/icons"
USER_DESKTOP_DIR="${USER_HOME}/.local/share/applications"


printf "${BLUE}RQTLL Installer: ${NC}Creando directorios del sistema...\n"

rm -rf "${INSTALL_DIR}"
rm -rf "${SERVICE_BIN}"
rm -rf "${SHARE_DIR}"
mkdir -p "${INSTALL_DIR}"
mkdir -p "${SHARE_DIR}"
mkdir -p "${ICON_SYSTEM_DIR}"
mkdir -p "${DESKTOP_SYSTEM_DIR}"
if [ -n "${SUDO_USER:-}" ]; then
    mkdir -p "${USER_ICON_DIR}"
    mkdir -p "${USER_DESKTOP_DIR}"
fi

if [ -d "src/ide" ] && [ "$(ls -A src/ide)" ]; then
    rm -rf "${INSTALL_DIR}/ide"
    cp -r src/ide "${INSTALL_DIR}/ide"
    chmod +x "${INSTALL_DIR}/ide/main"
else
    printf "${RED}RQTLL Installer: ${NC}No se encontraron los archivos de la IDE.\n"
    exit 1
fi

if [ -f "src/service/rqtll_service" ]; then
    cp src/service/rqtll_service "${SERVICE_BIN}"
    chmod +x "${SERVICE_BIN}"
elif [ -f "src/service/rqtll_rcl_utils" ]; then
    cp src/service/rqtll_rcl_utils "${SERVICE_BIN}"
    chmod +x "${SERVICE_BIN}"
else
    printf "${RED}RQTLL Installer: ${NC}No se encontraron los archivos del backend.\n"
    exit 1
fi

if [ -f "src/service/image_bridge.py" ]; then
    cp src/service/image_bridge.py "${SHARE_DIR}/image_bridge.py"
    chmod +x "${SHARE_DIR}/image_bridge.py"
else
    if [ -f "../rqtll-service/src/services/image_bridge.py" ]; then
        cp ../rqtll-service/src/services/image_bridge.py "${SHARE_DIR}/image_bridge.py"
        chmod +x "${SHARE_DIR}/image_bridge.py"
    else
        printf "${RED}RQTLL Installer: ${NC}No se encontró image_bridge.py.\n"
        exit 1
    fi
fi


printf "${BLUE}RQTLL Installer: ${NC}Creando script de arranque...\n"

cat << 'EOF' > "${IDE_BIN_LINK}"
#!/usr/bin/env bash
# wrapper script for rqtll-ide to load libraries and resource files correctly

if ! pgrep -x "rqtll_service" >/dev/null && ! pgrep -f "rqtll-service" >/dev/null; then
    /usr/sbin/rqtll-service >/dev/null 2>&1 &
    sleep 0.5
fi

cd /opt/rqtll/ide
exec ./main "$@"
EOF
chmod +x "${IDE_BIN_LINK}"


printf "${BLUE}RQTLL Installer: ${NC}Instalando iconos...\n"

LOGO_SOURCE=""
for path in "../rqtll-components/assets/branding/logo-main-color.svg" "src/ide/external/rqtll_components/assets/branding/logo-main-color.svg" "/opt/rqtll/ide/external/rqtll_components/assets/branding/logo-main-color.svg"; do
    if [ -f "${path}" ]; then
        LOGO_SOURCE="${path}"
        break
    fi
done

if [ -n "${LOGO_SOURCE}" ]; then
    cp "${LOGO_SOURCE}" "${ICON_SYSTEM_DIR}/rqtll.svg"
    if [ -n "${SUDO_USER:-}" ]; then
        cp "${LOGO_SOURCE}" "${USER_ICON_DIR}/rqtll.svg"
        chown -R "${SUDO_USER}:${SUDO_USER}" "${USER_ICON_DIR}/rqtll.svg" || true
    fi
    if command -v gtk-update-icon-cache >/dev/null 2>&1; then
        gtk-update-icon-cache -f -t /usr/share/icons/hicolor || true
    fi
else
    printf "${RED}RQTLL Installer: ${NC}No se encontró el logotipo oficial.\n"
    exit 1
fi


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

# Cleanup temporary clone
if [ "${CLONED_TEMP}" -eq 1 ]; then
    printf "${BLUE}RQTLL Installer: ${NC}Limpiando directorios temporales clonados...\n"
    cd /
    rm -rf "${TEMP_DIR}"
fi

printf "${GREEN}RQTLL Installer: ${NC}Instalación completada con éxito\n"