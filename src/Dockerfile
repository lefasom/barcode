FROM ubuntu:18.04

RUN apt-get update -y
# Get's shared library for zbar
RUN apt-get install -y libzbar0
# Installs Python
RUN apt-get install -y python3-pip python3-dev build-essential

COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Initially encountered an issue that indicated I had to set these ENVs
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
