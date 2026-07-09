#!/usr/bin/env bash
set -e

if [ -e "/opt/airflow/requirements.txt" ]; then
    pip install -r /opt/airflow/requirements.txt
fi

airflow db upgrade

airflow users create \
    --username admin \
    --firstname admin \
    --lastname admin \
    --role Admin \
    --email admin@example.com \
    --password admin

airflow webserver
