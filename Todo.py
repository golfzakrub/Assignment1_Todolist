import json
from tkcalendar import Calendar
import tkinter  as tk
from User import User

class Todo:

    def __init__(self):
        self.user= User()
        
    def add_todo(self,login,list_todo, user):
        data = user.getTasksUser()
        data["user"][login].append(list_todo)
        user.editTasksUser()


    def add_mark(self,login,index,user):
        datamark = user.getTasksUser()
        if datamark["user"][login][index][2] == "1":
            datamark["user"][login][index][2] = "0"
        else :
            datamark["user"][login][index][2] = "1"
        user.editTasksUser()    
        
    def remove_todo(self,login,remove_index,user):
        data = user.getTasksUser()
        print(data["user"][login][remove_index])
        data["user"][login].remove(data["user"][login][remove_index])
        user.editTasksUser()


    # def removeall_todo(self,login,remove_index):
    #     data = self.user.getTasksUser()
    #     print(data["user"][login])
    #     data["user"][login].clear()
    #     self.user.editTasksUser()
    # data["user"][login].clear()

