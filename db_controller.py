
import sqlite3
from datetime import datetime
from create_new_db import db_config
import psycopg2




class DbController:
    """Allows user to update task and projects in database"""
    def __init__(self, db_name):
        self.db_name = db_name           

    def query(self, sql, data):
        con=psycopg2.connect(db_config)
        cursor = con.cursor()
        cursor.execute(sql, data)
        con.commit()

    def add_task(self,description, duedate, project_id,userid):
        created = datetime.now()
        sql_add_task = "INSERT INTO tasks (Description, duedate, Created, ProjectID,userid) VALUES (%s, %s, %s, %s,%s)"
        self.query(sql_add_task, (description, duedate, created, project_id,userid))


    def select_query(self,sql,data=None):
        con = psycopg2.connect(db_config)
        cursor = con.cursor()
        if data:
            cursor.execute(sql,data)
        else:
            cursor.execute(sql)
        results = cursor.fetchall()
        return results



    def add_project(self, description, deadline,userid):
        created = datetime.now()
        sql_add_project =  "INSERT INTO projects (Description, duedate, Created,userid) VALUES (%s, %s, %s,%s)"
        self.query(sql_add_project, (description, deadline, created,userid))

    def delete_task(self, task_id):
        self.query("DELETE FROM tasks WHERE taskid = %s", (task_id,))

    def delete_project_only(self, project_id):
        self.query("UPDATE tasks SET ProjectID = NULL WHERE ProjectID = %s", (project_id,))
        self.query("DELETE FROM Projects WHERE ProjectID = %s", (project_id,))

    def delete_project_and_tasks(self, project_id):
        self.query("DELETE FROM Tasks WHERE ProjectID = %s", (project_id,))
        self.query("DELETE FROM Projects WHERE ProjectID = %s", (project_id,))

    def mark_task_completed(self, task_id):
        completed = datetime.now()
        sql_mark_completed =  "UPDATE Tasks SET Completed = %s WHERE TaskID = %s"
        self.query(sql_mark_completed, (completed, task_id))

    def mark_project_completed(self, project_id):
        completed = datetime.now()
        sql_mark_completed =  "UPDATE Projects SET Completed = %s WHERE ProjectID = %s"
        self.query(sql_mark_completed, (completed, project_id))

    def mark_project_tasks_completed(self, project_id):
        completed = datetime.now()
        sql_mark_completed =  "UPDATE Tasks SET Completed = %s WHERE ProjectID = %s"
        self.query(sql_mark_completed, (completed, project_id))

    def get_task_project_id(self, task_id):
        sql_get_project_id = "SELECT ProjectID FROM Tasks WHERE TaskID = %s"
        results = self.select_query(sql_get_project_id, (task_id,))
        return results[0][0]

    def check_project_tasks_completed(self, project_id):
        sql_check_project = "SELECT taskid FROM Tasks WHERE ProjectID = %s AND Completed IS NULL"
        results = self.select_query(sql_check_project, (project_id,))
        if not results:
            return True
        return False
        
    def edit_task_description(self, task_id, description):
        sql_edit_descr = "UPDATE Tasks SET Description = %s WHERE TaskID = %s"
        self.query(sql_edit_descr, (description, task_id))

    def set_task_deadline(self, task_id, deadline):
        sql_set_deadline = "UPDATE Tasks SET duedate = %s WHERE TaskID = %s"
        self.query(sql_set_deadline, (deadline, task_id))

    def assign_task_to_project(self, task_id, project_id):
        sql_assign_task = "UPDATE Tasks SET ProjectID = %s WHERE TaskID = %s"
        self.query(sql_assign_task, (project_id, task_id))

    def set_project_deadline(self, project_id, deadline):
        sql_set_deadline = "UPDATE Projects SET duedate = %s WHERE ProjectID = %s"
        self.query(sql_set_deadline, (deadline, project_id))

    def edit_project_description(self, project_id, description):
        sql_edit_descr = "UPDATE Projects SET Description = %s WHERE ProjectID = %s"
        self.query(sql_edit_descr, (description, project_id))

    def get_all_tasks(self,user):
        results = self.select_query("SELECT * FROM Tasks where userid=%s ",(user,))
        return results

    def get_active_tasks(self,user):
        results = self.select_query("SELECT * FROM Tasks WHERE Completed IS NULL and userid=%s ",(user,))
        return results

    def get_completed_tasks(self,user):
        results = self.select_query("SELECT * FROM Tasks WHERE Completed IS NOT NULL and userid=%s ",(user,))
        return results

    def get_single_task(self, task_id,user):
        results = self.select_query("SELECT * FROM Tasks WHERE taskid = %s and userid=%s", (task_id,user))
        return results

    def get_all_projects(self,user):
        results = self.select_query("SELECT * FROM Projects WHERE userid = %s", (user,))
        return results

    def get_active_projects(self,user):
        results = self.select_query("SELECT * FROM Projects WHERE Completed IS NULL and userid=%s ",(user,))
        return results

    def get_completed_projects(self,user):
        results = self.select_query("SELECT * FROM Projects WHERE Completed IS NOT NULL and userid=%s ",(user,))
        return results
       
    def get_single_project(self, project_id,user):
        results = self.select_query("SELECT * FROM Projects WHERE ProjectID = %s and userid=%s", (project_id,user))
        return results

    def get_project_tasks(self, project_id,user):
        results = self.select_query("SELECT * FROM Tasks WHERE ProjectID = %s and userid=%s", (project_id,user))
        return results








