# Hanchen David Wang - Personal Website

This repository contains my personal website and CV automation system.

## Structure

```
├── docs/                    # Website content (GitHub Pages)
├── data/                    # Source data (JSON) - EDIT THESE!
│   ├── personal.json       # Name, email, contact info
│   ├── education.json      # Degrees and institutions
│   ├── employment.json     # Work experience and internships
│   ├── research.json       # Research projects
│   ├── publications.json   # Papers and publications
│   ├── projects.json       # Course projects
│   └── skills.json         # Technical skills
├── templates/
│   ├── simple/             # t1: Clean, simple template
│   └── moderncv/           # t2: ModernCV template (in cv_template-main/)
├── scripts/                # Generation scripts
└── run.sh                  # Main build script
```

## Workflow

1. **Edit**: Update JSON files in `data/` folder
2. **Generate**: Run `./run.sh` or `./run.sh t1` (for simple template)
3. **Deploy**: Commit and push (GitHub Actions handles the rest)

### Templates

- `./run.sh` or `./run.sh t2` - ModernCV template (default, colorful)
- `./run.sh t1` - Simple clean template (Word-like)

## GitHub Pages

Website is served from the `docs/` folder.
Configure in: Settings → Pages → Source → Branch: main, Folder: /docs
