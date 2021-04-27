## CLONE AMAZON USING DJANGO

#### 0. Links to source on Github and Youtube

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

#### 10. Creating AdminUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 11. Creating StaffUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 12. Creating MerchantUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 13. Creating CustomerUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 14. Creating Categories model 

        modified:   README.md
        modified:   app/main/models.py

#### 15. Creating SubCategories model and add OneToMany relationship with Categories model

        modified:   README.md
        modified:   app/main/models.py

#### 16. Creating Products model and add OneToMany relationship with SubCategories and MerchantUser models

        modified:   README.md
        modified:   app/main/models.py

#### 17. Creating ProductMedia model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 18. Creating ProductTransaction model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 19. Creating ProductDetails model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 20. Creating ProductAbout model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 21. Creating ProductTags model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 22. Creating ProductQuestions model and add OneToMany relationship with Products and CustomerUser models

        modified:   README.md
        modified:   app/main/models.py

#### 23. Creating ProductReviews model and add OneToMany relationship with Products and CustomerUser models

        modified:   README.md
        modified:   app/main/models.py

#### 24. Creating ProductReviewVoting model and add OneToMany relationship with ProductReviews and CustomerUser models

        modified:   README.md
        modified:   app/main/models.py

#### 25. Creating ProductVarient model

        modified:   README.md
        modified:   app/main/models.py

#### 26. Creating ProductVarientItems model and add OneToMany relationship with ProductVarient and Products models

        modified:   README.md
        modified:   app/main/models.py

#### 27. Creating CustomerOrders model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 28. Creating OrderDeliveryStatus model and add OneToMany relationship with CustomerOrders model

        modified:   README.md
        modified:   app/main/models.py

#### 29. Creating OrderDeliveryStatus model and add OneToMany relationship with CustomerOrders model

        modified:   README.md
        modified:   app/main/models.py

#### 30. Creating create_user_profile model

        modified:   README.md
        modified:   app/main/models.py

#### 31. Creating save_user_profile model

        modified:   README.md
        modified:   app/main/models.py

#### 32. Modified README.md file

        modified:   README.md

#### 33. Register Categories and SubCategories models to admin

        modified:   README.md
        modified:   app/main/admin.py

#### 34. Correction of a typo in ProductTransaction model

        modified:   README.md
        modified:   app/main/models.py

#### 35. Checking the project

        (venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src> python manage.py check
        SystemCheckError: System check identified some issues:

        ERRORS:
        ...
        System check identified 4 issues (0 silenced).

        > There are 4 issues found
        > NEXT: fixing the errors

        modified:   README.md
        modified:   app/main/__pycache__/models.cpython-39.pyc
        modified:   app/main/models.py

#### 36. Fixing the errors

        > add: AUTH_USER_MODEL to settings.py
        > error fixed
        (venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src> python manage.py check
        System check identified no issues (0 silenced).

#### 37. Create database and superuser

        > python manage.py makemigrations
        > python manage.py py migrate
        > python manage.py createsuperuser
        modified:   README.md
        new file:   app/main/migrations/0001_initial.py
        modified:   db.sqlite3

#### 38. Modified README.md

#### 39. Modified README.md


## TEMPLATING

#### 40. Adding static and media files root and url

        modified:   README.md
        modified:   config/settings.py

#### 41. Using Urls, Views, Templates to render Home and About pages

        modified:   README.md
        new file:   app/main/urls.py
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        ...
        new file:   static/assets/...
        new file:   templates/main/about.html
        new file:   templates/main/index.html

#### 42. Create 'dashboard' app and install it to root project and move templates to project root

        modified:   README.md
        new file:   app/dashboard/__init__.py
        new file:   app/dashboard/admin.py
        new file:   app/dashboard/apps.py
        new file:   app/dashboard/models.py
        new file:   app/dashboard/tests.py
        new file:   app/dashboard/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   templates/main/index.html

#### 43. Adding login page

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        new file:   templates/dashboard/login.html
        modified:   templates/main/about.html
        modified:   templates/main/index.html

#### 44. Modified login page

        modified:   README.md
        new file:   static/assets/img/LOGO.JPG
        new file:   static/assets/img/vaficon.ico
        modified:   templates/dashboard/login.html























































































































































































































