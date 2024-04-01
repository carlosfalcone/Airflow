from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {'owner': 'falcone'}

with DAG(
    dag_id = 'hello_world_mod',
    description = 'Our first "hello world" DAG!',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@daily'
) as dag:

    task = BashOperator(
        task_id = 'hello_world_task_mod',
        bash_command = 'echo Hello - created a DAG using "with"!'
    )

task
