## CLONE AMAZON USING DJANGO


## 0. SOURCES

#### 0.1.1 Links to source on Github and Youtube

	https://github.com/gurnitha/django-amazon-clone
	https://www.youtube.com/channel/UCyz5M_3Rv2jLUDs4R_yRBkw

## 1. INITIAL SETUP

#### 1.1.1. Initial setup

        new file:   .gitignore
        new file:   README.md

#### 1.2.2. Create virtual environment

        $ python -m venv venv3932
        modified:   README.md

#### 1.3.3. Install Django  

        $ source ./venv3932/scripts/activate
        (venv3932)
        62812@DESKTOP-CMH9JMD MINGW64 /e/2021/DJANGO/WINDOWS/clone-amazon-ytb-supercoders (master)
        $ python -m pip install django==3.2.*
        $ python -m pip install django==3.2.*
        modified:   README.md

#### 1.4.4. Create Django project 'config' inside src folder

        $ django-admin startproject config .
        modified:   README.md
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   db.sqlite3
        new file:   manage.py

## 2. DJANGO PROJECT AND APPS

#### 2.1.5. Create Django app 'main' inside app folder

        modified:   README.md
        new file:   app/main/__init__.py
        new file:   app/main/admin.py
        new file:   app/main/apps.py
        new file:   app/main/migrations/__init__.py
        new file:   app/main/models.py
        new file:   app/main/tests.py
        new file:   app/main/views.py

#### 2.2.6. Install django app 'main' to the project

        modified:   README.md
        modified:   app/main/apps.py
        modified:   config/settings.py

#### 2.3.7. Checking the product structure

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


## 3. MODELS

#### 3.1.8. Modified README.md file 

		> Adding links to sources: Github and Youtube
        modified:   README.md

#### 3.2.9. Creating CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 3.3.10. Creating AdminUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 3.4.11. Creating StaffUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 3.5.12. Creating MerchantUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 3.6.13. Creating CustomerUser model and add OneToOne relationship with CustomUser model

        modified:   README.md
        modified:   app/main/models.py

#### 3.7.14. Creating Categories model 

        modified:   README.md
        modified:   app/main/models.py

#### 3.8.15. Creating SubCategories model and add OneToMany relationship with Categories model

        modified:   README.md
        modified:   app/main/models.py

#### 3.10.16. Creating Products model and add OneToMany relationship with SubCategories and MerchantUser models

        modified:   README.md
        modified:   app/main/models.py

#### 3.11.17. Creating ProductMedia model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 3.12.18. Creating ProductTransaction model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 3.13.19. Creating ProductDetails model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 3.14.20. Creating ProductAbout model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 3.15.21. Creating ProductTags model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 3.16.22. Creating ProductQuestions model and add OneToMany relationship with Products and CustomerUser models

        modified:   README.md
        modified:   app/main/models.py

#### 3.17.23. Creating ProductReviews model and add OneToMany relationship with Products and CustomerUser models

        modified:   README.md
        modified:   app/main/models.py

#### 3.18.24. Creating ProductReviewVoting model and add OneToMany relationship with ProductReviews and CustomerUser models

        modified:   README.md
        modified:   app/main/models.py

#### 3.19.25. Creating ProductVarient model

        modified:   README.md
        modified:   app/main/models.py

#### 3.20.26. Creating ProductVarientItems model and add OneToMany relationship with ProductVarient and Products models

        modified:   README.md
        modified:   app/main/models.py

#### 3.21.27. Creating CustomerOrders model and add OneToMany relationship with Products model

        modified:   README.md
        modified:   app/main/models.py

#### 3.22.28. Creating OrderDeliveryStatus model and add OneToMany relationship with CustomerOrders model

        modified:   README.md
        modified:   app/main/models.py

#### 3.23.29. Creating OrderDeliveryStatus model and add OneToMany relationship with CustomerOrders model

        modified:   README.md
        modified:   app/main/models.py

#### 3.24.30. Creating create_user_profile model

        modified:   README.md
        modified:   app/main/models.py

#### 3.25.31. Creating save_user_profile model

        modified:   README.md
        modified:   app/main/models.py

#### 3.26.32. Modified README.md file

        modified:   README.md

#### 3.27.33. Register Categories and SubCategories models to admin

        modified:   README.md
        modified:   app/main/admin.py

#### 3.28.34. Correction of a typo in ProductTransaction model

        modified:   README.md
        modified:   app/main/models.py

#### 3.29.35. Checking the project

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

#### 3.30.36. Fixing the errors

        > add: AUTH_USER_MODEL to settings.py
        > error fixed
        (venv3932) PS E:\2021\DJANGO\WINDOWS\clone-amazon-ytb-supercoders\src> python manage.py check
        System check identified no issues (0 silenced).

## 4. DATABASE

#### 4.1.37. Create database and superuser

        > python manage.py makemigrations
        > python manage.py py migrate
        > python manage.py createsuperuser
        modified:   README.md
        new file:   app/main/migrations/0001_initial.py
        modified:   db.sqlite3

## HOUSE KEEPING

#### 5.1.38. Modified README.md

#### 5.2.39. Modified README.md

## 5 TEMPLATING

#### 5.1.40. Adding static and media files root and url

        modified:   README.md
        modified:   config/settings.py

#### 5.2.41. Using Urls, Views, Templates to render Home and About pages

        modified:   README.md
        new file:   app/main/urls.py
        modified:   app/main/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        ...
        new file:   static/assets/...
        new file:   templates/main/about.html
        new file:   templates/main/index.html

#### 5.2.42. Create 'dashboard' app and install it to root project and move templates to project root

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

## 6. LOGIN

#### 6.1.43. Adding login page

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        new file:   templates/dashboard/login.html
        modified:   templates/main/about.html
        modified:   templates/main/index.html

#### 6.2.44. Modified login page

        modified:   README.md
        new file:   static/assets/img/LOGO.JPG
        new file:   static/assets/img/vaficon.ico
        modified:   templates/dashboard/login.html

#### 6.3.45. Adding Admin home page

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        modified:   static/assets/img/LOGO.JPG
        new file:   templates/dashboard/base.html
        new file:   templates/dashboard/home.html
        new file:   templates/dashboard/shared/navbar.html
        new file:   templates/dashboard/shared/sidebar.html

#### 6.4.46.1 Login - Login process with {% csrf_token %} added

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        modified:   templates/dashboard/login.html
        new file:   templates/dashboard/login_process.html

#### 6.5.46.2 Login - Authenticate user login

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        modified:   db.sqlite3
        modified:   templates/dashboard/login.html
        modified:   templates/main/about.html
        modified:   templates/main/index.html

#### 6.6.46.3 Login - Displaying logged in username on navabar

        modified:   README.md
        modified:   db.sqlite3
        modified:   templates/dashboard/shared/navbar.html 

## 7. LOGOUT

#### 7.1.47. Logout - Create logout method and add success message 

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        modified:   db.sqlite3
        modified:   templates/dashboard/login.html
        modified:   templates/dashboard/shared/navbar.html
        modified:   templates/dashboard/shared/sidebar.html

## 8. USERS ACCESS

#### 8.1.48. Limiting the access to admin dashboard, only logged in user can access it

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   db.sqlite3

## HOUSE KEEPING AND CHANGING LOGO

        modified:   README.md
        new file:   static/assets/img/head-title-logo.png
        new file:   static/assets/img/logo-new.png
        new file:   static/assets/img/vaficon-new.ico
        modified:   templates/dashboard/login.html

## 9. ADMIN PAGES

#### 9.1.49 Create Category List Page

        modified:   README.md
        modified:   app/dashboard/views.py
        modified:   config/urls.py
        new file:   templates/dashboard/category_list.html
        modified:   templates/dashboard/home.html

#### 9.1.50 Moving content of main/models.py to dashboard/models.py

        modified:   README.md
        modified:   app/dashboard/admin.py
        renamed:    app/main/migrations/0001_initial.py -> app/dashboard/migrations/0001_initial.py
        modified:   app/dashboard/models.py
        modified:   app/dashboard/views.py
        modified:   app/main/admin.py
        modified:   app/main/models.py
        modified:   config/settings.py
        modified:   db.sqlite3
        new file:   mdeia/Acer_C27.jpg


























































































































































































