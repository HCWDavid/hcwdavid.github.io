# Hanchen David Wang - Personal Website

This repository contains my personal website and CV automation system.

## Structure

```
├── docs/                    # Website content (GitHub Pages)
├── data/                    # Source data (JSON)
│   └── cv-content.json     # Single source of truth
├── scripts/                 # Generation scripts
│   ├── generate-latex.py   # Generate CV LaTeX
│   └── generate-website.py # Generate website content
├── cv_template-main/        # CV build system
├── generate-all.sh          # Generate everything from JSON
└── build-cv-local.sh        # Build CV locally
```

## Workflow

1. **Edit**: Update `data/cv-content.json`
2. **Generate**: Run `./generate-all.sh`
3. **Build**: Run `./build-cv-local.sh` (optional, to preview PDF)
4. **Deploy**: Commit and push (GitHub Actions handles the rest)

## GitHub Pages

Website is served from the `docs/` folder.
Configure in: Settings → Pages → Source → Branch: main, Folder: /docs
