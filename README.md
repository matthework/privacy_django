# privacy_django

command  

$ mkdir django_app  

$ cd django_app  

$ virtualenv venv  

$ venv\Scripts\activate  

$ pip install --upgrade pip  

$ pip install django  

$ django-admin.py startproject mysite .  

$ python manage.py migrate  

$ python manage.py runserver  

$ python manage.py startapp privacy  

$ python manage.py makemigrations privacy  

$ python manage.py migrate privacy  

$ python manage.py createsuperuser  

$ heroku login  

$ heroku apps  

$ heroku run --app privacy-django python manage.py migrate  

$ heroku run --app privacy-django python manage.py createsuperuser  