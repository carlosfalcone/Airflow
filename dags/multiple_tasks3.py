from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {'owner': 'falcone'}

with DAG(
    dag_id = 'executing_multiple_tasks3',
    description = 'DAG with multiple tasks and dependencies',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = timedelta(days=1),
    tags = ['scripts', 'template search'],
    template_searchpath = '/home/carlosfalcone/airflow/dags/bash_scripts'
) as dag:

    task_A = BashOperator(
        task_id = 'task_A',
        bash_command = 'task_A.sh'
    )

    task_B = BashOperator(
        task_id = 'task_B',
        bash_command = 'task_B.sh'
    )

    task_C = BashOperator(
        task_id = 'task_C',
        bash_command = 'task_C.sh'
    )

    task_D = BashOperator(
        task_id = 'task_D',
        bash_command = 'task_D.sh'
    )

    task_E = BashOperator(
        task_id = 'task_E',
        bash_command = 'task_E.sh'
    )

    task_F = BashOperator(
        task_id = 'task_F',
        bash_command = 'task_F.sh'
    )

    task_G = BashOperator(
        task_id = 'task_G',
        bash_command = 'task_G.sh'
    )


task_A >> task_B >> task_E
task_A >> task_C >> task_F
task_A >> task_D >> task_G