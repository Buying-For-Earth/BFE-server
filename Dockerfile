FROM python:3

RUN mkdir myapp/

ADD . myapp/

WORKDIR /myapp/

RUN pip3 install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app/__init__.py

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]