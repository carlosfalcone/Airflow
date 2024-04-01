from datetime import datetime, timedelta
from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.bash import BashOperator


default_args = {'owner': 'falcone'}

with DAG(
    dag_id = 'executing_multiple_tasks2',
    description = 'DAG with multiple tasks and dependencies',
    default_args = default_args,
    start_date = days_ago(1),
    schedule_interval = timedelta(days=1),
    tags = ['upstream', 'downstream']
) as dag:

    task_A = BashOperator(
        task_id = 'task_A',
        bash_command = '''
            echo Task A has started!
            for i in {1..10}
            do
                echo Task A printing $i
            done
            echo Task A has ended!
        '''
    )

    task_B = BashOperator(
        task_id = 'task_B',
        bash_command = '''
            echo Task B has started!
            sleep 4
            echo Task B has ended!
        '''
    )

    task_C = BashOperator(
        task_id = 'task_C',
        bash_command = '''
            echo Task C has started!
            sleep 3
            echo Task C has ended!
        '''
    )

    task_D = BashOperator(
        task_id = 'task_D',
        bash_command = 'echo Task D has completed!'
    )

# Commands #1
# task_A.set_downstream(task_B)
# task_A.set_downstream(task_C)
# task_D.set_upstream(task_B)
# task_D.set_upstream(task_C)

# Commands #2
# task_A >> task_B
# task_A >> task_C
# task_D << task_B
# task_D << task_C

# Commands #3
task_A >> [task_B, task_C]
task_D << [task_B, task_C]