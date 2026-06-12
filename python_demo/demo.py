#--------Commands to run on terminal ,after cloning the repository------------
# docker ps -a
# docker run -it ubuntu 
# docker run -it python:slim

# python -V  (To know the version of python)

print("Hello world")

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