all work and pip install (including django installation) should be in virtual environment

To create virtual environment:
py -m venv django-vir-env
This will create folder (django-vir-env)

To activate env:
D:\Projects\PythonQPickDjangoSearch> django-vir-env\Scripts\activate

Result in command:
(django-vir-env) D:\Projects\PythonQPickDjangoSearch>

Install django:
pip install django

To install django site(project)
django-admin startproject mysearchsite(name of the site)
This will create mysearchsite folder with root stuff

To create django app(modul,folder inside django main folder)
python manage.py startapp products
 

To run web server
(django-vir-env) D:\Projects\PythonQPickDjangoSearch\mysearchsite>py mysearchsite\manage.py runserver

To generate table creation, modification from models
py manage.py makemigrations products

#To apply changes from generate files to database to db.sqlite3
py manage.py migrate

To create requirenments text of any lib that you have install with pip,
activate environment then
pip freeze > requirenment.text
//will create and save inside requirenment.text

//you can install from requirenment
pip install -r requirenment.text
pip install django-taggit

