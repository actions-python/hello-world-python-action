FROM docker.io/library/python:3.11-alpine
ENV PATH /app:$PATH
COPY requirements.txt /app/requirements.txt
RUN pip install --disable-pip-version-check --no-cache-dir -r /app/requirements.txt
COPY main.py /app/main.py
ENTRYPOINT ["main.py"]
