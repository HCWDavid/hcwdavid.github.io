#!/bin/bash
# Quick workflow helper

echo "📝 What do you want to do?"
echo ""
echo "1. Generate content from JSON (LaTeX + Website)"
echo "2. Build CV PDF locally"  
echo "3. Generate + Build (full workflow)"
echo ""
read -p "Choice (1-3): " choice

case $choice in
  1)
    ./generate-all.sh
    ;;
  2)
    ./build-cv-local.sh
    ;;
  3)
    ./generate-all.sh && ./build-cv-local.sh
    echo ""
    echo "✅ Done! Check docs/Resume.pdf"
    ;;
  *)
    echo "Invalid choice"
    exit 1
    ;;
esac
