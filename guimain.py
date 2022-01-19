from pathlib import Path
from time import time
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, filedialog
import tkinter as tk
from tkinter import font as tkfont
from tkinter import *
import tkinter.messagebox 
from Manager import Manager
from tkcalendar import Calendar
import numpy as np
from matplotlib import pyplot as plt
import numpy as np



# LOGIN PAGE
class loginPage(tk.Frame):


    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def setName(self):
        if len(self.controller.user_file)>0 and len(self.controller.task_file) > 0:
            self.manager.user.setFileUser(self.controller.user_file)
            self.manager.user.setFileTask(self.controller.task_file)

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.login = ""
        self.manager = Manager()

        self.setName()




        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets")


        self.canvas = Canvas(
            self,
            bg = "#574B90", 
            height = 617,
            width = 484,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            242.0,
            308.0,
            image=self.image_image_1
        )
        #pageTwo
        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("registerPage"),
            relief="flat"
        )
        self.button_1.place(
            x=189.0,
            y=441.0,
            width=107.0,
            height=20.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.logincheck(self.entry_1,self.entry_2),
            relief="flat"
        )
        self.button_2.place(
            x=101.0,
            y=392.0,
            width=280.0,
            height=49.0
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            241.0,
            371.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(self,show= "*",
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=101.0,
            y=347.0,
            width=280.0,
            height=47.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            241.0,
            322.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=101.0,
            y=298.0,
            width=280.0,
            height=47.0
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            242.0,
            137.0,
            image=self.image_image_2
        )

        self.canvas.create_text(
            197.0,
            250.0,
            anchor="nw",
            text="SIGN IN",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )
    
    def logincheck(self,entry_1,entry_2):
        global login
        login = entry_2.get()
        password = entry_1.get()
        self.login = login
        check = self.manager.checkLogin(login, password)

        if check:
            self.controller.show_frame("notePage")  
        else:
            tk.messagebox.showinfo("ประกาศ","Wrong Username or password!!!")

 
# REGISTER PAGE
class registerPage(tk.Frame):
    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def setName(self):
        if len(self.controller.user_file)>0 and len(self.controller.task_file) > 0:
            self.manager.user.setFileUser(self.controller.user_file)
            self.manager.user.setFileTask(self.controller.task_file)

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.manager = Manager()
        
        self.setName()

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets3")
    


        self.canvas = Canvas(
            self,
            bg = "#574B90",
            height = 617,
            width = 484,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            238.0,
            308.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            191.0,
            58.0,
            anchor="nw",
            text="SIGN UP",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_user(self.entry_1,self.entry_2),
            relief="flat"
        )
        self.button_1.place(
            x=100.0,
            y=361.0,
            width=280.0,
            height=49.0
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            240.0,
            297.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(self,show = "*",
        
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
    
        self.entry_1.place(
            x=100.0,
            y=273.0,
            width=280.0,
            height=47.0
        )

        self.entry_image_2 = PhotoImage(
            file=self.relative_to_assets("entry_2.png"))
        self.entry_bg_2 = self.canvas.create_image(
            240.0,
            217.5,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_2.place(
            x=100.0,
            y=193.0,
            width=280.0,
            height=47.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("loginPage"),
            relief="flat"
        )
        self.button_2.place(
            x=212.0,
            y=449.0,
            width=60.0,
            height=61.0
        )
    def add_user(self,entry_1,entry_2):
        login = entry_2.get()
        password = entry_1.get()
        print(login)
        print(password)
        
        new = self.manager.newuser(login, password)
        if new is True:
            print("add success")
            tk.messagebox.showinfo("ประกาศ","Registration Success!!!")
            self.controller.show_frame("loginPage")
        elif new == 0:
            tk.messagebox.showinfo("ประกาศ","Can't use this!!!")
            
        else: 
            tk.messagebox.showinfo("ประกาศ","The username is already exists")
    

#notePAGE
class notePage(tk.Frame):
    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets4") 
        self.manager = Manager()
        self.setName()
        

        
        self.canvas = Canvas(
            self,
            bg = "#574B90",
            height = 617,
            width = 484,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            242.0,
            308.0,
            image=self.image_image_1
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.remove(login),
            relief="flat"
        )
        self.button_1.place(
            x=328.0,
            y=521.0,
            width=49.0,
            height=49.0
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.graph_pie,
            relief="flat"
        )
        self.button_2.place(
            x=319.0,
            y=44.0,
            width=24.0,
            height=24.0
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            242.0,
            290.0,
            image=self.image_image_2
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("loginPage"),
            relief="flat"
        )
        self.button_3.place(
            x=41.0,
            y=521.0,
            width=60.0,
            height=61.0
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            71.0,
            50.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            100.0,
            40.0,
            anchor="nw",
            text="TO DO LIST",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        self.button_image_4 = PhotoImage(
            file=self.relative_to_assets("button_4.png"))
        self.button_4 = Button(self,
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.import_file(login),
            relief="flat"
        )
        self.button_4.place(
            x=397.0,
            y=44.0,
            width=24.0,
            height=24.0
        )

        self.button_image_5 = PhotoImage(
            file=self.relative_to_assets("button_5.png"))
        self.button_5 = Button(self,
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:self.export_file(login),
            relief="flat"
        )
        self.button_5.place(
            x=436.0,
            y=44.0,
            width=24.0,
            height=24.0
        )

        self.button_image_6 = PhotoImage(
            file=self.relative_to_assets("button_6.png"))
        self.button_6 = Button(self,
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.mark(self.manager.user),
            relief="flat"
        )
        self.button_6.place(
            x=358.0,
            y=44.0,
            width=24.0,
            height=24.0
        )

        self.button_image_7 = PhotoImage(
            file=self.relative_to_assets("button_7.png"))
        self.button_7 = Button(self,
            image=self.button_image_7,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("taskCreatePage"),
            relief="flat"
        )
        self.button_7.place(
            x=416.0,
            y=521.0,
            width=49.0,
            height=49.0
        )

        self.button_image_8 = PhotoImage(
            file=self.relative_to_assets("button_8.png"))
        self.button_8 = Button(self,
            image=self.button_image_8,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.graph_bar(),
            relief="flat"
        )
        self.button_8.place(
            x=280.0,
            y=44.0,
            width=24.0,
            height=24.0
        )

        self.button_image_9 = PhotoImage(
            file=self.relative_to_assets("button_9.png"))
        self.button_9 = Button(self,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.graph_datebar(),
            relief="flat"
        )
        self.button_9.place(
            x=241.0,
            y=44.0,
            width=24.0,
            height=24.0
        )
                        
        self.listbox_tasks = tk.Listbox(self,height=11,width=26 ,bg="#F2F0FB",font=('Arial', 20))      
        self.listbox_tasks.place(x=45,y=90)

    def setName(self):
        if len(self.controller.user_file)>0 and len(self.controller.task_file) > 0:
            self.manager.user.setFileUser(self.controller.user_file)
            self.manager.user.setFileTask(self.controller.task_file)

    def import_file(self,login):
        user_file = filedialog.askopenfilename(filetype=[('Json file', '*.json')])
        if user_file:
            self.controller.user_file = user_file
            self.manager.user.setFileUser(user_file)
            self.manager.user.getUser()
        task_file = filedialog.askopenfilename(filetype=[('Json file', '*.json')])
        if task_file:
            self.controller.task_file = task_file
            self.manager.user.setFileTask(task_file)
            self.manager.user.getTasksUser()
        self.load_tasks(login)
        
    def export_file(self,login):
        user_file = filedialog.asksaveasfilename(filetype=[('Json file', '*.json')]) 
        self.manager.user.getUser()
        self.manager.user.getTasksUser()
        if user_file:
            self.manager.user.setFileUser(user_file+'.json')
            self.manager.user.editMember(login)
        task_file = user_file+'_task.json'
        if task_file:
            self.manager.user.setFileTask(task_file)
            self.manager.user.editdataMember(login)
        app.destroy()
        
    def load_tasks(self,login):
        self.listbox_tasks.delete(0, END)
        self.sort()          
        data_loaded = self.manager.data_receive(login)
        global done
        done = 0
        global undone
        undone = 0
        for task in data_loaded["user"][login]:
            if task[2] == "1":
                self.listbox_tasks.insert(END, task[0:2])
                self.listbox_tasks.itemconfig(END, bg='white',fg='green')
                done += 1
            elif task[2] == "0":
                self.listbox_tasks.insert(END, task[0:2])
                undone += 1
            else:
                self.listbox_tasks.insert(END, task[0:2])
            
        
            

    def mark(self,user):
        mark_index = self.listbox_tasks.curselection()[0]
        self.listbox_tasks.itemconfig(mark_index, bg='cyan',fg='green')
        self.manager.add_mark(login,mark_index,self.manager.user)
        self.load_tasks(login)


        
    def sort(self):
        self.manager.sort_datetime(login)

    def remove(self,login):
        remove_index = self.listbox_tasks.curselection()[0]
        self.manager.todo.remove_todo(login,remove_index,self.manager.user)
        self.load_tasks(login)

    def graph_pie(self): #different graph
        pie = [done,undone]
        calall = done+undone
        caldone = (done/calall)*100
        calundone = (undone/calall)*100
        labeldone = "Done "+ str("%.2f" %caldone) + "%"
        labelundone = "Undone " + str("%.2f" %calundone) + "%"
        Labels = [labeldone,labelundone]
        plt.pie(pie,labels=Labels,wedgeprops={'edgecolor':"red"})
        plt.title('Graph Done and Undone %')
        plt.show()


    def graph_bar(self): #Undone done graph
        plt.style.use("fivethirtyeight")
        le = ['Done','Undone']
        st = [done,undone]
        plt.bar(le, st)
        plt.title("All Done Tasks and Undone Tasks ")
        plt.xlabel("")
        plt.ylabel("Tasks")
        plt.tight_layout()
        plt.show()

    def graph_datebar(self):
        datetask_list = []
        datecount = []
        datetaskscount =[]
        data_loaded = self.manager.data_receive(login)
        for task in data_loaded["user"][login]:
            if task[2] == "0":
                datecount.append(task[1])
                if task[1] not in datetask_list: #do not want same day
                    datetask_list.append(task[1])
        for i in range(len(datetask_list)):
            datetaskscount.append(datecount.count(datetask_list[i]))
        plt.style.use("fivethirtyeight")
        plt.bar(datetask_list,datetaskscount)
        plt.title("Statis of Undone Tasks")
        plt.xlabel("Day")
        plt.ylabel("Tasks")
        plt.tight_layout()
        plt.show()




    
    
#taskCreatePage
class taskCreatePage(tk.Frame):
    def relative_to_assets(self,path: str) -> Path:
        return self.ASSETS_PATH / Path(path)
    
    def setName(self):
        if len(self.controller.user_file)>0 and len(self.controller.task_file) > 0:
            self.manager.user.setFileUser(self.controller.user_file)
            self.manager.user.setFileTask(self.controller.task_file)

    def openNewWindow(self):
        
        newWindow = tk.Toplevel(app)
        newWindow.title("Select Date")
        newWindow.geometry("400x400")   
        cal = Calendar(newWindow, selectmode = 'day', 
               year = 2022, month = 1, 
               day = 20)
        cal.pack(pady = 20) 
        def grad_date():
            date_deadline = cal.get_date()
            datesplit = date_deadline.split("/")
            datesort_split = datesplit[1] +"/"+datesplit[0]+"/"+datesplit[2]
            global time_deadline
            time_deadline = datesort_split      
            tk.messagebox.showinfo("ประกาศ","Selected Date is: " + time_deadline)
            newWindow.destroy() 
        Button(newWindow, text = "Get Date", command = grad_date).pack(pady = 20)
        return 1 
  

 

    def __init__(self,parent,controller):
        tk.Frame.__init__(self,parent)
        self.controller = controller
        self.manager = Manager()
        self.setName()

        self.OUTPUT_PATH = Path(__file__).parent
        self.ASSETS_PATH = self.OUTPUT_PATH / Path("./assets5")

        self.canvas = Canvas(
            self,
            bg = "#574B90",
            height = 617,
            width = 484,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file=self.relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            242.0,
            308.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=self.relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            242.0,
            320.0,
            image=self.image_image_2
        )

        self.entry_image_1 = PhotoImage(
            file=self.relative_to_assets("entry_1.png"))
        self.entry_bg_1 = self.canvas.create_image(
            233.0,
            278.5,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(self,
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0
        )
        self.entry_1.place(
            x=93.0,
            y=254.0,
            width=280.0,
            height=47.0
        )

        self.button_image_1 = PhotoImage(
            file=self.relative_to_assets("button_1.png"))
        self.button_1 = Button(self,
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: controller.show_frame("notePage"),
            relief="flat"
        )
        self.button_1.place(
            x=49.0,
            y=467.0,
            width=96.0,
            height=79.0
        )

        self.image_image_3 = PhotoImage(
            file=self.relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            71.0,
            50.0,
            image=self.image_image_3
        )

        self.canvas.create_text(
            100.0,
            40.0,
            anchor="nw",
            text="TO DO LIST",
            fill="#FFFFFF",
            font=("Roboto", 24 * -1)
        )

        self.button_image_2 = PhotoImage(
            file=self.relative_to_assets("button_2.png"))
        self.button_2 = Button(self,
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=lambda:taskCreatePage.openNewWindow(self) ,
            relief="flat"
        )
        self.button_2.place(
            x=86.0,
            y=329.0,
            width=156.0236358642578,
            height=43.0
        )

        self.image_image_4 = PhotoImage(
            file=self.relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            241.0,
            150.0,
            image=self.image_image_4
        )

        self.button_image_3 = PhotoImage(
            file=self.relative_to_assets("button_3.png"))
        self.button_3 = Button(self,
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: self.add_todo(login,self.entry_1,time_deadline),
            relief="flat"
        )
        self.button_3.place(
            x=93.0,
            y=407.0,
            width=280.0,
            height=49.0
        )

        self.canvas.create_text(
            104.0,
            235.0,
            anchor="nw",
            text="Enter task name",
            fill="#000000",
            font=("Roboto", 14 * -1)
        )
    
            
    def add_todo(self,login,entry_1,deadline): 
        name_task = entry_1.get()
        name_tasks = name_task.replace('{', '')
        name_tasks = name_task.replace('}',"")
        if "  " in name_tasks or name_tasks == "":
            tk.messagebox.showinfo("ประกาศ","Please enter your task")         
        else:
            list_todo = [name_tasks,deadline,"0"]
            gettodo = self.manager.todo.add_todo(login,list_todo, self.manager.user)            
            self.entry_1.delete(0, END)
            if gettodo == 1:
                tk.messagebox.showinfo("ประกาศ","Add Task successed!")



#displayFrame
class displayFrame(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.user_file = ""
        self.task_file = ""

        self.frames = {}
        for F in (loginPage,registerPage,notePage,taskCreatePage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("loginPage")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        if page_name == "notePage":
            self.frames[page_name].load_tasks(self.frames['loginPage'].login)

        frame = self.frames[page_name]
        frame.setName()
        frame.tkraise()



app = displayFrame()
app.geometry("484x617")
app.configure(bg = "#574B90")
app.mainloop()
