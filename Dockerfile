FROM python:3.15.0a6-slim

ENV PYTHONUNBUFFERED=1
ENV CRON_SCHEDULE="0 0 * * *"
ENV PY_ARGS=""

RUN apt-get update && \
    apt-get install -y ffmpeg cron

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY src/ .

COPY start-cron.sh /usr/local/bin/start-cron.sh
RUN chmod +x /usr/local/bin/start-cron.sh

ENTRYPOINT [ "/usr/local/bin/start-cron.sh" ]