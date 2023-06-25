#!/bin/sh

until cd /app/digitalsys_loan
do
    echo "Loading server volume..."
done

celery -A digitalsys_loan worker --loglevel=info --concurrency 1 -E -Q proposal_analysis
