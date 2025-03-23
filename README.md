1. First install python software
2. Create "djangoapps" within the c-drive & intall django within it (Don't install django in the original python folder)
3. Install virtual environment **c:\users\hp\djangoapps> pip3 install virtualenv myenv**
4. Activate virtual environment **c:\users\hp\djangoapps\myenv\Scripts>.\activate** (If any error then change terminal as command prompt)
5. Create django-admin start project **c:\users\hp\djangoapps>django-admin startproject myproject1**
6. Create or start an application **c:\users\hp\djangoapps\myproject1>python manage.py startapp DemoApp**
7. Add your application name to installed-apps withing setting.py
8. Go to urls.py and define urls for your project
9. Go to views.py and defin input() function
10. Migrate your project to check if any errors **c:\users\hp\djangoapps\myproject1>python manage.py migrate**
11. Run servers **c:\users\hp\djangoapps\myproject1>python manage.py runserver**
12. Giving request in the browser **http://127.0.0.1:8080/demo**
