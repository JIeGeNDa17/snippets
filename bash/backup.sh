#!/usr/bin/env bash
set -euo pipefail
tar czf "backup-$(date +%F).tar.gz" "$1"
