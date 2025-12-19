from tkinter import *

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")

        # Main Title
        title = Label(
            self.root,
            text="Employee Payroll Management System",
            font=("time new roman", 30, "bold"),
            bg="#262626",
            fg="white",
            padx=10,
        )
        title.place(x=0, y=0, relwidth=1)

        # Frame1
        Frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=750, height=580)

        # Title inside Frame1
        title_label = Label(
            Frame1,
            text="Employee Payroll Management",
            font=("times new roman", 20, "bold"),
            bg="white",
            fg="black",
        )
        title_label.place(x=200, y=10)

        # Section 1: Employee Details
        section1_label = Label(
            Frame1,
            text="Employee Details",
            font=("times new roman", 16, "bold"),
            bg="white",
            fg="black",
        )
        section1_label.place(x=10, y=50)

        # Column 1 (Left side)
        lbl_code = Label(
            Frame1,
            text="Employee Code:",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_code.place(x=10, y=90)
        txt_code = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_code.place(x=150, y=90, width=200)

        lbl_description = Label(
            Frame1,
            text="Description:",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_description.place(x=10, y=130)
        txt_description = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_description.place(x=150, y=130, width=200)

        lbl_name = Label(
            Frame1, text="Name:", font=("times new roman", 12), bg="white", fg="black"
        )
        lbl_name.place(x=10, y=170)
        txt_name = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_name.place(x=150, y=170, width=200)

        lbl_age = Label(
            Frame1, text="Age:", font=("times new roman", 12), bg="white", fg="black"
        )
        lbl_age.place(x=10, y=210)
        txt_age = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_age.place(x=150, y=210, width=200)

        lbl_gender = Label(
            Frame1, text="Gender:", font=("times new roman", 12), bg="white", fg="black"
        )
        lbl_gender.place(x=10, y=250)
        txt_gender = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_gender.place(x=150, y=250, width=200)

        lbl_email = Label(
            Frame1, text="Email:", font=("times new roman", 12), bg="white", fg="black"
        )
        lbl_email.place(x=10, y=290)
        txt_email = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_email.place(x=150, y=290, width=200)

        lbl_hired_location = Label(
            Frame1,
            text="Hired Location:",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_hired_location.place(x=10, y=330)
        txt_hired_location = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_hired_location.place(x=150, y=330, width=200)

        lbl_address = Label(
            Frame1,
            text="Address:",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_address.place(x=10, y=370)
        txt_address = Text(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
            height=3,
            width=25
        )
        txt_address.place(x=150, y=370, width=200)

        # Column 2 (Right side) - Search section
        section2_label = Label(
            Frame1,
            text="Search",
            font=("times new roman", 16, "bold"),
            bg="white",
            fg="black",
        )
        section2_label.place(x=500, y=50)

        lbl_dob = Label(
            Frame1, text="D.O.B:", font=("times new roman", 12), bg="white", fg="black"
        )
        lbl_dob.place(x=400, y=90)
        txt_dob = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_dob.place(x=500, y=90, width=200)

        lbl_doj = Label(
            Frame1, text="D.O.J:", font=("times new roman", 12), bg="white", fg="black"
        )
        lbl_doj.place(x=400, y=130)
        txt_doj = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_doj.place(x=500, y=130, width=200)

        lbl_experience = Label(
            Frame1,
            text="Experience:",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_experience.place(x=400, y=170)
        txt_experience = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_experience.place(x=500, y=170, width=200)

        lbl_proof_id = Label(
            Frame1,
            text="Proof ID:",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_proof_id.place(x=400, y=210)
        txt_proof_id = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_proof_id.place(x=500, y=210, width=200)

        lbl_contact = Label(
            Frame1,
            text="Contact:",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_contact.place(x=400, y=250)
        txt_contact = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_contact.place(x=500, y=250, width=200)

        lbl_status = Label(
            Frame1, text="Status:", font=("times new roman", 12), bg="white", fg="black"
        )
        lbl_status.place(x=400, y=290)
        txt_status = Entry(
            Frame1,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_status.place(x=500, y=290, width=200)

        # Buttons at the bottom
        btn_save = Button(
            Frame1,
            text="Save",
            font=("times new roman", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            bd=2,
            relief=RAISED,
        )
        btn_save.place(x=400, y=450, width=100, height=35)

        btn_update = Button(
            Frame1,
            text="Update",
            font=("times new roman", 12, "bold"),
            bg="#2196F3",
            fg="white",
            bd=2,
            relief=RAISED,
        )
        btn_update.place(x=520, y=450, width=100, height=35)

        btn_delete = Button(
            Frame1,
            text="Delete",
            font=("times new roman", 12, "bold"),
            bg="#F44336",
            fg="white",
            bd=2,
            relief=RAISED,
        )
        btn_delete.place(x=640, y=450, width=100, height=35)

        btn_clear = Button(
            Frame1,
            text="Clear",
            font=("times new roman", 12, "bold"),
            bg="#FF9800",
            fg="white",
            bd=2,
            relief=RAISED,
        )
        btn_clear.place(x=400, y=500, width=100, height=35)

        # Frame2
        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=770, y=70, width=570, height=250)

        lbl_months = Label(
            Frame2,
            text="Months",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_months.place(x=10, y=10)
        txt_months = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_months.place(x=100, y=10, width=150)
        
        lbl_years = Label(
            Frame2,
            text="Years",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_years.place(x=300, y=10)
        years_txt = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        years_txt.place(x=400, y=10, width=150)
        
        lbl_salary = Label(
            Frame2,
            text="Salary",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_salary.place(x=10, y=50)
        txt_salary = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_salary.place(x=100, y=50, width=150)
        
        Total_Days = Label(
            Frame2,
            text="Total Days",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        Total_Days.place(x=300, y=50)
        txt_total_days = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_total_days.place(x=400, y=50, width=150)
        
        Absent_Days = Label(
            Frame2,
            text="Absent Days",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        Absent_Days.place(x=10, y=90)
        txt_absent_days = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_absent_days.place(x=100, y=90, width=150)
        
        lbl_Medical = Label(
            Frame2,
            text="Medical",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_Medical.place(x=300, y=90)
        txt_medical = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_medical.place(x=400, y=90, width=150)
        
        lbl_Pf = Label(
            Frame2,
            text="PF",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_Pf.place(x=10, y=130)
        txt_pf = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_pf.place(x=100, y=130, width=150)
        
        lbl_Net_Salary = Label(
            Frame2,
            text="Net Salary",
            font=("times new roman", 12),
            bg="white",
            fg="black",
        )
        lbl_Net_Salary.place(x=300, y=130)
        txt_net_salary = Entry(
            Frame2,
            font=("times new roman", 12),
            bg="#F0F0F0",
            fg="black",
            bd=2,
            relief=GROOVE,
        )
        txt_net_salary.place(x=400, y=130, width=150)
        
        # Buttons in Frame2
        btn_calculate = Button(
            Frame2,
            text="Calculate",
            font=("times new roman", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            bd=2,
            relief=RAISED,
        )
        btn_calculate.place(x=150, y=180, width=100, height=30)
        
        btn_save2 = Button(
            Frame2,
            text="Save",
            font=("times new roman", 12, "bold"),
            bg="#2196F3",
            fg="white",
            bd=2,
            relief=RAISED,
        )
        btn_save2.place(x=270, y=180, width=100, height=30)
        
        btn_clear2 = Button(
            Frame2,
            text="Clear",
            font=("times new roman", 12, "bold"),
            bg="#FF9800",
            fg="white",
            bd=2,
            relief=RAISED,
        )
        btn_clear2.place(x=390, y=180, width=100, height=30)

        # Frame3
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame3.place(x=770, y=330, width=570, height=320)

        # Calculator Frame
        calc_frame = Frame(Frame3, bd=2, relief=RIDGE, bg="white")
        calc_frame.place(x=5, y=5, width=270, height=310)

        # Calculator Title
        calc_title = Label(
            calc_frame,
            text="Salary Calculator",
            font=("times new roman", 14, "bold"),
            bg="#262626",
            fg="white",
        )
        calc_title.place(x=0, y=0, width=270, height=30)

        # Calculator Display
        calc_display = Entry(
            calc_frame,
            font=("times new roman", 14, "bold"),
            bg="lightgray",
            fg="black",
            bd=5,
            relief=SUNKEN,
            justify=RIGHT,
        )
        calc_display.place(x=10, y=40, width=250, height=40)

        # Calculator Buttons
        button_frame = Frame(calc_frame, bg="white")
        button_frame.place(x=10, y=90, width=250, height=210)

        # Calculator buttons layout
        buttons = [
            ("7", "8", "9"),
            ("4", "5", "6"),
            ("1", "2", "3"),
            ("C", "0", "-"),
        ]

        # Create calculator buttons
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                btn_color = "#F0F0F0"
                if text == "C":
                    btn_color = "#FF6B6B"
                elif text == "-":
                    btn_color = "#2196F3"

                btn = Button(
                    button_frame,
                    text=text,
                    font=("times new roman", 12, "bold"),
                    bg=btn_color,
                    fg="black",
                    bd=2,
                    relief=RAISED,
                    command=lambda t=text: self.on_calc_button_click(t, calc_display),
                )
                btn.place(x=j * 83, y=i * 52, width=80, height=50)

        # Salary Input Section (Right side of Frame3)
        salary_frame = Frame(Frame3, bd=2, relief=RIDGE, bg="white")
        salary_frame.place(x=280, y=5, width=285, height=310)

        # Salary Calculation Title
        salary_title = Label(
            salary_frame,
            text="Salary Details",
            font=("times new roman", 14, "bold"),
            bg="#262626",
            fg="white",
        )
        salary_title.place(x=0, y=0, width=285, height=30)

        # Salary Input Fields
        salary_labels = [
            "Basic Salary:",
            "Allowances:",
            "Deductions:",
            "Overtime:",
            "Bonus:",
            "Net Salary:",
        ]
        salary_entries = []

        for i, label_text in enumerate(salary_labels):
            lbl = Label(
                salary_frame,
                text=label_text,
                font=("times new roman", 12),
                bg="white",
                fg="black",
            )
            lbl.place(x=10, y=40 + i * 40, width=120)

            entry = Entry(
                salary_frame,
                font=("times new roman", 12),
                bg="#F0F0F0",
                fg="black",
                bd=2,
                relief=GROOVE,
            )
            entry.place(x=140, y=40 + i * 40, width=130)
            btn_calculate_salary = Button(
              salary_frame,
                text="Calculate Salary",
                font=("times new roman", 12, "bold"),
                bg="#4CAF50",
                fg="white",
                bd=2,
                relief=RAISED,
                command=lambda: self.calculate_salary(salary_entries)
            )
            btn_calculate_salary.place(x=10, y=280, width=265, height=30)

            if "Net Salary:" in label_text:
                entry.config(state="readonly", readonlybackground="#E8F5E8")

            salary_entries.append(entry)

root = Tk()
obj = EmployeeSystem(root)
root.mainloop()
