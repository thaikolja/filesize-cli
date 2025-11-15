#!/bin/bash
# Script to update SHA256 in Homebrew formula

set -e

VERSION="2.0.0"
URL="https://github.com/thaikolja/filesize-cli/archive/refs/tags/v${VERSION}.tar.gz"

echo "Downloading ${URL} to calculate SHA256..."
TEMP_FILE=$(mktemp)
curl -sSL "$URL" -o "$TEMP_FILE"

SHA256=$(shasum -a 256 "$TEMP_FILE" | cut -d' ' -f1)
rm "$TEMP_FILE"

echo "SHA256 for v${VERSION}: ${SHA256}"

# Update the formula
sed -i.bak "s/sha256 \"[^\"]*\"/sha256 \"${SHA256}\"/" homebrew/filesize-cli.rb
rm homebrew/filesize-cli.rb.bak

echo "Updated homebrew/filesize-cli.rb with new SHA256"
