from importlib.resources import path
import json
from Todo import Todo
from User import User
from datetime import datetime
class Manager:
    
    def __init__(self):
        self.todo = Todo()
        self.user = User()

        

    def checkLogin(self, login, password):
        data_userid = self.user.getUser()
        
        if login in data_userid and data_userid[login] == password:  
            return True
        else:
            return False
    
    def newuser(self,login,password):
        if " " in login or login == "" or " " in password or password == "" :
            return 0
        else:
            data_userid = self.user.getUser()
            if login not in data_userid:
                data_userid[login] = password 
                self.user.editUser() 
                data = self.user.getTasksUser()                               
                data["user"][login] = []  
                self.user.editTasksUser()
                return True
            else:
                return False

    def data_receive(self,login):
        load = self.user.getTasksUser()
        return load

    def get_todo(self,login,list_todo):
        self.todo.add_todo(login,list_todo)
        return 1
    
    def sort_datetime(self,login):
        data_sort = self.user.getTasksUser()  
        data_sort["user"][login].sort( key=lambda a:datetime.strptime(a[1], "%d/%m/%y"))
        self.user.editTasksUser()


    def add_mark(self,login,index,user):
        self.todo.add_mark(login,index,user)




                    