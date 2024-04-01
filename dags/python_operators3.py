from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.python import PythonOperator
import time

default_args = {'owner': 'falcone'}

def greet_hello(name):
    print('Hello, {name}!'.format(name=name))

def greet_hello_with_city(name, city):
    print('Hello, {name} from {city}'.format(name=name, city=city))


with DAG(
    dag_id = 'execute_python_operators3',
    description = 'Python operators in DAGs',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['parameters', 'python'],
) as dag:

    task_a = PythonOperator(
        task_id = 'greet_hello',
        python_callable = greet_hello,
        op_kwargs = {'name': 'Desmond'}
    )

    task_b = PythonOperator(
        task_id = 'greet_hello_with_cities',
        python_callable = greet_hello_with_city,
        op_kwargs = {'name': 'Louise', 'city': 'Seattle'}
    )

task_a >> task_b