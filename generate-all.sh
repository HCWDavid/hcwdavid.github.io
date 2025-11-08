#!/bin/bash
# Generate all content from JSON source

set -e

echo "🔄 Generating content from JSON..."
echo ""

# Generate LaTeX files
echo "📝 Generating LaTeX CV sections..."
python3 scripts/generate-latex.py

echo ""

# Generate website content
echo "🌐 Generating website content..."
python3 scripts/generate-website.py

echo ""
echo "✅ All content generated successfully!"
echo ""
echo "Next steps:"
echo "  1. Review the generated files"
echo "  2. Run './build-cv-local.sh' to build the PDF (optional)"
echo "  3. Commit and push to deploy"
