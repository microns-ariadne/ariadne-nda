#!/bin/sh
set -e

UWSGI_PORT=${UWSGI_PORT:-80}
UWSGI_THREADS=${UWSGI_THREADS:-$(grep -c processor /proc/cpuinfo)}

uwsgi \
  --master \
  --thunder-lock \
  --threads ${UWSGI_THREADS} \
  --single-interpreter \
  --http ":${UWSGI_PORT}" \
  --mount "/=ariadne_nda.wsgi:app"
