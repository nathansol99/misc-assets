#!/usr/bin/env python3
"""
Script to download assets from the misc-assets repository
Usage: python download-asset.py <asset-path> [output-path]

Example:
    python download-asset.py logos/my-logo.png
    python download-asset.py images/hero.jpg ./local-hero.jpg
"""

import sys
import os
import urllib.request
import urllib.error

# Configuration
REPO_OWNER = "nathansol99"
REPO_NAME = "misc-assets"
BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}"


def download_asset(asset_path, output_path=None):
    """Download an asset from the repository."""
    # Remove leading slash if present
    asset_path = asset_path.lstrip('/')
    
    # Use asset path as output path if not specified
    if output_path is None:
        output_path = asset_path
    
    # Construct full URL
    download_url = f"{BASE_URL}/{asset_path}"
    
    print(f"Downloading: {download_url}")
    print(f"Saving to: {output_path}")
    
    # Create output directory if it doesn't exist
    output_dir = os.path.dirname(output_path)
    if output_dir and not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Download the file
    try:
        urllib.request.urlretrieve(download_url, output_path)
        print(f"Successfully downloaded: {output_path}")
        return True
    except urllib.error.HTTPError as e:
        print(f"Error: Failed to download asset (HTTP {e.code})")
        return False
    except urllib.error.URLError as e:
        print(f"Error: Failed to download asset ({e.reason})")
        return False
    except Exception as e:
        print(f"Error: {str(e)}")
        return False


def main():
    """Main entry point."""
    if len(sys.argv) < 2:
        print("Error: Asset path is required")
        print(f"Usage: {sys.argv[0]} <asset-path> [output-path]")
        print("")
        print("Example:")
        print(f"  {sys.argv[0]} logos/my-logo.png")
        print(f"  {sys.argv[0]} images/hero.jpg ./local-hero.jpg")
        sys.exit(1)
    
    asset_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None
    
    success = download_asset(asset_path, output_path)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
