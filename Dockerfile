FROM python:3.7-slim-buster

RUN apt-get update &&\
    apt-get install -y python3-dev build-essential

# make app directory
RUN mkdir -p /usr/src/sceneclassifier

# change directory
WORKDIR /usr/src/sceneclassifier

# copy and install requirements
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# copy all files over
COPY . .

EXPOSE 8501

# streamlit specific commands for config
CMD streamlit run app.py
