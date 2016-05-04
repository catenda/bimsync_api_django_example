## Bimsync API example
This project demonstrates how to easily integrate the bimsync viewers in an external app using python and the django framework. 

Specify a projectId to one of your bimsync projects, and soon you should be able to view the project in the bimsync 2D and 3D viewers.

This is only a simple demonstration with a few methods, for a full list of methods see our APIs
[bimsync API](https://bimsync.com/developers/reference/api/1.0),
[Viewer 3D API](https://bimsync.com/developers/reference/viewer-3d/1.0),
[Viewer 2D API](https://bimsync.com/developers/reference/viewer-2d/beta),
[Viewer Widget API](https://bimsync.com/developers/reference/viewer-widget/1.0),
[BCF API](https://bimsync.com/developers/reference/bcf/beta)

### Requires Python 3.x
https://www.python.org/downloads/

## Getting started
Clone/download project

## Install Django:
```pip install Django```

if shell hangs you could try
```python -m pip install Django```

docs: 
https://docs.djangoproject.com/en/1.9/topics/install/#installing-official-release
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

## Init db for session handling:
Navigate to project root folder and run:
```python manage.py migrate```

## Replace credentials:
Open bimsync/views.py in an editor and change the app credentials there.
You find your app credentials here:
https://bimsync.com/account/integrations

If you do not yet own any apps, you are welcome to contact us
support@bimsync.com
And we will set ut a new app for you.

## Run server:
```python .\manage.py runserver```

## Web browser:
Open: 
http://localhost:8000/bimsync
