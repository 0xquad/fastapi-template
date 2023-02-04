# Basic Dockerfile to run a FastAPI server
FROM python:3-alpine
RUN pip install -qU pip && pip install -q fastapi uvicorn
RUN adduser -DH app
COPY ./app /app
WORKDIR /app
USER app
# Binding to "" will listen on both on ipv4 and ipv6
CMD uvicorn main:app --reload --host ""
