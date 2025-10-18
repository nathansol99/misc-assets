# Download Scripts

This directory contains scripts to help download assets from this repository.

## Available Scripts

### Bash Script (`download-asset.sh`)

A shell script for downloading assets. Works on Linux, macOS, and WSL.

**Usage:**
```bash
./download-asset.sh <asset-path> [output-path]
```

**Examples:**
```bash
# Download a logo to the current directory
./download-asset.sh logos/my-logo.png

# Download an image to a specific location
./download-asset.sh images/hero.jpg ./my-hero.jpg
```

**Requirements:**
- `curl` or `wget`

### Python Script (`download-asset.py`)

A Python script for downloading assets. Works on any platform with Python 3.

**Usage:**
```bash
python download-asset.py <asset-path> [output-path]
```

**Examples:**
```bash
# Download a logo to the current directory
python download-asset.py logos/my-logo.png

# Download an image to a specific location
python download-asset.py images/hero.jpg ./my-hero.jpg
```

**Requirements:**
- Python 3.x

## Direct Download URLs

You can also download assets directly using their raw GitHub URL:

```
https://raw.githubusercontent.com/nathansol99/misc-assets/main/<asset-path>
```

For example:
```
https://raw.githubusercontent.com/nathansol99/misc-assets/main/logos/my-logo.png
```
