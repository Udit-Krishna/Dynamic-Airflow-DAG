from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dynamic_dag_3",
    default_args={'owner': 'airflow owner 3', 'depends_on_past': False, 'start_date': '2024-06-01', 'email_on_failure': False, 'email_on_retry': False, 'retries': 3, 'retry_delay': 30},
    schedule_interval="0 * * * *"
) as dag:

    task_1=BashOperator(
                task_id="task_1",
                bash_command="echo 'This is task 1 of DAG 3'",
            )
    task_2=BashOperator(
                task_id="task_2",
                bash_command="echo 'This is task 2 of DAG 3'",
            )
    task_3=BashOperator(
                task_id="task_3",
                bash_command="echo 'This is task 3 of DAG 3'",
            )

    task_2.set_upstream(task_1)
    task_3.set_upstream(task_2)
