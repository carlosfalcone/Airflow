from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {'owner': 'falcone'}

with DAG(
    dag_id = 'executing_multiple_tasks',
    description = 'DAG with multiple tasks and dependencies',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = '@once'
) as dag:

    task_A = BashOperator(
        task_id = 'task_A',
        bash_command = 'echo Task A has executed!'
    )

    task_B = BashOperator(
        task_id = 'task_B',
        bash_command = 'echo Task B has executed!'
    )

# task_A.set_downstream(task_B)
task_A.set_upstream(task_B)
