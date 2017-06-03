### Set Up New Environment
cd to the target environment and type `virtualenv poll_project`.  
It will create a folder in the current directory which will contain the Python executable files, and a copy of the pip library which you can use to install other packages.  
Activate the virtual environment by using `poll_project\Scripts\activate`, and deactivate by using `deactivate`.  

### Part 1
Check the django version by `python -m django --version`.  
Create a project called mysite by `django-admin startproject mysite`.  
Create a app called polls by `python manage.py startapp polls`. 