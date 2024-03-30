This script automates the process of pulling updates from your GitHub repository to your server and then performs necessary actions like installing dependencies, collecting static files, applying migrations, and restarting the Gunicorn server and Nginx to apply the changes.

#!/bin/bash

# Navigate to the project directory
cd /path/to/your/project

# Activate the virtual environment if you're using one
source venv/bin/activate

# Pull changes from the GitHub repository
git pull origin master

# Install any new dependencies
pip install -r requirements.txt

# Collect static files if necessary
python manage.py collectstatic --noinput

# Apply migrations if necessary
python manage.py migrate

# Restart Gunicorn server
sudo systemctl restart gunicorn

# Restart Nginx to apply changes
sudo systemctl restart nginx
Replace /path/to/your/project with the actual path to your Django project directory.

Make the Script Executable:

Make the script executable by running:

bash
Copy code
chmod +x deploy.sh
Run the Script:

You can now run the script whenever you want to deploy new changes. Simply execute it from the terminal:

bash
Copy code
./deploy.sh
