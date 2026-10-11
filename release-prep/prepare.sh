#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
node release-prep/build.cjs
python3 release-prep/finalize.py
python3 release-prep/brand-pages.py
python3 brand-icons.py release-prep/candidate
python3 release-prep/vendor.py
node release-prep/test-lead.cjs
python3 release-prep/audit.py
python3 release-prep/seal.py
python3 release-prep/preview-branded-pages.py
printf '\nPrepared locally. Launch remains blocked; see release-prep/README.md. Nothing deployed.\n'
