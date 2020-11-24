FROM python:3

COPY . /api

WORKDIR /api

RUN pip install -r requirementes.txt

EXPOSE 5000

CMD [ "python", "app.py" ]