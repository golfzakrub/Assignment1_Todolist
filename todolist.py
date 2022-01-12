import tkinter as tk
import tkinter.messagebox
import json
from tkinter import * 
from tkinter.ttk import *


class Editor():                                                 #Edit everything

    def add_task(entry_task, listbox_tasks):
        task = entry_task.get()
        if task != "":
            listbox_tasks.insert(tkinter.END, task)
            entry_task.delete(0, tkinter.END)
        else:
            tkinter.messagebox.showwarning(
                title="Warning!", message="You must enter a task.")

    def delete_task(listbox_tasks):
        try:
            task_index = listbox_tasks.curselection()[0]
            listbox_tasks.delete(task_index)
        except:
            tkinter.messagebox.showwarning(
                title="Warning!", message="You must select a task.")

    def load_tasks(listbox_tasks):
        try:
            with open('data.json', 'r') as data_file:
                data_loaded = json.load(data_file)
            listbox_tasks.delete(0, tkinter.END)
            for task in data_loaded:
                listbox_tasks.insert(tkinter.END, task)
        except:
            tkinter.messagebox.showwarning(
                title="Warning!", message="Cannot find tasks.dat.")

    def save_tasks(listbox_tasks):
        tasks = listbox_tasks.get(0, listbox_tasks.size())
        with open('data.json', 'w') as data_file:
            json.dump(tasks, data_file)


class main(tk.Tk):                            #Show Frame(GUI)
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage,PageTwo): #PageOne

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()
        frame.configure(bg='crimson')


class StartPage(tk.Frame):         

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self,text="TO DO LIST Ver1.0",font=('Arial', 15),bg="lightgray")
        label.pack(pady=300, padx=150)

        # canvas = Canvas(self, width = 300, height = 300)      
        # canvas.pack()      
        # img = PhotoImage(file="F:\_coding\softdev2\week2\_1bc.png")      
        # canvas.create_image(20,20, anchor=NW, image=img)      


        button1 = tk.Button(self, text="Visit ToDoList", font=('Arial', 10),
                            command=lambda: controller.show_frame(PageTwo))

        button1.pack(side=tk.BOTTOM)


# class PageOne(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         label = tk.Label(self, text="Folder!")
#         label.pack(pady=300, padx=150)

#         button1 = tk.Button(self, text="Back to Home", font=('Arial', 10),
#                             command=lambda: controller.show_frame(StartPage))
#         button1.pack()

#         button2 = tk.Button(self, text="Go to Note", font=('Arial', 10),
#                             command=lambda: controller.show_frame(PageTwo))
#         button2.pack()


class PageTwo(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        # label = tk.Label(self,text="Page Note!!")
        # label.pack(pady=400,padx=200)
        # root = tkinter.Tk()
        # root.title("To-Do List ")

        button1 = tk.Button(self, text="Back to Home", font=('Arial', 10),
                            command=lambda: controller.show_frame(StartPage))
        button1.pack()

        # button2 = tk.Button(self, text="Return to Folder", font=('Arial', 10),
        #                     command=lambda: controller.show_frame(PageOne))
        # button2.pack()

        todolist1 = tkinter.IntVar()
        tkinter.Checkbutton(self ,variable=todolist1).pack()

        listbox_tasks = tk.Listbox(self, height=10, width=30, bg="#E5E5E5",font=('Arial', 20))
        listbox_tasks.pack()

        # scrollbar_tasks = tk.Scrollbar(self)
        # scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

        # listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
        # scrollbar_tasks.config(command=listbox_tasks.yview)



        button_save_tasks = tk.Button(self, text="Save tasks", font=(
            'Arial', 10), width=10, command=lambda: Editor.save_tasks(listbox_tasks))
        button_save_tasks.pack(side=tk.BOTTOM)

        button_load_tasks = tk.Button(self, text="Load tasks", font=(
            'Arial', 10), width=10, command=lambda: Editor.load_tasks(listbox_tasks))
        button_load_tasks.pack(side=tk.BOTTOM)

        button_delete_task = tk.Button(self, text="Delete task", font=(
            'Arial', 10), width=10, command=lambda: Editor.delete_task(listbox_tasks))
        button_delete_task.pack(side=tk.BOTTOM)

        button_add_task = tk.Button(self, text="Add task", font=(
            'Arial', 10), width=10, command=lambda: Editor.add_task(entry_task, listbox_tasks))
        button_add_task.pack(side=tk.BOTTOM)

        entry_task = tk.Entry(self,width=40,font=('Arial', 15))
        entry_task.pack(side=tk.BOTTOM)




app = main()
app.mainloop()
