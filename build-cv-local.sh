#!/bin/bash
# Local CV Build Script
# This script builds your CV locally and copies it to the website root

set -e  # Exit on error

echo "🔧 Building CV locally..."
echo ""

# Navigate to CV template directory
cd cv_template-main

# Start Docker container
echo "📦 Starting Docker container..."
docker-compose up -d --force-recreate

# Wait for PDF generation
echo "⏳ Waiting for PDF generation..."
cv_counter=0
max_wait=60

while [[ $(find . -name "cv.pdf" | wc -l) -eq 0 && $cv_counter -le $max_wait ]]; do
    echo "   Waiting... ($cv_counter/$max_wait seconds)"
    ((cv_counter++))
    sleep 2
done

if [[ $cv_counter -ge $max_wait ]]; then
    echo "❌ Timeout while waiting for PDF generation."
    echo "   Check Docker logs:"
    docker-compose logs
    docker-compose down
    exit 1
fi

echo "✅ PDF generated successfully!"

# Find and copy the CV
CV_PDF=$(find . -name "cv.pdf" | grep "/en/cv.pdf" | head -n 1)

if [ -z "$CV_PDF" ]; then
    echo "❌ Error: CV PDF not found!"
    docker-compose down
    exit 1
fi

echo "📄 Found CV at: $CV_PDF"

# Copy to docs folder for website
cd ..
mkdir -p docs
cp "cv_template-main/$CV_PDF" ./docs/Resume.pdf

echo "✅ CV copied to docs/Resume.pdf"
ls -lh docs/Resume.pdf

# Cleanup
echo "🧹 Cleaning up Docker..."
cd cv_template-main
docker-compose down

cd ..
echo ""
echo "🎉 Done! Your Resume.pdf has been updated."
echo "   You can now commit and push, or the GitHub Action will handle it automatically."
