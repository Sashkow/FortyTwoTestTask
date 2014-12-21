42-test template
===========================
###Install Instructions 

* git clone https://github.com/Sashkow/FortyTwoTestTask.git
* cd FortyTwoTestTask
* virtualenv --no-site-packages .env
* source .env/bin/activate
* .env/bin/pip install -r requirements.txt
* **./manage.py migrate**
* python manage.py syncdb --no-input



A Django 1.6+ project template

Use fortytwo_test_task.settings when deploying with getbarista.com

### Recomendations
* apps in apps/ folder
* use per-app templates folders
* use per-app static folders
* use migrations
* use settings.local for different environments
* common templates live in templates/
* common static lives in assets/
* management commands should be proxied to single word make commands, e.g make test

