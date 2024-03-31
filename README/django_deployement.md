
Create Virtual env

    virtualenv venv
  
Activate Virtual env

    source venv/bin/activate

Install Dependencies

    pip install -r requirements.txt
  
Install Gunicorn

    pip install gunicorn
  
Deactivate Virtualenv

    deactivate


Create System Socket File for Gunicorn

    sudo nano /etc/systemd/system/sim.com.gunicorn.socket
    

Write below code inside sim.com.gunicorn.socket File

        [Unit]
        Description=sim.com.gunicorn socket
        
        [Socket]
        ListenStream=/run/sim.com.gunicorn.sock
        
        [Install]
        WantedBy=sockets.target
        

Create System Service File for Gunicorn

    sudo nano /etc/systemd/system/sim.com.gunicorn.service
    

Write below code inside sim.com.gunicorn.service File

    [Unit]
    Description=sim.com.gunicorn daemon
    Requires=sim.com.gunicorn.socket
    After=network.target
    
    [Service]
    User=vijaysardulgarh
    Group=vijaysardulgarh
    WorkingDirectory=/home/vijasardulgarh/sim
    ExecStart=/home/raj/miniblog/mb/bin/gunicorn \
              --access-logfile - \
              --workers 3 \
              --bind unix:/run/sim.com.gunicorn.sock \
              sim.wsgi:application
    
    [Install]
    WantedBy=multi-user.target
    


Start Gunicorn Socket and Service

    sudo systemctl start sim.com.gunicorn.socket
    sudo systemctl start sim.com.gunicorn.service
    
Enable Gunicorn Socket and Service

    sudo systemctl enable sim.com.gunicorn.socket
    sudo systemctl enable sonamkumari.com.gunicorn.service

Check Gunicorn Socket and Service Status

    sudo systemctl status sim.com.gunicorn.socket
    sudo systemctl status sim.com.gunicorn.service
    
Restart Gunicorn (You may need to restart everytime you make change in your project code)

    sudo systemctl daemon-reload
    sudo systemctl restart sim.com.gunicorn


Configuring Nginx as a reverse proxy

Create Virtual Host File

    sudo nano /etc/nginx/sites-available/sim.com

Write following Code in Virtual Host File

    server{
        listen 80;
        listen [::]:80;
    
        server_name sim.com www.sim.com;
    
        location = /favicon.ico { access_log off; log_not_found off; }
    
        location / {
            proxy_set_header Host $http_host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_pass http://unix:/run/sim.com.gunicorn.sock;
        }
    
        location  /static/ {
            root /var/www/sim;
        }
    
        location  /media/ {
            root /var/www/miniblog;
        }
    }    


Enable Virtual Host or Create Symbolic Link of Virtual Host File

    sudo ln -s /etc/nginx/sites-available/sonamkumari.com /etc/nginx/sites-enabled/sonamkumari.com

Check Configuration is Correct or Not
    
    sudo nginx -t
    
Restart Nginx

    sudo service nginx restart
    
