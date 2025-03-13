FROM python:3.10-slim AS base
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . /
RUN mkdir -p logs credentials
EXPOSE 8501
USER root
RUN apt-get update && apt-get install -y --no-install-recommends \
      build-essential \
      curl && rm -rf /var/lib/apt/lists/
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV DEBIAN_FRONTEND noninteractive
ENV UID 1001
ENV GID 1001
USER 1001
CMD [\"streamlit\", \"run\", \"app/main.py\", \"--server.address\", \"0.0.0.0\"]