import json

class User:
    def __init__(self):
        self.data_userid = {}
        self.tasks_user = {}
        self.file_user = 'data_user.json'
        self.file_task = 'data_tasks.json'

    def getUser(self):
        with open(self.file_user,'r') as user_file:
            self.data_userid = json.load(user_file)
        return self.data_userid
    
    def editUser(self):
        with open(self.file_user, 'w') as user1_file:
            json.dump(self.data_userid, user1_file)
            print(self.tasks_user)
    
    def getTasksUser(self):
        with open(self.file_task, 'r') as data_file:
            self.tasks_user = json.load(data_file)
        return  self.tasks_user               

    def editTasksUser(self):
        with open(self.file_task, 'w') as data1_file: 
            json.dump(self.tasks_user, data1_file)
            print(self.tasks_user)
        
    def setFileUser(self, path):
        self.file_user = path

    def setFileTask(self, path):
        self.file_task = path
    
    def editMember(self,login):
        with open(self.file_user, 'w') as user3_file:  
            member = {login:self.data_userid[login]}
            json.dump(member, user3_file)
            
    def editdataMember(self,login):
        with open(self.file_task, 'w') as data3_file:  
            member = {login:self.tasks_user["user"][login]}
            dataMember = {"user":member}
            json.dump(dataMember, data3_file)
            