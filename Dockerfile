FROM python:3.9.7

RUN pip install --no-cache-dir -r requirements.txt

WORKDIR /home/andrii/PycharmProjects/SH_app(v1.0)/SH_app_v1_0

COPY . /home/andrii/PycharmProjects/SH_app(v1.0)/SH_app_v1_0

CMD ['python', 'manage.py', 'runserver 9000']

EXPOSE 5432