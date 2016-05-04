Clone/download project

Requires Python 3.x
https://www.python.org/downloads/

Install Django:
docs: https://docs.djangoproject.com/en/1.9/topics/install/#installing-official-release

pip install Django

if shell hangs you could try
python -m pip install Django

Init db for session handling:
Navigate to project root folder and run
python manage.py migrate


Replace credentials:
Open bimsync/views.py in an editor and change the app credentials there.
You find your app credentials here:
https://bimsync.com/account/integrations

If you do not yet own any apps, you are welcome to contact us
support@bimsync.com
And we will set ut a new app for you.


Run server:
python .\manage.py runserver


Web browser:
open 
http://localhost:8000/bimsync
