# expenses-app
It is a web-app which keeps a track of all the expenses. All you need to do is add the expense. Rest will be done for you!!

### Installation (python 2.7)

- Get the requirements

`$ sudo apt-get install python-pip`

  
- Fork and clone the expenses-app repository

	`$ git clone https://github.com/<Username>/expenses_app`

- Now get the django specific requirements 
 	
	`$ cd expenses_app`
  
  	`$ pip install django`

- Now run the server 
 	
	`$ python manage.py runserver`

open [127.0.0.1:8000](127.0.0.1:8000) in the browser


- Apply the migrations

	`python manage.py makemigrations`

	`python manage.py migrate`

- Create the admin

	`python manage.py createsuperuser`

- Add the relevant information

- open [127.0.0.1:8000/admin](127.0.0.1:8000/admin)
