#simple_hello_world.py
from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {'owner': 'falcone'}

dag = DAG(
    dag_id = 'hello_world',
    description = 'Our first "hello world" DAG!',
    default_args = default_args,
    start_date = days_ago(1),
    # schedule_interval = None
    schedule_interval = '@daily',
    tags = ['beginner', 'bash', 'hello world']
)

task = BashOperator(
    task_id = 'hello_world_task',
    # bash_command = 'echo Hello World',
    bash_command = 'echo Hello World once again!',
    dag = dag
)

task
