mkdir app
python3 -m venv .venv


[Unit]
Description=flask app
After=network.target

[Service]
User=ec2-user
Group=ec2-user
WorkingDirectory=/home/ec2-user/app/
Environment="PATH=/home/ec2-user/app/venv/bin"
ExecStart=/home/ec2-user/app/venv/bin/python3 /home/ec2-user/app/app.py

[Install]
WantedBy=multi-user.target


sudo vi flaskapp.service
sudo systemctl daemon-reload
sudo systemctl enable flaskapp.service
sudo systemctl start flaskapp.service