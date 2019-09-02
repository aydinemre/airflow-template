# -*- coding: utf-8 -*-

# Created by emre.aydin (eaydin@boynergrup.com) at 2019-09-02
import airflow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.trigger_rule import TriggerRule

from src.code.person import main as print_person
from src.code.sleeper import main as sleep

default_args = {
    'owner': 'airflow',
    # 'retries': 1,
    # 'retry_delay': timedelta(seconds=10)
}

with DAG(dag_id='test_dag',
         default_args=default_args,
         description='Test Dag',
         schedule_interval='5 5 5 5 5',
         start_date=airflow.utils.dates.days_ago(1),
         catchup=False
         ) as dag:
    print_person_task = PythonOperator(
        python_callable=print_person,
        op_kwargs={'name': 'ARGE', 'age': 2},
        task_id='print_person_task',
        dag=dag)

    sleeper_task = PythonOperator(
        python_callable=sleep,
        op_kwargs={'sleep_time': 10},
        task_id='sleeper_task',
        dag=dag)

    print_person_task_2= PythonOperator(
        python_callable=print_person,
        op_kwargs={'name': 'ARGE', 'age': 2},
        task_id='print_person_task_2',
        dag=dag)

    print_person_task >> sleeper_task >> print_person_task_2