FROM python:3

WORKDIR /app

RUN pip install requests

RUN pip install beautifulsoup4

CMD [ "python", "./app.py" ]
# CMD [ "bash" ]
