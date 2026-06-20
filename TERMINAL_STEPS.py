# cd Docker_demo (To open the Docker_demo folder inside the main DOCKER_DEMO folder)

#--------Commands to run on terminal ,after cloning the repository------------
# docker ps -a
# docker run -it ubuntu 
# docker run -it python:slim

# python -V  (To know the version of python)

#---------Open the python_demo folder --------
# cd python_demo
# py demo.py (TO run python file)

# --------Making and image and run it---------
# docker build -t demo-app . (To make the image)
# docker run demo-app
# docker ps -a 

# ========To close the current folder python_demo and open pandas_demo folder and make its image and run it========= 
# cd..
# cd pandas_demo
# py app.py

# docker build -t pandas-app .
# docker run pandas-app 
# docker ps -a

#========Now for spark_demo folder=========
# cd..
# cd spark_demo
# docker build -t spark-demo-app .
# docker run -it --rm -p 8080:8080 -v "$(pwd):/workspace" spark-demo-app
# {Copy the url from the terminal and open it in the browser to see the spark demo app,jupyter notebook will open in the browser}

#=========Now for kafka-basic folder============
# cd..
# cd kafka-basic
# docker compose up --build

# docker compose down {i have not run this}

# -------------------------------------------
#{OPEN New terminal while not closing the previous,and run the below commands}

# docker exec -it kafka bash
# {NOW make a topic and run it }

#/opt/kafka/bin/kafka-topics.sh \
# --create \
# --topic demo-topic \
# --bootstrap-server localhost:9092

# /opt/kafka/bin/kafka-topics.sh \
# --list \
# --bootstrap-server localhost:9092

#=========Now for airflow-basic folder============
#{Airflow Password for user 'admin': CGcqzBZx5sRqur75}

# cd docker_demo
# cd airflow-basic
# docker compose up --build
# docker compose up -d
# docker ps

# docker exec -it airflow-webserver airflow version
# docker exec -it airflow airflow dags list
# [if error aa jaye]
# docker exec -it airflow airflow dags list-import-errors
# docker exec -it airflow airflow dags list

# {iske baad bhi airflow ke dags me customer_onboarding nhi aaye to run these commands:-}
# docker exec -it airflow ls -la /opt/airflow/dags
# docker exec -it airflow python -c "import sys; sys.path.append('/opt/airflow/dags'); import customer_pipeline; print(customer_pipeline.dag)"
# docker exec -it airflow airflow dags reserialize
# docker exec -it airflow airflow dags list

# [customer_onboarding aa jane ke baad use trigger krna h usse hii output me file banegiii]

# {Some extra commands which should be run in bash,i.e.,VS Code → Terminal (Using Now ) → New Terminal}:-
# docker exec -it airflow bash
# ls -la /workspaces/docker-demo/airflow-basic/dags
# sudo chown -R codespace:codespace /workspaces/docker-demo/airflow-basic
# touch /workspaces/docker-demo/airflow-basic/dags/test.py (Creates an empty "test.py" file.)