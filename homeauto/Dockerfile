FROM python:3.8



RUN pip install --upgrade pip 
COPY ./requirements.txt . 
RUN pip3 install -r requirements.txt

COPY . /homeauto

WORKDIR ./homeauto
