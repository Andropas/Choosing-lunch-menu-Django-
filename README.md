CHOOSING LUNCH MENU

How to SetUp system:

#1 SetUp database

Change all properties to your configuration in settings.py file

#You should change these values
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'postgres',
        'PASSWORD': '1234',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


#2 Create admin in system

Open command prompt in the root of project directory, then enter there:
...> python manage.py createsuperuser
    Username: <your_username>
    Email address: <youremail@addres.com>
    Password: <your password>
    Password (again): <your password>


#3 Run application server

In command prompt enter:
...> python manage.py runserver

Now, open a web browser and go to http://127.0.0.1:8000/admin/

Log in Django administration


#4 Now you can use functionality of system

Create restaurants, menus, employees. You can both edit and delete them

Good luck!
Enjoy coding :D
