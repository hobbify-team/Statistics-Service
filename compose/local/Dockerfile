FROM python:3

COPY ./requirements /requirements
RUN pip install -r /requirements/local.txt
COPY . /app
WORKDIR /app
CMD python Hobbify-Stats/server.py
