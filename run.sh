#!/bin/bash
# Main build script - generates CV and website from JSON data

set -e

# Default template
TEMPLATE="${1:-t1}"

if [[ "$TEMPLATE" != "t1" && "$TEMPLATE" != "t2" ]]; then
    echo "❌ Invalid template. Use: ./run.sh [t1|t2]"
    echo "   t1 = Simple clean template (default)"
    echo "   t2 = ModernCV template"
    exit 1
fi

echo "🔄 Building with template: $TEMPLATE"
echo ""

# Generate LaTeX and website content
echo "📝 Generating content from JSON..."

if [ "$TEMPLATE" = "t1" ]; then
    python3 scripts/generate-t1.py
else
    python3 scripts/generate-t2.py
fi

echo ""
echo "🌐 Generating website..."
python3 scripts/generate-website.py

echo ""
echo "� Generating search index..."
python3 scripts/generate-search-index.py

echo ""
echo "�📄 Building PDF..."

if [ "$TEMPLATE" = "t1" ]; then
    # Build simple template with xelatex
    cd templates/simple/
    xelatex -interaction=nonstopmode cv.tex > /dev/null 2>&1
    xelatex -interaction=nonstopmode cv.tex > /dev/null 2>&1
    cp cv.pdf ../../docs/Resume.pdf
    cd ../..
else
    # Build moderncv template
    cd cv_template-main/src/cv/lang/en/
    pdflatex -interaction=nonstopmode cv.tex > /dev/null 2>&1
    pdflatex -interaction=nonstopmode cv.tex > /dev/null 2>&1
    cp cv.pdf ../../../../../docs/Resume.pdf
    cd ../../../../..
fi

echo ""
echo "✅ Build complete!"
echo "   📄 docs/Resume.pdf"
echo "   🌐 docs/index.md"
echo ""
echo "Next: git add . && git commit -m 'Update CV' && git push"
