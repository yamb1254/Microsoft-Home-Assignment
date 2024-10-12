FROM python:3.9-slim

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir requests

EXPOSE 80

CMD ["python", "app.py"]