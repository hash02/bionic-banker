#!/bin/bash
set -e

echo "Site validation: checking built output..."

if [ -f "index.html" ]; then
  echo "index.html OK"
else
  echo "index.html MISSING"
  exit 1
fi

if [ -f "intelligence/index.html" ]; then
  echo "intelligence/index.html OK"
else
  echo "intelligence/index.html MISSING"
  exit 1
fi

echo "Site validation passed."
