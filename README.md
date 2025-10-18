# misc-assets

A general-purpose repository for storing and sharing assets like logos, images, icons, and documents across multiple projects.

## Purpose

This repository serves as a centralized location for miscellaneous assets that can be easily pulled down using scripts or direct URLs. It's designed to make asset management simple and accessible across different projects and environments.

## Repository Structure

```
misc-assets/
├── logos/          # Logo files for projects and brands
├── images/         # General images and photos
├── icons/          # Icon files for UI elements
├── documents/      # Document files and templates
└── scripts/        # Download scripts for easy asset retrieval
```

Each directory contains its own README with specific guidelines for that asset type.

## How to Use

### Method 1: Download Scripts

Use the provided scripts in the `scripts/` directory to download assets programmatically.

**Bash:**
```bash
curl -O https://raw.githubusercontent.com/nathansol99/misc-assets/main/scripts/download-asset.sh
chmod +x download-asset.sh
./download-asset.sh logos/my-logo.png
```

**Python:**
```bash
curl -O https://raw.githubusercontent.com/nathansol99/misc-assets/main/scripts/download-asset.py
python download-asset.py logos/my-logo.png
```

### Method 2: Direct Download URLs

Access assets directly via their raw GitHub URL:

```
https://raw.githubusercontent.com/nathansol99/misc-assets/main/<asset-path>
```

**Example:**
```
https://raw.githubusercontent.com/nathansol99/misc-assets/main/logos/my-logo.png
```

### Method 3: Git Clone

Clone the entire repository to have local access to all assets:

```bash
git clone https://github.com/nathansol99/misc-assets.git
```

### Method 4: Wget or Curl

Download individual files using `wget` or `curl`:

```bash
# Using curl
curl -O https://raw.githubusercontent.com/nathansol99/misc-assets/main/logos/my-logo.png

# Using wget
wget https://raw.githubusercontent.com/nathansol99/misc-assets/main/logos/my-logo.png
```

## Naming Conventions

- Use lowercase with hyphens for file names (e.g., `my-project-logo.png`)
- Use descriptive names that indicate the content or purpose
- Include size dimensions or variants when applicable (e.g., `logo-small.png`, `icon-24x24.png`)
- Organize related assets in subdirectories within their respective category

## Contributing

To add new assets:

1. Fork this repository
2. Add your assets to the appropriate directory following the naming conventions
3. Update the relevant README if needed
4. Submit a pull request

## License

Please ensure you have the rights to any assets you add to this repository. By contributing, you agree that your contributions will be used across various projects.
