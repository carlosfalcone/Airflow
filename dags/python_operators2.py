from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.python import PythonOperator
import time

default_args = {'owner': 'falcone'}

def task_a():
    print('Task A executed!')

def task_b():
    time.sleep(3)
    print('Task B executed!')

def task_c():
    print('Task C executed!')

def task_d():
    print('Task D executed!')

with DAG(
    dag_id = 'execute_python_operators2',
    description = 'Python operators in DAGs',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['dependencies', 'python'],
) as dag:

    task_a = PythonOperator(
        task_id = 'task_a',
        python_callable = task_a
    )

    task_b = PythonOperator(
        task_id = 'task_b',
        python_callable = task_b
    )

    task_c = PythonOperator(
        task_id = 'task_c',
        python_callable = task_c
    )

    task_d = PythonOperator(
        task_id = 'task_d',
        python_callable = task_d
    )

task_a >> [task_b, task_c]
[task_b, task_c] >> task_d