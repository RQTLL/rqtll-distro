#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROTO_DIR="$ROOT_DIR/proto"
OUT_DIR="$ROOT_DIR/py"

mkdir -p "$OUT_DIR"

mapfile -t PROTO_FILES < <(find "$PROTO_DIR" -maxdepth 1 -type f -name "*.proto" | sort)

if [[ ${#PROTO_FILES[@]} -eq 0 ]]; then
	echo "No se encontraron archivos proto en $PROTO_DIR"
	exit 1
fi

FAILED=0

for proto_file in "${PROTO_FILES[@]}"; do
	if ! python3 -m grpc_tools.protoc \
		-I"$PROTO_DIR" \
		--python_out="$OUT_DIR" \
		--grpc_python_out="$OUT_DIR" \
		"$proto_file"; then
		echo "Fallo compilando: $proto_file"
		FAILED=1
	fi
done

if [[ $FAILED -ne 0 ]]; then
	echo "Algunos contratos no pudieron compilarse"
	exit 1
fi
