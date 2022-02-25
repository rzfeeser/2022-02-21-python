# select a starting image
# it is assumed you want to download from hub.docker.com
# FROM hub.docker.com/python:alpine3.7
FROM python:alpine3.7

# copy our code and requirements.txt into the /app dir within the image
COPY . /app

# relative to the image we are within the /app dir
WORKDIR /app 

# within the image, run this command (within the /app dir)
RUN pip install -r requirements.txt

# expose a port (firewall hole)
# EXPOSE 5000

# You get a single CMD to kick off your container
CMD python ./micro.py
