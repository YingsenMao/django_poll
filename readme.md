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
```
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```
To call the view, we need to mapt it to a URL. Create a file called **urls.py**, and include the following code:
```
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
```