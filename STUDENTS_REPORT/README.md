# my-django-projects

# TO DEPLOY THIS PROJECT IN YOUR LOCAL SYSTEM FOLLOW THE BELOW STEPS

## title--students academic report

### 1) Installing pip
 * $ sudo apt-get update
 * $ sudo apt-get upgrade
 * $ sudo apt-get install python-pip

### 2)Create virtual environment for your project
 * $ sudo apt install virtualenv
 * $ virtualenv env(your environment name)

### 3) Activating  your environment
 * $ source env/bin/activate

### 4)Installing mysql server and mysql client
 * $ sudo apt-get install python-dev libmysql-client-dev mysql-server
 (as a part of instalation it will ask password for mysql server and 'root' is default username)

### 5) Installing git and cloning repositery from github
 * $ sudo apt-get install git
 * $ git clone https://github.com/ganeshsingamaneni/my-django-projects.git

### 6)Change the directory
 * $ cd my-django-projects
  (my-django-projects is the repositery name)

### 7)Installing the requirements.txt
 * $ pip install -r requirements.txt
  (in requirements.txt file there are some packages which are needed for our django application)

### 8)Create a database in mysql server
 * $ mysql -u root-p.
  after giving the password
 * $ create database "database name";
  (database name should be of your own,"" in not necessary)
 * $ show databases;
 * $ use 'databasename";
 * $ exit;

### 9) Opening the project files and change necessary fields
 (go to settings.py to change the  name in databases,give the name of your database and change the password )

### 10) migrating models
 * $ python manage.py makemigrations
 * $ python manage.py migrate
  (now you will see the list of migrations happened)

### 11)Checking tables in our databses
 * $ mysql -u root -p
 * $ show databses;
 * $ use database;
 * $ show tables;
 
 (you can see your tables there)

### 12) Sending data to our tables
 (first change the datbase name,mysql user name and password in db.py file and also change the path of studentsmarks.csv,subjects.csv in   db.py file)
 after changing the changes in db.py file go to db.py file and run the script
 * $ cd DETAILS
 * $ python db.py
 (after running db.py file come out of DETAILS by command 'cd..')
 
### 13) Check the data in tables in mysql server 
 
 * $ mysql -u root -p
 * $ show databses;
 * $ use database;
 * $ show tables; 
 * $ select *from (tablename)
  
  (you can see the data in mysql tables)


### 14) Creating super user
 * $ python manage.py createsuperuser
 
  (give name password and mail)

### 15) running the server
 * $ python manage.py runserver
 
 
 (you will see a link in the terminal open that link)
 (you can check any url in the urls.py in browser and also check the admin page)


