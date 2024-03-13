FROM python:3.11.2-slim-buster

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY actions_example actions_example
ENTRYPOINT ["python3", "actions_example/main.py"]
