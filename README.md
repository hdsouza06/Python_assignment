#ZERO TODO LIST APPLICATION

It is a Graphical User Interface tool to manage End to end tasks along 
with user authentication and also category folder to list 
out tasks 

It is built with Python 3.6 ,Postgres database and Pyqt5.

#Steps to install this application :
1) install PG ADMIN in your local and create a new Database 
2)Open a Python file named create_new_db.py ,goto line number 6 and then add the credentials of your newly
created Database and also username and password , It will look like this.

db_config = "dbname='Yourdbname' user='yourusername' password='yourpassword' host='localhost' port='5432'"

3)Once the DB Configuration is done , Run the python file  Ziro_todo_main.py ,when you run this,
3 tables will be created automatically to the DB that has been created and the application
goes to the login Screen .

4)Since you will be new user , First you need to click on create account and once the authentication is 
complete ,it will redirect you to the main task screen.

#Feautures that are present with ZIRO TODO LIST APP.

1)User authentication with the individual user accessing their own list 
2)User Can create a new todo list , update the current or any todo list ,Mark the todo list as
completed , Delete the current or any todo list , sort the tasks by any field ,also has a title and a description
3)The todolist also has a Due date which will track the list if it goes overdue
4)The to-Do list also have a folder named category to categorize it
5)In the Category folder where the user can assign task to any particular category,
user can view all the tasks in that category , mark the category has completed ,edit or delete the tasks in category,
edit or delete a category ,sort the category using different fields 
6)Please refer to giff file that is present where it contains the end to end implementation.