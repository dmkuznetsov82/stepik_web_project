#!/bin/sh
#sudo ln -s etc/nginx.conf /etc/nginx/sites-enabled/test.conf

#gunicorn -c etc/hello.gunicorn.conf hello:wsgi_application
cd ask
gunicorn -c ../etc/ask_local.gunicorn.conf ask.wsgi:application

#sudo /etc/init.d/mysql start
