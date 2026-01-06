#!/bin/bash
set -e

echo "🔨 Building Programming Language Comparison Site"
echo ""

cd "$(dirname "$0")/builder"

echo "Step 1/4: Generating language landing pages..."
python generate_language_landing.py

echo ""
echo "Step 2/4: Generating static concept pages..."
python generate_static_pages.py

echo ""
echo "Step 3/4: Generating sitemap..."
python generate_sitemap.py

echo ""
echo "Step 4/4: Counting generated pages..."
cd ..
PAGE_COUNT=$(find docs/concepts -name '*.html' | wc -l)
SITEMAP_SIZE=$(du -h docs/sitemap.xml | cut -f1)

echo ""
echo "✅ Build complete!"
echo "   📄 Generated $PAGE_COUNT pages"
echo "   🗺️  Sitemap: docs/sitemap.xml ($SITEMAP_SIZE)"
echo ""
echo "Preview locally:"
echo "   cd docs && python -m http.server 8000"
echo "   Then visit: http://localhost:8000"
