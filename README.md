
# Studify - Learning Management System

A student-faculty oriented learning management system 
based in Django framework.

The prototype provides students a bunch of tools to stay engaged with 
their studies,peer and broader univeristy community during pandemic

This prototype takes care of the requirements of three major stakeholders
### Admin : 
- Responsible for adding and updating details of students and faculty members.
- Acts as a moderator between conversations of faculty members and students.
- Takes care of leaves requested by students and faculty.
- Adds the courses and the corresponding subjects along with their respective session year.

### Faculty:
- Enters the marks of corresponding students enrolled in thier course.
- Updates the attendance of students.
- Can provide feedback to admin.
- Can ask the admin to notify the enrolled students of details concerning the subject being taught.
- Can request for leaves.

### Students :
- Views the marks entered by the faculty member.
- Can provide feedback to admin
- Can ask the admin to notify the enrolled students of details concerning the subject being taught.
- Can request for leaves.



## Features

- **Online Forum with admin moderation.**
- **Admin Dashbboard managing students, faculty, courses, subjects, session years**
- **Feedback System**
- **Security Middleware that prevents SQL injection**


## Check out the deployed webapp here

https://studify2021.herokuapp.com
## Installation Steps on Local Machine

1. **Clone project from Github**
Clone the project from the url - https://github.com/akshatshukla175/studify-webapp.
Open the project in any IDE. Make sure you open your terminal with the project directory. It should look something like :
>> 
    C:\....\....\studify-webapp

2. **Install Python**
Download python from https://www.python.org/downloads/

3. **Install Virtual environment**
Install virtual environment using the command 
>>
    pip install virtualenv

4. **Create virtual environment**
Create virtual environment using the command
>>
    virtualenv django_env

Here django_env is the name of the virtual environment created

5. **Activate the virtual environemnt**
Activate virtual environment using the command
>>
    django_env/Scripts/activate

6. **Install requirements and dependenices**
Install requirements and dependenices with the help of requirements.txt.
>>
    pip install -r requirements.txt

7. **Run on local host**
Start your machine using the command
>>
    python manage.py runserver
## Prerequisites and Dependencies

>>
    asgiref==3.4.1
    dj-config-url==0.1.1
    dj-database-url==0.5.0
    Django==3.2.9
    gunicorn==20.1.0
    psycopg2==2.9.2
    pytz==2021.3
    sqlparse==0.4.2
    whitenoise==5.3.0
    requests==2.26.0
## Database Design

![design](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/dd.png)
## Screenshots

![1](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/1.png)
![2](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/2.png)
![3](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/3.png)
![4](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/4.png)
![5](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/5.png)
![6](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/6.png)
![7](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/7.png)
![8](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/8.png)
![9](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/9.png)
![10](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/10.png)
![11](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/11.png)
![12](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/12.png)
![13](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/13.png)
![14](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/14.png)
![15](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/15.png)
![16](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/16.png)
![17](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/17.png)
![18](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/18.png)
![19](https://github.com/akshatshukla175/studify-webapp/blob/main/demo/19.png)

## Demo

Insert gif or link to demo


## Authors

- [@akshatshukla](https://github.com/akshatshukla175)

