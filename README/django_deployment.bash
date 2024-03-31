#!/bin/bash

# Variables
PROJECT_NAME="your_project_name"
DOMAIN="your_domain.com"
USER="your_username"
PROJECT_DIR="/home/$USER/$PROJECT_NAME"
NGINX_CONFIG_DIR="/etc/nginx/sites-available"
NGINX_SITES_ENABLED_DIR="/etc/nginx/sites-enabled"
SOCKET_FILE="/run/$PROJECT_NAME.sock"
NGINX_SOCKET_FILE="/etc/systemd/system/$PROJECT_NAME.gunicorn.socket"
NGINX_SERVICE_FILE="/etc/systemd/system/$PROJECT_NAME.gunicorn.service"
NGINX_LOG_DIR="/var/log/nginx"
GUNICORN_BIN="$PROJECT_DIR/venv/bin/gunicorn"
GUNICORN_WSGI="your_project.wsgi:application"  # Replace with your project's WSGI module

# Create project directory
mkdir -p $PROJECT_DIR

# Clone or copy your Django project to the project directory
# git clone <repository_url> $PROJECT_DIR
# Or copy your project files to $PROJECT_DIR

# Create virtual environment
python3 -m venv $PROJECT_DIR/venv

# Activate virtual environment
source $PROJECT_DIR/venv/bin/activate

# Install dependencies
pip install -r $PROJECT_DIR/requirements.txt

# Install Gunicorn
pip install gunicorn

# Deactivate virtual environment
deactivate

# Create Nginx socket file
cat << EOF | sudo tee $NGINX_SOCKET_FILE
[Unit]
Description=$PROJECT_NAME Gunicorn socket

[Socket]
ListenStream=$SOCKET_FILE

[Install]
WantedBy=sockets.target
EOF

# Create Nginx service file
cat << EOF | sudo tee $NGINX_SERVICE_FILE
[Unit]
Description=$PROJECT_NAME Gunicorn daemon
Requires=$PROJECT_NAME.gunicorn.socket
After=network.target

[Service]
User=$USER
Group=$USER
WorkingDirectory=$PROJECT_DIR
ExecStart=$GUNICORN_BIN --access-logfile - --workers 3 --bind unix:$SOCKET_FILE $GUNICORN_WSGI

[Install]
WantedBy=multi-user.target
EOF

# Enable and start Gunicorn socket and service
sudo systemctl enable $PROJECT_NAME.gunicorn.socket
sudo systemctl enable $PROJECT_NAME.gunicorn.service
sudo systemctl start $PROJECT_NAME.gunicorn.socket
sudo systemctl start $PROJECT_NAME.gunicorn.service

# Create Nginx configuration file
cat << EOF | sudo tee $NGINX_CONFIG_DIR/$DOMAIN
server {
    listen 80;
    listen [::]:80;
    server_name $DOMAIN www.$DOMAIN;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        proxy_set_header Host \$http_host;
        proxy_set_header X-Real-IP \$remote_addr;
        proxy_set_header X-Forwarded-For \$proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto \$scheme;
        proxy_pass http://unix:$SOCKET_FILE;
    }

    location /static/ {
        alias $PROJECT_DIR/static/;
    }

    location /media/ {
        alias $PROJECT_DIR/media/;
    }
}
EOF

# Enable Nginx site
sudo ln -s $NGINX_CONFIG_DIR/$DOMAIN $NGINX_SITES_ENABLED_DIR/$DOMAIN

# Test Nginx configuration
sudo nginx -t

# Restart Nginx
sudo systemctl restart nginx

echo "Deployment completed successfully!"
