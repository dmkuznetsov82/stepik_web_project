sudo rm /etc/nginx/sites-enabled/default

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

#sudo ln -s /home/box/web/etc/hello.gunicorn.conf   /etc/gunicorn.d/hello.py
#sudo ln -s /home/box/web/etc/ask.gunicorn.conf   /etc/gunicorn.d/ask.py
#sudo /etc/init.d/gunicorn restart
gunicorn -c etc/hello.gunicorn.conf hello:wsgi_application

cd ask
gunicorn -c ../etc/ask_local.gunicorn.conf ask.wsgi:application

sudo /etc/init.d/mysql start
