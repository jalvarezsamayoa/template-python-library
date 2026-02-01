#!/bin/bash
set -e

OS="$(uname -s)"

echo "Detected OS: $OS"

case "$OS" in
    Darwin)
        echo "Updating macOS system dependencies..."
        if ! command -v brew &> /dev/null; then
            echo "Homebrew not found. Please install it from https://brew.sh/"
            exit 1
        fi
        brew install uv asdf
        ;;
    Linux)
        if [ -f /etc/debian_version ]; then
            echo "Updating Debian-based system dependencies..."
            sudo apt-get update
            sudo apt-get install -y build-essential curl git libssl-dev zlib1g-dev \
                libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
                libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

            # Install uv if missing
            if ! command -v uv &> /dev/null; then
                curl -LsSf https://astral.sh/uv/install.sh | sh
            fi

            # Install asdf if missing
            if [ ! -d "$HOME/.asdf" ]; then
                git clone https://github.com/asdf-vm/asdf.git ~/.asdf --branch v0.14.0
            fi
        else
            echo "Unsupported Linux distribution. This script supports Debian-based systems."
            exit 1
        fi
        ;;
    *)
        echo "Unsupported OS: $OS"
        exit 1
        ;;
esac

echo "System setup complete. Please ensure 'uv' and 'asdf' are in your PATH."
