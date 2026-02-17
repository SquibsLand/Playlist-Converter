#!/bin/bash

echo "$CRON_SCHEDULE /usr/local/bin/python /app/main.py $PY_ARGS" > /etc/cron.d/user-cron

chmod 0644 /etc/cron.d/user-cron

crontab /etc/cron.d/user-cron

cron -f