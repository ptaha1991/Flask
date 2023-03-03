FROM python:3.9.1-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 5010

CMD ["python3", "wsgi.py"]