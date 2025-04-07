

**This is a Tutorial Project for Content Management**

Deployment Proccess:

1. 
sudo apt update && sudo apt install python3 python3-venv python3-pip -y

2.
git clone https://github.com/yourusername/yourproject.git
cd yourproject

3.
python3 -m venv venv
source venv/bin/activate

4.
pip install -r requirements.txt

5.
ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

6.
python manage.py migrate

7.
sudo apt install gunicorn

8.
gunicorn --bind 127.0.0.1:8000 yourproject.wsgi

9.
sudo apt install nginx

10.
sudo nano /etc/nginx/sites-available/yourproject


    server {
        listen 80;
        server_name localhost;
    
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }


11.
sudo ln -s /etc/nginx/sites-available/yourproject /etc/nginx/sites-enabled
sudo nginx -t
sudo systemctl restart nginx

#Static file

1.
# settings.py
    
    import os
    from pathlib import Path
    
    BASE_DIR = Path(__file__).resolve().parent.parent
    
    
    STATIC_URL = '/static/'
    
    
    STATIC_ROOT = BASE_DIR / "staticfiles"
    
    
    STATICFILES_DIRS = [
        BASE_DIR / "static",
    ]
    
    
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR / "media"

2.
#urls.py
    from django.conf import settings
    from django.conf.urls.static import static
    
    if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

3.
python manage.py collectstatic

# Https for localhost

1.
sudo apt install libnss3-tools
curl -sSL https://github.com/FiloSottile/mkcert/releases/download/v1.4.4/mkcert-v1.4.4-linux-amd64 -o mkcert
chmod +x mkcert
sudo mv mkcert /usr/local/bin/

2.
mkcert -install  
mkcert localhost 127.0.0.1 ::1  (mkcert 192.168.1.100)

3. 
'''

     server{
        listen 443 ssl;
        server_name localhost;
    
        ssl_certificate /path/to/localhost.pem;
        ssl_certificate_key /path/to/localhost-key.pem;
    
        location / {
            proxy_pass http://127.0.0.1:8000;
            proxy_set_header Host $host;
        }
    }
    
    server {

        listen 80;
        server_name localhost;
        return 301 https://$host$request_uri;

    }
'''
4. 
sudo nginx -t && sudo systemctl restart nginx

5.
gunicorn yourproject.wsgi:application --bind 0.0.0.0:8000






