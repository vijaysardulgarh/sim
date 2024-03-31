
Create Virtual env

    cd ~/project_folder_name
    Syntax:- virtualenv env_name
    Example:- virtualenv venv
  
Activate Virtual env

    Syntax:- source virtualenv_name/bin/activate
    Example:- source venv/bin/activate

Install Dependencies

    pip install -r requirements.txt
  
Install Gunicorn

    pip install gunicorn
  
Deactivate Virtualenv

    deactivate


Create System Socket File for Gunicorn

Syntax:- sudo nano /etc/systemd/system/your_domain.gunicorn.socket

Example:- 

    sudo nano /etc/systemd/system/sim.com.gunicorn.socket
    

Write below code inside sim.com.gunicorn.socket File

    Syntax:- 
    [Unit]
    Description=your_domain.gunicorn socket
    
    [Socket]
    ListenStream=/run/your_domain.gunicorn.sock
    
    [Install]
    WantedBy=sockets.target

Example:- 

        [Unit]
        Description=sim.com.gunicorn socket
        
        [Socket]
        ListenStream=/run/sim.com.gunicorn.sock
        
        [Install]
        WantedBy=sockets.target

Create System Service File for Gunicorn

Syntax:- sudo nano /etc/systemd/system/your_domain.gunicorn.service

Example:- 

    sudo nano /etc/systemd/system/sim.com.gunicorn.service

Write below code inside sim.com.gunicorn.service File
Syntax:-
[Unit]
Description=your_domain.gunicorn daemon
Requires=your_domain.gunicorn.socket
After=network.target

[Service]
User=username
Group=groupname
WorkingDirectory=/home/username/project_folder_name
ExecStart=/home/username/project_folder_name/virtual_env_name/bin/gunicorn \
          --access-logfile - \
          --workers 3 \
          --bind unix:/run/your_domain.gunicorn.sock \
          inner_project_folder_name.wsgi:application

[Install]
WantedBy=multi-user.target

Example:-

    [Unit]
    Description=sonamkumari.com.gunicorn daemon
    Requires=sonamkumari.com.gunicorn.socket
    After=network.target
    
    [Service]
    User=raj
    Group=raj
    WorkingDirectory=/home/raj/miniblog
    ExecStart=/home/raj/miniblog/mb/bin/gunicorn \
              --access-logfile - \
              --workers 3 \
              --bind unix:/run/sonamkumari.com.gunicorn.sock \
              miniblog.wsgi:application
    
    [Install]
    WantedBy=multi-user.target

Start Gunicorn Socket and Service

Syntax:- sudo systemctl start your_domain.gunicorn.socket
Example:- sudo systemctl start sim.com.gunicorn.socket

Syntax:- sudo systemctl start your_domain.gunicorn.service
Example:- sudo systemctl start sim.com.gunicorn.service
Enable Gunicorn Socket and Service
Syntax:- sudo systemctl enable your_domain.gunicorn.socket
Example:- sudo systemctl enable sim.com.gunicorn.socket

Syntax:- sudo systemctl enable your_domain.gunicorn.service
Example:- sudo systemctl enable sonamkumari.com.gunicorn.service
Check Gunicorn Status
sudo systemctl status sonamkumari.com.gunicorn.socket
sudo systemctl status sonamkumari.com.gunicorn.service
Restart Gunicorn (You may need to restart everytime you make change in your project code)
sudo systemctl daemon-reload
sudo systemctl restart sonamkumari.com.gunicorn
