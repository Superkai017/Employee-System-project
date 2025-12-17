from tkinter import *

class EmployeeSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700")
        title = Label(self.root, text = "Employee payroll manager system", font =( "time new roman", 30,"bold"), bg = "#262626" , fg = "white").place( x = 0, y=0, relwidth = 1)
root=Tk()
obj = EmployeeSystem(root)
root.mainloop()