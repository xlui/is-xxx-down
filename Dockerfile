FROM python:3.9-slim
ADD . /data
WORKDIR /data
RUN pip install -r requirements.txt
ENTRYPOINT ["gunicorn", "app:app", "-c", "gunicorn.conf.py"]
