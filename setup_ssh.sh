#!/usr/bin/env bash
# ── SSH Key Setup for GitHub (Fix #1 + #2) ───────────────────────────────────
# Usage: bash setup_ssh.sh your@email.com
# ─────────────────────────────────────────────────────────────────────────────

set -euo pipefail

EMAIL="${1:?Usage: bash setup_ssh.sh your@email.com}"
KEY_PATH="$HOME/.ssh/id_ed25519"

echo ">>> Generating SSH key..."
# Fix #2: use uppercase -C (not lowercase -c)
ssh-keygen -t ed25519 -C "$EMAIL" -f "$KEY_PATH" -N ""

echo ">>> Starting ssh-agent..."
eval "$(ssh-agent -s)"
ssh-add "$KEY_PATH"

echo ""
echo ">>> Copy this public key to GitHub → Settings → SSH Keys:"
echo "────────────────────────────────────────────────────────"
cat "${KEY_PATH}.pub"
echo "────────────────────────────────────────────────────────"
echo ""
echo ">>> After adding the key to GitHub, test with:"
echo "    ssh -T git@github.com"
echo ""
echo ">>> Then clone your repo via SSH (not HTTPS):"
echo "    git clone git@github.com:USERNAME/REPO.git"