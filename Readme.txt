Install Django:
https://docs.djangoproject.com/en/1.9/topics/install/#installing-official-release

pip install Django

if shell hangs you could try

python -m pip install Django


Init db for session handling:
python manage.py migrate


Replace credentials:
Open views.py in an editor and change the app credentials there.
You find your app credentials here:
https://bimsync.com/account/integrations


Run server:
python .\manage.py runserver


Web browser:
open 
http://localhost:8000/bimsync
