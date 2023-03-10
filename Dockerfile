FROM python:3.8
RUN mkdir /app 

COPY test_koek/ /app/test_koek
COPY pyproject.toml /app 
COPY README.md /app 

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD} 
RUN pip3 install poetry
RUN poetry config virtualenvs.create false

RUN poetry install --only main