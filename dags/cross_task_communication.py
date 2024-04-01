from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.python import PythonOperator
import time

default_args = {'owner': 'falcone'}

def increment_by_1(counter):
    print('Count, {counter}!'.format(counter=counter))
    return counter + 1

def multiply_by_100(counter):
    print('Count, {counter}!'.format(counter=counter))
    return counter * 100

with DAG(
    dag_id = 'cross_task_communication',
    description = 'Cross-task communication with XCom',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily',
    tags = ['xcom', 'python'],
) as dag:

    task_a = PythonOperator(
        task_id = 'increment_by_1',
        python_callable = increment_by_1,
        op_kwargs = {'counter': 100}
    )

    task_b = PythonOperator(
        task_id = 'multiply_by_100',
        python_callable = multiply_by_100,
        op_kwargs = {'counter': 9}
    )

task_a >> task_b