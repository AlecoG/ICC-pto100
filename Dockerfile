FROM python:3.12.4-alpine3.20


# Crear el grupo www-data si no existe, y luego crear el usuario www-data si no existe
RUN getent group www-data || addgroup -S www-data && \
    getent passwd www-data || adduser -S -G www-data www-data

WORKDIR /usr/src/app
ENV PYTHONPATH=/usr/src/app


COPY requirements.txt ./

RUN apk add --no-cache libc-dev gcc

RUN pip install -r requirements.txt

COPY . .


# Create a Gunicorn configuration file
RUN mkdir -p /etc/gunicorn
RUN touch /etc/gunicorn/gunicorn.conf.py
RUN echo "bind = '0.0.0.0:7000'" > /etc/gunicorn/gunicorn.conf.py
RUN echo "workers = 5" >> /etc/gunicorn/gunicorn.conf.py
RUN echo "user = 'www-data'" >> /etc/gunicorn/gunicorn.conf.py
RUN echo "group = 'www-data'" >> /etc/gunicorn/gunicorn.conf.py
#RUN echo "keyfile = '/etc/ssl/private/server.key'" >> /etc/gunicorn/gunicorn.conf.py
#RUN echo "certfile = '/etc/ssl/certs/server.pem'" >> /etc/gunicorn/gunicorn.conf.py

#RUN rm db.sqlite3

#COPY nginx/certs/server.key /etc/ssl/private/server.key
#COPY nginx/certs/server.pem /etc/ssl/certs/server.pem

#EXPOSE 8080
EXPOSE 7000


CMD ["gunicorn", "--config", "/etc/gunicorn/gunicorn.conf.py", "Icc.wsgi:application"]

