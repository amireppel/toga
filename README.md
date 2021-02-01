# toga Project By Amir Eppel

this is a project simulates a behaviour of a file system using Python-Django Webserver and ORM, i used simple sqlite database in this project, so the database itself is already the repository and there should be no nedd for extra installation beyond what is written below

# requirements 

Python 3.69 or newer versions, i used this version in Python3 virtual environment on Linux Ubuntu 18.04

# Installation and starting the app

git clone 

git clone git@github.com:amireppel/toga.git

cd toga

pip install -r req.txt

cd cd DirProject

python manage.py migarte

python manage.py runserver

# Application api and use

once the Django server is running you should be able to use the following API's:

http://localhost:8000/api/showFileSystem :
in this api you should see the structure of the file system, containing files, directories and subdirectories. initiali the file system is empty.

http://localhost:8000/api/addDir:
in this api , you can add new directories to the file system, the first directory added will be the root directory. you can also add the  parent directory name in order to insert the directory as a sub directory of an existing directory, if parent directory name is not provided, the directory will be added as a subdirectory of the parent directory.

http://localhost:8000/api/addFile:
in this api , you can add new files to the file system, similarly to the addDir api, if parentDir is not specified, the file will be add to the root directory

http://localhost:8000/api/deleteDir
in this api you can delete directories from the file system

http://localhost:8000/api/deleteFile
in this api you can delete files from the file system

command line addition of the first directory(if the filesytem  is empty) could be done by running the following comand from toga/DirProject: 
python manage.py createRootDir <First-Dir-Name>

# Short description of the code

django database models for file and directory are found toga/DirProject/api/models.py 

django views that handles the different api requests and interactig with the models are in toga/DirProject/api/views.py

json seriliazires for the django models are found in toga/DirProject/api/urls.py


