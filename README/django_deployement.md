
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
