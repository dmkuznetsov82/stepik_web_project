sudo rm /etc/nginx/sites-enabled/default

sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart

sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/hello.py
sudo /etc/init.d/gunicorn restart
#gunicorn -с /etc/gunicorn.d/hello.py hello

sudo /etc/init.d/mysql start
