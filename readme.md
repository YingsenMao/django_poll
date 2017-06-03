## Set Up New Environment
cd to the target environment and type `virtualenv poll_project`.  
It will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages.  
Activate the virtual environment by using `poll_project\Scripts\activate`, and deactivate by using `deactivate`.  

## Part 1
Check the django version by `python -m django --version`.  
#### Create a project 
```
django-admin startproject mysite
```  
#### Create a app 
```
python manage.py startapp polls
```
#### Write your first view
Open the file **polls/views.py** and put the following code  
```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
To call the view, we need to mapt it to a URL. Create a file called **urls.py**, and include the following code:
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