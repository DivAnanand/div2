from tkinter import *
from NoteDB import NoteDB
from tkinter import messagebox
from DashBoard import Dashboard
if __name__=="__main__":
    try:
        db=NoteDB(username="root",password="rockstardiv")
        Dashboard().initUI(db)
    except Exception as e:
        messagebox.showinfo("Error","Unable to establish  database connection")
