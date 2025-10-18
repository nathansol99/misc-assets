#!/bin/bash
# Script to download assets from the misc-assets repository
# Usage: ./download-asset.sh <asset-path> [output-path]
#
# Example:
#   ./download-asset.sh logos/my-logo.png
#   ./download-asset.sh images/hero.jpg ./local-hero.jpg

set -e

# Configuration
REPO_OWNER="nathansol99"
REPO_NAME="misc-assets"
BRANCH="main"
BASE_URL="https://raw.githubusercontent.com/${REPO_OWNER}/${REPO_NAME}/${BRANCH}"

# Check if asset path is provided
if [ $# -eq 0 ]; then
    echo "Error: Asset path is required"
    echo "Usage: $0 <asset-path> [output-path]"
    echo ""
    echo "Example:"
    echo "  $0 logos/my-logo.png"
    echo "  $0 images/hero.jpg ./local-hero.jpg"
    exit 1
fi

ASSET_PATH="$1"
OUTPUT_PATH="${2:-${ASSET_PATH}}"

# Remove leading slash if present
ASSET_PATH="${ASSET_PATH#/}"

# Construct full URL
DOWNLOAD_URL="${BASE_URL}/${ASSET_PATH}"

echo "Downloading: ${DOWNLOAD_URL}"
echo "Saving to: ${OUTPUT_PATH}"

# Create output directory if it doesn't exist
OUTPUT_DIR=$(dirname "${OUTPUT_PATH}")
if [ ! -d "${OUTPUT_DIR}" ] && [ "${OUTPUT_DIR}" != "." ]; then
    mkdir -p "${OUTPUT_DIR}"
fi

# Download the file
if command -v curl &> /dev/null; then
    curl -L -f -o "${OUTPUT_PATH}" "${DOWNLOAD_URL}"
elif command -v wget &> /dev/null; then
    wget -O "${OUTPUT_PATH}" "${DOWNLOAD_URL}"
else
    echo "Error: Neither curl nor wget is available"
    exit 1
fi

if [ $? -eq 0 ]; then
    echo "Successfully downloaded: ${OUTPUT_PATH}"
else
    echo "Error: Failed to download asset"
    exit 1
fi
