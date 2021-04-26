## CLONE AMAZON USING DJANGO

### 0. Links to source on Github and Youtube

	https://github.com/gurnitha/django-amazon-clone
	https://www.youtube.com/channel/UCyz5M_3Rv2jLUDs4R_yRBkw

#### 1. Initial setup

        new file:   .gitignore
        new file:   README.md

#### 2. Create virtual environment

        $ python -m venv venv3932
        modified:   README.md

#### 3. Install Django  

        $ source ./venv3932/scripts/activate
        (venv3932)
        62812@DESKTOP-CMH9JMD MINGW64 /e/2021/DJANGO/WINDOWS/clone-amazon-ytb-supercoders (master)
        $ python -m pip install django==3.2.*
        $ python -m pip install django==3.2.*
        modified:   README.md

#### 4. Create Django project 'config' inside src folder

        $ django-admin startproject config .
        modified:   README.md
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   db.sqlite3
        new file:   manage.py

#### 5. Create Django app 'main' inside app folder

        modified:   README.md
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py

#### 6. Install django app 'main' to the project

        modified:   README.md
        modified:   app/main/apps.py
        modified:   config/settings.py

#### 7. Checking the product structure

		(venv3932)
		62812@DESKTOP-CMH9JMD MINGW64 /e/2021/DJANGO/WINDOWS/clone-amazon-ytb-supercoders/src (main)
		$ cmd //c tree //F
		Folder PATH listing
		Volume serial number is DC72-8D6C
		E:.
		▒   .gitignore
		▒   db.sqlite3
		▒   manage.py
		▒   README.md
		▒
		▒▒▒▒app
		▒   ▒▒▒▒main
		▒       ▒   admin.py
		▒       ▒   apps.py
		▒       ▒   models.py
		▒       ▒   tests.py
		▒       ▒   views.py
		▒       ▒   __init__.py
		▒       ▒
		▒       ▒▒▒▒migrations
		▒       ▒   ▒   __init__.py
		▒       ▒   ▒
		▒       ▒   ▒▒▒▒__pycache__
		▒       ▒           __init__.cpython-39.pyc
		▒       ▒
		▒       ▒▒▒▒__pycache__
		▒               admin.cpython-39.pyc
		▒               apps.cpython-39.pyc
		▒               models.cpython-39.pyc
		▒               __init__.cpython-39.pyc
		▒
		▒▒▒▒config
		    ▒   asgi.py
		    ▒   settings.py
		    ▒   urls.py
		    ▒   wsgi.py
		    ▒   __init__.py
		    ▒
		    ▒▒▒▒__pycache__
		            settings.cpython-39.pyc
		            urls.cpython-39.pyc
		            wsgi.cpython-39.pyc
		            __init__.cpython-39.pyc

        modified:   README.md

#### 8. Modified README.md file 

		> Adding links to sources: Github and Youtube
        modified:   README.md

#### 9. Creating CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 10. Creating AdminUser model and OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 11. Creating StaffUser model and OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

















































































































































































































































































