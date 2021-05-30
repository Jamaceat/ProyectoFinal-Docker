FROM python:3
RUN apt-get update -y && apt-get install -y build-essential
ENV PYTHONUNBUFFERED 1
WORKDIR /code
COPY /code/ /code/
RUN pip install pandas
RUN pip install dash
RUN pip install psycopg2-binary