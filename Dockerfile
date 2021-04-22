FROM python:3

RUN mkdir myapp/

ADD . myapp/

WORKDIR /myapp/

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app/app.py"]