#!/bin/bash
# validate.sh — Validate info HTML files for 文化苦旅 chapters
# Usage: ./validate.sh <file.html>

set -e

FILE="$1"
if [ ! -f "$FILE" ]; then
  echo "❌ FILE NOT FOUND: $FILE"
  exit 1
fi

echo "=== Validating: $FILE ==="
errors=0

# Check CSS: FZXPYZS font first in body font-family
if grep -q "font-family: 'FZXPYZS'" "$FILE"; then
  echo "✅ FZXPYZS font declared"
else
  echo "❌ Missing FZXPYZS font"
  errors=$((errors+1))
fi

# Check body font-family has FZXPYZS first
if grep -q "font-family: 'FZXPYZS', 'PingFang SC'" "$FILE"; then
  echo "✅ Body font-family FZXPYZS first"
else
  echo "❌ Body font-family missing FZXPYZS as first"
  errors=$((errors+1))
fi

# Check container max-width:880px
if grep -q "max-width: 880px" "$FILE"; then
  echo "✅ Container max-width: 880px"
else
  echo "❌ Wrong container max-width"
  errors=$((errors+1))
fi

# Check body display:flex + justify-content:center
if grep -q "display: flex" "$FILE" && grep -q "justify-content: center" "$FILE"; then
  echo "✅ Body flex+center"
else
  echo "❌ Body missing flex+center"
  errors=$((errors+1))
fi

# Check #f5f1eb background
if grep -q "#f5f1eb" "$FILE"; then
  echo "✅ Background #f5f1eb"
else
  echo "❌ Missing #f5f1eb background"
  errors=$((errors+1))
fi

# Check h1 font-size:36px
if grep -q "font-size: 36px" "$FILE"; then
  echo "✅ h1 font-size: 36px"
else
  echo "❌ Wrong h1 font-size"
  errors=$((errors+1))
fi

# Check 5 sections with section-01~05
for i in 01 02 03 04 05; do
  if grep -q "section-${i}" "$FILE"; then
    echo "✅ section-${i} found"
  else
    echo "❌ Missing section-${i}"
    errors=$((errors+1))
  fi
done

# Check num-01~05
for i in 01 02 03 04 05; do
  if grep -q "num-${i}" "$FILE"; then
    echo "✅ num-${i} found"
  else
    echo "❌ Missing num-${i}"
    errors=$((errors+1))
  fi
done

# Check color classes (section borders match colors)
if grep -q "#dc2626" "$FILE" && grep -q "#ea580c" "$FILE" && grep -q "#ca8a04" "$FILE" && grep -q "#4f46e5" "$FILE" && grep -q "#db2777" "$FILE"; then
  echo "✅ All 5 section border colors present"
else
  echo "❌ Missing section border colors"
  errors=$((errors+1))
fi

# Check no section-header (old format)
if grep -q "section-header" "$FILE"; then
  echo "❌ Found old section-header (should be section-01~05)"
  errors=$((errors+1))
else
  echo "✅ No old section-header"
fi

# Check chapter-overview
if grep -q "chapter-overview" "$FILE"; then
  echo "✅ chapter-overview found"
else
  echo "❌ Missing chapter-overview"
  errors=$((errors+1))
fi

# Check takeaway
if grep -q "takeaway" "$FILE"; then
  echo "✅ takeaway found"
else
  echo "❌ Missing takeaway"
  errors=$((errors+1))
fi

# Check footer
if grep -q "footer" "$FILE"; then
  echo "✅ footer found"
else
  echo "❌ Missing footer"
  errors=$((errors+1))
fi

# Check back-catalog button
if grep -q "back-catalog-btn" "$FILE"; then
  echo "✅ back-catalog-btn found"
else
  echo "❌ Missing back-catalog-btn"
  errors=$((errors+1))
fi

# Check catalog link (supports both wenhua-kulv and fooled-by-randomness)
if grep -qE "([a-z-]+-catalog)\.html" "$FILE"; then
  echo "✅ Catalog link correct"
else
  echo "❌ Wrong catalog link"
  errors=$((errors+1))
fi

# Check lang-btn with target="_blank"
if grep -q 'target="_blank"' "$FILE"; then
  echo "✅ lang-btn has target=_blank"
else
  echo "❌ lang-btn missing target=_blank"
  errors=$((errors+1))
fi

# Check KPI
if grep -qi "kpi" "$FILE"; then
  echo "✅ KPI found"
else
  echo "⚠️ No KPI (optional)"
fi

# Check at least 2 visualization components
viz_count=0
if grep -q "flow-row" "$FILE"; then viz_count=$((viz_count+1)); fi
if grep -q "dual-grid" "$FILE"; then viz_count=$((viz_count+1)); fi
if grep -q "risk-bars" "$FILE"; then viz_count=$((viz_count+1)); fi
if grep -q "data-row" "$FILE"; then viz_count=$((viz_count+1)); fi
if [ "$viz_count" -ge 2 ]; then
  echo "✅ Visualization components: $viz_count (≥2)"
else
  echo "❌ Only $viz_count visualization components (<2)"
  errors=$((errors+1))
fi

echo ""
if [ "$errors" -eq 0 ]; then
  echo "🎉 ALL CHECKS PASSED"
else
  echo "❌ $errors ERRORS FOUND"
fi
echo ""
exit $errors
