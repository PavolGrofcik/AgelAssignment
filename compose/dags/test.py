from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from datetime import datetime

import os
import time

#################################################
# DAG Callables Definition
#################################################
def helloWorld():
    #os.chdir("/home/pavol")
    #with open("helloworld.txt", "w") as f:
     #   f.write("Hello World")
    time.sleep(10)
    print("Hello world!")

#################################################
# DAG Definition
#################################################
dag =  DAG(dag_id="hello_world_dag",
         start_date=datetime.now(),
         schedule=None,
         max_active_tasks=1,
         catchup=False,
         is_paused_upon_creation=False
        )

#Test task
task1 = PythonOperator(
    task_id="hello_world",
    python_callable=helloWorld,
    retries=0,
dag=dag)

#Test task
task2 = BashOperator(
    task_id="create_test_file",
    bash_command="touch $AGEL_DIR/bash_test_file.txt",
    retries=0,
    dag=dag
)

#######################
task1 >> task2


