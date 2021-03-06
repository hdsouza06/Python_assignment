from PyQt5.QtWidgets import *
from PyQt5.QtGui import *

from create_new_db import *
from db_controller import *
from datetime import datetime


class TableWidget(QTableWidget):

    def __init__(self):
        super().__init__()
        self.controller = DbController("to_do.pgadmin")

        self.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.setSelectionBehavior(QTableView.SelectRows)
        self.setShowGrid(False)

    def show_items(self, item_list):
        if len(item_list) == 0:
            self.setRowCount(0)
        else:
            row = 0
            for entry in item_list:
                if entry[4] == None:
                    active = True
                else:
                    active = False
                self.setRowCount(row+1)
                column = 0
                for item in entry:
                    if item == None:
                        item = ""
                    elif column == 3 or column == 4:
                        item=datetime.strftime(item,'%Y-%m-%d')

                        # item = str(item[:-7])
                    table_item = QTableWidgetItem(str(item))
                    if column == 2 and item != "" and active:
                        if self.check_overdue(item):
                            table_item.setForeground(QColor(255,0,0))
                    self.setItem(row, column, table_item)
                    column += 1
                row += 1
        
    def check_completed(self):
        return self.item(self.currentRow(), 4).text() != ""

    def get_id(self):
        return int(self.item(self.currentRow(), 0).text())

    def check_overdue(self, deadline):
        deadline=str(deadline)
        deadline_date = datetime.strptime(deadline, '%Y-%m-%d')
        if deadline_date <= datetime.today():
            return True
        return False
        
class TasksTable(TableWidget):

    def __init__(self):
        super().__init__()

        self.setColumnCount(6)
        self.setHorizontalHeaderLabels(["Title", "Decription", "Duedate", "Created", "Completed", "CategoryID"])

    def get_tasks(self, task_type):
        global user
        con = psycopg2.connect(db_config)
        cursor = con.cursor()
        cursor.execute("""select * from users order by userid desc limit 1""")
        for row in cursor.fetchall():
            user, username, password, confirm_password = row
        if task_type == 0:
            tasks = self.controller.get_active_tasks(user)
        elif task_type == 1:
            tasks = self.controller.get_completed_tasks(user)
        else:
            tasks = self.controller.get_all_tasks(user)
        return tasks

    def get_task_project_id(self):
        return False

class ProjectTasksTable(TasksTable):

    def __init__(self, project_id):
        super().__init__()
        global user
        con = psycopg2.connect(db_config)
        cursor = con.cursor()
        cursor.execute("""select * from users order by userid desc limit 1""")
        for row in cursor.fetchall():
            user, username, password, confirm_password = row
        self.project_id = project_id


    def get_project_tasks(self,user):
        return self.controller.get_project_tasks(self.project_id,user)


class ProjectsTable(TableWidget):

    def __init__(self):
        super().__init__()
        
        self.setColumnCount(5)
        self.setHorizontalHeaderLabels(["CategoryID", "Decription", "Duedate", "Created", "Completed"])

    def get_projects(self, project_type):
        global user
        con = psycopg2.connect(db_config)
        cursor = con.cursor()
        cursor.execute("""select * from users order by userid desc limit 1""")
        for row in cursor.fetchall():
            user, username, password, confirm_password = row
        if project_type == 0:
            projects = self.controller.get_active_projects(user)
        elif project_type == 1:
            projects = self.controller.get_completed_projects(user)
        else:
            projects = self.controller.get_all_projects(user)
        return projects