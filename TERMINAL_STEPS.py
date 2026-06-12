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