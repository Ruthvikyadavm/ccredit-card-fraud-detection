from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta

default_args = {
    'owner': 'ruthvik',
    'depends_on_past': False,
    'email_on_failure': False,
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'fraud_detection_pipeline',
    default_args=default_args,
    description='Run ETL and model training hourly',
    schedule_interval='@hourly',
    catchup=False
)

# Task 1: Run ETL
etl_task = BashOperator(
    task_id='run_etl',
    bash_command='python3 etl_pipeline.py',
    dag=dag
)

# Task 2: Run Model Training
model_task = BashOperator(
    task_id='run_model',
    bash_command='python3 model_training.py',
    dag=dag
)

etl_task >> model_task  # Set dependency
