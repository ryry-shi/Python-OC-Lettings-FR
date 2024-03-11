FROM python:3.12.2
# setup environment variable 
# where your code lives  
WORKDIR /app  

# set environment variables  
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1  

# install dependencies  
RUN pip install --upgrade pip  

# copy whole project to your docker home directory. 
COPY . /app
# run this command to install all dependencies  
RUN pip install -r requirements.txt  
# port where the Django app runs  