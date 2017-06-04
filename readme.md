## Set Up New Environment
cd to the target environment and type `virtualenv poll_project`.  
It will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages.  
Activate the virtual environment by using `poll_project\Scripts\activate`, and deactivate by using `deactivate`.  

## Part 1
Check the django version by `python -m django --version`.  
#### Create a project 
```django-admin startproject mysite``` creates a project.  
```python manage.py startapp polls``` creates a application.  
#### Create a view and call the view using url
```python
#polls/views.py
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
To call the view, we need to map it to a URL. 
```python
#polls/urls.py
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```
The next step is to reference the application urls in the project urls.
```python
#mysite/urls.py
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^polls/', include('polls.urls')),
    url(r'^admin/', admin.site.urls),
]
```
Note the regular expressions for the **include()** functiond doesn't have a **$**(end-of-string match character) but rather a trailing slash. Whenever Django encounters **include()**, it chops off whatever part of the URL matched up to that point and sends the remaining string to the included URLconf for further processing.

## Part 2
#### Database Setup
The **DATABASES** in the **mysite/setting.py** defines the database.  
* **ENGINE**: database type.Eg. 'django.db.backends.postgresql'.
* **NAME**: The name of your database. If you're using SQLite, it will be the full absolute path, including the filename.
If you are not using SQLite as your database, the following additional settings must be added.
* **USER**
* **PASSWORD**
* **HOST** 
Below is an example connecting poll database in local postgresql server by using postgres users.
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'poll',
        'USER': 'postgres',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
For more detials, see [DATABASES](https://docs.djangoproject.com/en/1.11/ref/settings/#std:setting-DATABASES)
#### Add Applications
The **INSTALLED_APPS** in the **mysite/setting.py** holds all the activated Django applications in this Django instance. To include the app created in our project, its configuration class needs to be added in the **INSTALLED_APPS** setting.  
The **PollsConfig** class is in the **polls/apps.py** file, so its dotted path is **'polls.apps.PollsConfig'**. It'll look like this:
```python
#mysite/settings.py
INSTALLED_APPS = [
    'polls.apps.PollsConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

Some of these applications make use of at least one database table, so you need to create the tables in the database before you can use them. To do this, run command: ```python manage.py migrate```.  
#### Create and Activate Models
A model is the single, definitive source of information about your data. It contains the essential fields and behaviors of the data you're storing. 
* Each model is a Python class that subclasses **django.db.models.Model**.
* Each attribute of the model represnets a database field.
* With all of this, Django gives you an automatically-generated database-access API.
Below is an example creating two models.
```python
#polls/models.py
from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    #return a clear description of object in database API
    def __str__(self):
        return self.question_text
    def was_published_recently(sef):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
        
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    #return a clear description of object in database API
    def __str__(self):
        return self.choice_text
```
Before activating the models just created, the application that contains the models (polls in this case) has to be added into **INSTALLED_APPS**. (described in **Add Application** section)  
  
Command ```python manage.py makemigrations polls``` tells Django that you've made some changes to your models.  
Command ```python manage.py sqlmigrate polls 0001``` returns SQLs.  
Command ```python manage.py migrate``` takes all migrations and synchronizing the changes you made to your models with the schema in the database.  
The **migrate** command looks at the INSTALLED_APPS setting and creates any necessary database tables according to the database settings in your **mysite/settings.py** file and the **database migrations** shipped with the app.
