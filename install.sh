#!/bin/bash
# filesize-cli installation script
# Installs filesize-cli globally with minimal user interaction

set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Function to print colored output
print_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

print_error() {
    echo -e "${RED}✗ $1${NC}"
}

print_info() {
    echo -e "${YELLOW}ℹ $1${NC}"
}

# Check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Installation methods
install_with_pipx() {
    print_info "Installing with pipx..."
    if ! command_exists pipx; then
        print_info "pipx not found. Installing pipx..."
        python3 -m pip install --user pipx
        python3 -m pipx ensurepath
    fi
    pipx install filesize-cli
    print_success "filesize-cli installed with pipx"
}

install_with_pip() {
    print_info "Installing with pip..."
    pip3 install --user filesize-cli
    print_success "filesize-cli installed with pip"
}

install_with_homebrew() {
    print_info "Installing with Homebrew..."
    if brew install filesize-cli 2>/dev/null; then
        print_success "filesize-cli installed with Homebrew"
    else
        print_info "filesize-cli not found in Homebrew. Falling back to pipx..."
        install_with_pipx
    fi
}

install_from_source() {
    print_info "Installing from source..."
    
    # Create temp directory
    TEMP_DIR=$(mktemp -d)
    cd "$TEMP_DIR"
    
    # Clone and install
    git clone https://github.com/thaikolja/filesize-cli.git
    cd filesize-cli
    pip3 install .
    
    # Cleanup
    cd ..
    rm -rf "$TEMP_DIR"
    
    print_success "filesize-cli installed from source"
}

# Main installation logic
main() {
    echo "filesize-cli v2.0.0 Installation Script"
    echo "======================================="
    echo ""
    
    # Detect OS
    if [[ "$OSTYPE" == "darwin"* ]]; then
        OS="macOS"
    elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
        OS="Linux"
    else
        OS="Unknown"
    fi
    
    print_info "Detected OS: $OS"
    
    # Check Python installation
    if ! command_exists python3; then
        print_error "Python 3 is required but not installed"
        exit 1
    fi
    
    # Try different installation methods
    if command_exists brew && command_exists pipx; then
        echo "Choose installation method:"
        echo "1) Homebrew (recommended for macOS)"
        echo "2) pipx (recommended for cross-platform)"
        echo "3) pip (system-wide)"
        echo "4) From source"
        echo "5) Auto-select best method"
        echo ""
        read -p "Enter choice [1-5]: " choice
        
        case $choice in
            1) install_with_homebrew ;;
            2) install_with_pipx ;;
            3) install_with_pip ;;
            4) install_from_source ;;
            5)
                if command_exists brew; then
                    install_with_homebrew
                elif command_exists pipx; then
                    install_with_pipx
                else
                    install_with_pip
                fi
                ;;
            *) 
                print_error "Invalid choice"
                exit 1
                ;;
        esac
    else
        print_info "Auto-selecting installation method..."
        if command_exists brew; then
            install_with_homebrew
        elif command_exists pipx; then
            install_with_pipx
        else
            install_with_pip
        fi
    fi
    
    # Verify installation
    echo ""
    print_info "Verifying installation..."
    if command_exists filesize; then
        VERSION=$(filesize --version 2>&1)
        print_success "Installation verified: $VERSION"
        echo ""
        print_info "Usage examples:"
        echo "  filesize file.txt          # Show file size"
        echo "  filesize -r directory/     # Recursive directory size"
        echo "  filesize -u mb file.txt    # Force megabytes"
        echo "  filesize -c file.txt       # Raw bytes only"
        echo ""
        print_success "Installation complete!"
    else
        print_error "Installation failed. filesize command not found."
        print_info "You may need to restart your terminal or update your PATH."
        exit 1
    fi
}

# Run main function
main "$@"