# import the libraries
from _datetime import datetime
from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator

# default arguments passed to every task in the DAG.
# 'owner' is a label; 'start_date' tells Airflow when to start scheduling.

default_args = {
    'owner': 'airscholar',
    'start_date': datetime(2026, 7, 7, 10, 00)
}

# the API URL is hardcoded inside it
def get_data():
    import requests
    # fetch a random user profile from the public API
    # response present in the below variable
    res = requests.get("https://randomuser.me/api/")
    # convert into the python dictionary
    res = res.json()
    # drills into the data. res have the actual user data
    res = res['results'][0]

    return res

def format_data(res):
    data = {}
    location = res['location']
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['postcode'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data



def stream_data():
    import json

    res = get_data()
    res = format_data(res)
    print(json.dumps(res, indent = 3))
    

# define the dag
# with DAG('user_automation',
#         default_args= default_args,
#         schedule= '@daily',
#         catchup= False) as dag:

#     # define a task that calls stream_data() when the DAG runs
#     streaming_task = PythonOperator(
#         task_id = 'stream_data_from_api',
#         python_callable= stream_data
#     )

# temporary manual test call — remove this before deploying to Airflow


stream_data()