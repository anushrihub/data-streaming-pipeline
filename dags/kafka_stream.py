# import the libraries
from _datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator #type: ignore

# default arguments passed to every task in the DAG.
# 'owner' is a label; 'start_date' tells Airflow when to start scheduling.

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2026, 7, 7, 10, 00)
}


def stream_data():
    import json
    import requests

    # fetch a random user profile from the public API
    res = requests.get("https://randomuser.me/api/")
    print(res.json())

# define the dag
with DAG('user_automation',
        default_args= default_args,
        schedule= '@daily',
        catchup= False) as dag:

    # define a task that calls stream_data() when the DAG runs
    streaming_task = PythonOperator(
        task_id = 'stream_data_from_api',
        python_callable= stream_data
    )

# temporary manual test call — remove this before deploying to Airflow
stream_data();