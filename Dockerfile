# set base image (host OS)
FROM python:3.8

RUN apt-get update
RUN pip3 install uwsgi

# set the working directory in the container
RUN mkdir -p /export/python_utils/current
WORKDIR /export/python_utils/current


# copy the dependencies file to the working directory
COPY requirements.txt .

# install dependencies
RUN pip3 install -r requirements.txt

# copy the content of the local src directory to the working directory
COPY . .

# command to run on container start
EXPOSE 9000
CMD [ "/usr/local/bin/uwsgi",  "--ini", "/export/python_utils/current/py-utils.ini"]
