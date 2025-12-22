from tkinter import *
from tkinter import messagebox, ttk
import json
from EmployeesManager import EmployeeBackend

class EmployeeSystem:
    def __init__(self, root):
        self.root = root
        self.backend = EmployeeBackend()
        
        # Set window properties
        self.root.title("Employee Payroll Management System")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        
        # Store widgets
        self.entries = {}
        self.salary_entries = []
        
        # Initialize UI
        self.setup_ui()
    
    def setup_ui(self):
        """Setup the complete user interface"""
        # Main Title
        title = Label(
            self.root,
            text="Employee Payroll Management System",
            font=("Arial", 30, "bold"),
            bg="#262626",
            fg="white",
        )
        title.place(x=0, y=0, relwidth=1, height=60)
        
        # ========== FRAME 1: Employee Details ==========
        Frame1 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame1.place(x=10, y=70, width=750, height=580)
        
        # Frame Title
        Label(
            Frame1,
            text="Employee Details",
            font=("Arial", 20, "bold"),
            bg="white",
            fg="black"
        ).place(x=250, y=10)
        
        # Create employee form
        self.create_employee_form(Frame1)
        
        # ========== FRAME 2: Monthly Details ==========
        Frame2 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame2.place(x=770, y=70, width=570, height=250)
        
        Label(
            Frame2,
            text="Monthly Payroll Details",
            font=("Arial", 16, "bold"),
            bg="white",
            fg="black"
        ).place(x=170, y=10)
        
        self.create_monthly_details(Frame2)
        
        # ========== FRAME 3: Calculator & Salary ==========
        Frame3 = Frame(self.root, bd=3, relief=RIDGE, bg="white")
        Frame3.place(x=770, y=330, width=570, height=320)
        
        self.create_calculator_section(Frame3)
    
    def create_employee_form(self, parent):
        """Create employee input form"""
        # Left Column Labels and Entries
        left_fields = [
            ("Employee Code:", "employee_code", 10, 50),
            ("Name:", "name", 10, 90),
            ("Age:", "age", 10, 130),
            ("Gender:", "gender", 10, 170),
            ("Email:", "email", 10, 210),
            ("Contact:", "contact", 10, 250),
            ("Address:", "address", 10, 290),
        ]
        
        for label_text, field_name, x, y in left_fields:
            lbl = Label(parent, text=label_text, font=("Arial", 12), bg="white")
            lbl.place(x=x, y=y)
            
            if field_name == "address":
                entry = Text(parent, font=("Arial", 11), height=3, width=25, bd=2, relief=GROOVE)
                entry.place(x=x+120, y=y, width=200, height=70)
            else:
                entry = Entry(parent, font=("Arial", 11), bd=2, relief=GROOVE)
                entry.place(x=x+120, y=y, width=200, height=30)
            
            self.entries[field_name] = entry
        
        # Right Column Labels and Entries
        right_fields = [
            ("Description:", "description", 400, 50),
            ("DOB (dd/mm/yyyy):", "dob", 400, 90),
            ("DOJ (dd/mm/yyyy):", "doj", 400, 130),
            ("Experience (years):", "experience", 400, 170),
            ("Proof ID:", "proof_id", 400, 210),
            ("Status:", "status", 400, 250),
            ("Hired Location:", "hired_location", 400, 290),
        ]
        
        for label_text, field_name, x, y in right_fields:
            lbl = Label(parent, text=label_text, font=("Arial", 12), bg="white")
            lbl.place(x=x, y=y)
            
            entry = Entry(parent, font=("Arial", 11), bd=2, relief=GROOVE)
            entry.place(x=x+150, y=y, width=200, height=30)
            self.entries[field_name] = entry
        
        # Buttons Section
        buttons = [
            ("Save", self.save_employee, "#4CAF50", 400, 380),
            ("Update", self.update_employee, "#2196F3", 520, 380),
            ("Delete", self.delete_employee, "#F44336", 640, 380),
            ("Clear", self.clear_form, "#FF9800", 400, 420),
            ("Search", self.search_employee_window, "#9C27B0", 520, 420),
            ("View All", self.view_all_employees, "#607D8B", 640, 420),
        ]
        
        for text, command, color, x, y in buttons:
            btn = Button(
                parent,
                text=text,
                font=("Arial", 12, "bold"),
                bg=color,
                fg="white",
                bd=2,
                relief=RAISED,
                command=command
            )
            btn.place(x=x, y=y, width=100, height=35)
    
    def create_monthly_details(self, parent):
        """Create monthly salary details section"""
        fields = [
            ("Months:", "months", 10, 50),
            ("Years:", "years", 300, 50),
            ("Basic Salary:", "basic_salary", 10, 90),
            ("Total Days:", "total_days", 300, 90),
            ("Absent Days:", "absent_days", 10, 130),
            ("Medical:", "medical", 300, 130),
            ("PF:", "pf", 10, 170),
            ("Net Salary:", "net_salary", 300, 170),
        ]
        
        for label_text, field_name, x, y in fields:
            lbl = Label(parent, text=label_text, font=("Arial", 12), bg="white")
            lbl.place(x=x, y=y)
            
            entry = Entry(parent, font=("Arial", 11), bd=2, relief=GROOVE)
            entry.place(x=x+100, y=y, width=150, height=30)
            self.entries[field_name] = entry
        
        # Buttons
        Button(
            parent,
            text="Calculate Monthly",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=self.calculate_monthly_salary
        ).place(x=150, y=210, width=150, height=35)
        
        Button(
            parent,
            text="Clear",
            font=("Arial", 12, "bold"),
            bg="#FF9800",
            fg="white",
            command=self.clear_monthly_fields
        ).place(x=350, y=210, width=150, height=35)
    
    def create_calculator_section(self, parent):
        """Create calculator and salary calculation section"""
        # Calculator Frame (Left)
        calc_frame = Frame(parent, bd=2, relief=RIDGE, bg="#f5f5f5")
        calc_frame.place(x=5, y=5, width=270, height=310)
        
        Label(
            calc_frame,
            text="Calculator",
            font=("Arial", 14, "bold"),
            bg="#2c3e50",
            fg="white"
        ).place(x=0, y=0, width=270, height=40)
        
        # Calculator Display
        self.calc_display = Entry(
            calc_frame,
            font=("Consolas", 16, "bold"),
            bg="white",
            fg="#2c3e50",
            bd=3,
            relief=SUNKEN,
            justify=RIGHT
        )
        self.calc_display.place(x=10, y=50, width=250, height=40)
        self.calc_display.insert(0, "0")
        
        # Calculator Buttons
        self.create_calculator_buttons(calc_frame)
        
        # Salary Calculator Frame (Right)
        salary_frame = Frame(parent, bd=2, relief=RIDGE, bg="#f5f5f5")
        salary_frame.place(x=280, y=5, width=285, height=310)
        
        Label(
            salary_frame,
            text="Salary Calculator",
            font=("Arial", 14, "bold"),
            bg="#27ae60",
            fg="white"
        ).place(x=0, y=0, width=285, height=40)
        
        # Salary Fields
        salary_fields = [
            ("Basic Salary:", "calc_basic", 10, 50),
            ("Allowances:", "calc_allowances", 10, 90),
            ("Deductions:", "calc_deductions", 10, 130),
            ("Overtime Hours:", "calc_overtime", 10, 170),
            ("Bonus:", "calc_bonus", 10, 210),
            ("Net Salary:", "calc_net_salary", 10, 250),
        ]
        
        self.salary_entries = []
        for i, (label_text, field_name, x, y) in enumerate(salary_fields):
            lbl = Label(salary_frame, text=label_text, font=("Arial", 11), bg="#f5f5f5")
            lbl.place(x=x, y=y)
            
            entry = Entry(salary_frame, font=("Arial", 11), bd=2, relief=GROOVE)
            if "Net Salary" in label_text:
                entry.config(state="readonly", bg="#e8f5e9", fg="#27ae60")
            
            entry.place(x=x+120, y=y, width=140, height=30)
            self.salary_entries.append(entry)
            self.entries[field_name] = entry
        
        # Calculate Salary Button
        Button(
            salary_frame,
            text="Calculate Salary",
            font=("Arial", 12, "bold"),
            bg="#27ae60",
            fg="white",
            command=self.calculate_salary
        ).place(x=10, y=280, width=265, height=25)
    
    def create_calculator_buttons(self, parent):
        """Create calculator buttons"""
        buttons = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("C", "0", ".", "+"),
            ("(", ")", "⌫", "="),
        ]
        
        for i, row in enumerate(buttons):
            for j, text in enumerate(row):
                # Color coding
                if text in ["C", "⌫"]:
                    bg_color = "#e74c3c"
                elif text in ["+", "-", "*", "/", "="]:
                    bg_color = "#3498db"
                elif text in ["(", ")"]:
                    bg_color = "#9b59b6"
                else:
                    bg_color = "#ffffff"
                
                btn = Button(
                    parent,
                    text=text,
                    font=("Arial", 12, "bold"),
                    bg=bg_color,
                    fg="black" if bg_color == "#ffffff" else "white",
                    bd=2,
                    relief=RAISED,
                    command=lambda t=text: self.on_calc_button_click(t)
                )
                btn.place(x=10 + j*62, y=100 + i*45, width=60, height=40)
    
    # ========== DATABASE OPERATIONS ==========
    
    def save_employee(self):
        """Save employee to database"""
        try:
            # Collect data from form
            employee_data = {
                "employee_code": self.entries["employee_code"].get().strip(),
                "name": self.entries["name"].get().strip(),
                "age": self.entries["age"].get().strip(),
                "gender": self.entries["gender"].get().strip(),
                "email": self.entries["email"].get().strip(),
                "contact": self.entries["contact"].get().strip(),
                "address": self.entries["address"].get("1.0", END).strip(),
                "description": self.entries["description"].get().strip(),
                "dob": self.entries["dob"].get().strip(),
                "doj": self.entries["doj"].get().strip(),
                "experience": self.entries["experience"].get().strip(),
                "proof_id": self.entries["proof_id"].get().strip(),
                "status": self.entries["status"].get().strip() or "Active",
                "hired_location": self.entries["hired_location"].get().strip(),
            }
            
            # Add salary data if available
            try:
                employee_data["basic_salary"] = float(self.entries["basic_salary"].get() or 0)
                employee_data["net_salary"] = float(self.entries["net_salary"].get() or 0)
            except:
                employee_data["basic_salary"] = 0
                employee_data["net_salary"] = 0
            
            # Save to database
            success, message = self.backend.add_new_employee(employee_data)
            
            if success:
                # Update employee code field with generated code
                emp_code = message.split(": ")[-1]
                self.entries["employee_code"].delete(0, END)
                self.entries["employee_code"].insert(0, emp_code)
                
                messagebox.showinfo("Success", message)
                self.clear_form()
            else:
                messagebox.showerror("Error", message)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save employee: {str(e)}")
    
    def update_employee(self):
        """Update existing employee"""
        try:
            emp_code = self.entries["employee_code"].get().strip()
            if not emp_code:
                messagebox.showwarning("Warning", "Please enter Employee Code")
                return
            
            employee_data = {
                "name": self.entries["name"].get().strip(),
                "age": self.entries["age"].get().strip(),
                "gender": self.entries["gender"].get().strip(),
                "email": self.entries["email"].get().strip(),
                "contact": self.entries["contact"].get().strip(),
                "address": self.entries["address"].get("1.0", END).strip(),
                "description": self.entries["description"].get().strip(),
                "dob": self.entries["dob"].get().strip(),
                "doj": self.entries["doj"].get().strip(),
                "experience": self.entries["experience"].get().strip(),
                "proof_id": self.entries["proof_id"].get().strip(),
                "status": self.entries["status"].get().strip(),
                "hired_location": self.entries["hired_location"].get().strip(),
            }
            
            # Update salary data if available
            try:
                employee_data["basic_salary"] = float(self.entries["basic_salary"].get() or 0)
                employee_data["net_salary"] = float(self.entries["net_salary"].get() or 0)
            except:
                employee_data["basic_salary"] = 0
                employee_data["net_salary"] = 0
            
            success, message = self.backend.update_employee(emp_code, employee_data)
            
            if success:
                messagebox.showinfo("Success", message)
            else:
                messagebox.showerror("Error", message)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to update employee: {str(e)}")
    
    def delete_employee(self):
        """Delete employee from database"""
        try:
            emp_code = self.entries["employee_code"].get().strip()
            if not emp_code:
                messagebox.showwarning("Warning", "Please enter Employee Code")
                return
            
            # Confirm deletion
            confirm = messagebox.askyesno("Confirm", f"Delete employee {emp_code}?")
            if not confirm:
                return
            
            success, message = self.backend.delete_employee(emp_code)
            
            if success:
                messagebox.showinfo("Success", message)
                self.clear_form()
            else:
                messagebox.showerror("Error", message)
                
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete employee: {str(e)}")
    
    def search_employee_window(self):
        """Open search window"""
        search_win = Toplevel(self.root)
        search_win.title("Search Employee")
        search_win.geometry("600x500")
        search_win.config(bg="white")
        
        # Title
        Label(
            search_win,
            text="Search Employees",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=10)
        
        # Search controls
        search_frame = Frame(search_win, bg="white")
        search_frame.pack(pady=10)
        
        Label(search_frame, text="Search By:", bg="white", font=("Arial", 11)).grid(row=0, column=0, padx=5, pady=5)
        
        search_by = StringVar(value="all")
        OptionMenu(
            search_frame, search_by,
            "all", "employee_code", "name", "email", "contact"
        ).grid(row=0, column=1, padx=5, pady=5)
        
        Label(search_frame, text="Search Term:", bg="white", font=("Arial", 11)).grid(row=1, column=0, padx=5, pady=5)
        search_entry = Entry(search_frame, font=("Arial", 11), width=30)
        search_entry.grid(row=1, column=1, padx=5, pady=5)
        
        # Results area
        results_frame = Frame(search_win, bg="white")
        results_frame.pack(pady=10, fill=BOTH, expand=True, padx=10)
        
        # Treeview for results
        tree = ttk.Treeview(results_frame, columns=("Code", "Name", "Email", "Contact"), show="headings", height=15)
        tree.heading("Code", text="Employee Code")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.heading("Contact", text="Contact")
        
        tree.column("Code", width=80)
        tree.column("Name", width=150)
        tree.column("Email", width=150)
        tree.column("Contact", width=100)
        
        tree.pack(fill=BOTH, expand=True)
        
        # Scrollbar
        scrollbar = Scrollbar(results_frame, orient=VERTICAL, command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scrollbar.set)
        
        def perform_search():
            """Perform search operation"""
            # Clear previous results
            for item in tree.get_children():
                tree.delete(item)
            
            term = search_entry.get().strip()
            by = search_by.get()
            
            # Get search results
            results = self.backend.search_employees(term, by)
            
            # Display results
            for emp in results:
                tree.insert("", END, values=(
                    emp.get("employee_code", ""),
                    emp.get("name", ""),
                    emp.get("email", ""),
                    emp.get("contact", "")
                ))
        
        def on_select(event):
            """Load selected employee data"""
            selected = tree.focus()
            if selected:
                values = tree.item(selected, "values")
                if values and values[0]:
                    self.load_employee_data(values[0])
                    search_win.destroy()
        
        # Bind events
        tree.bind("<<TreeviewSelect>>", on_select)
        
        # Search button
        Button(
            search_win,
            text="Search",
            font=("Arial", 12, "bold"),
            bg="#4CAF50",
            fg="white",
            command=perform_search
        ).pack(pady=10)
    
    def load_employee_data(self, emp_code):
        """Load employee data into form"""
        try:
            employee = self.backend.get_employee_by_code(emp_code)
            if not employee:
                messagebox.showinfo("Info", "Employee not found")
                return
            
            # Clear form first
            self.clear_form()
            
            # Fill form fields
            self.entries["employee_code"].insert(0, employee.get("employee_code", ""))
            self.entries["name"].insert(0, employee.get("name", ""))
            self.entries["age"].insert(0, employee.get("age", ""))
            self.entries["gender"].insert(0, employee.get("gender", ""))
            self.entries["email"].insert(0, employee.get("email", ""))
            self.entries["contact"].insert(0, employee.get("contact", ""))
            self.entries["address"].delete("1.0", END)
            self.entries["address"].insert("1.0", employee.get("address", ""))
            self.entries["description"].insert(0, employee.get("description", ""))
            self.entries["dob"].insert(0, employee.get("dob", ""))
            self.entries["doj"].insert(0, employee.get("doj", ""))
            self.entries["experience"].insert(0, employee.get("experience", ""))
            self.entries["proof_id"].insert(0, employee.get("proof_id", ""))
            self.entries["status"].insert(0, employee.get("status", ""))
            self.entries["hired_location"].insert(0, employee.get("hired_location", ""))
            
            # Load salary data
            basic_salary = employee.get("basic_salary", 0)
            net_salary = employee.get("net_salary", 0)
            
            self.entries["basic_salary"].delete(0, END)
            self.entries["basic_salary"].insert(0, str(basic_salary))
            
            self.entries["net_salary"].delete(0, END)
            self.entries["net_salary"].insert(0, str(net_salary))
            
            messagebox.showinfo("Success", f"Loaded employee {emp_code}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load employee: {str(e)}")
    
    def view_all_employees(self):
        """View all employees in a new window"""
        all_win = Toplevel(self.root)
        all_win.title("All Employees")
        all_win.geometry("800x500")
        all_win.config(bg="white")
        
        # Title
        Label(
            all_win,
            text="All Employees",
            font=("Arial", 18, "bold"),
            bg="white"
        ).pack(pady=10)
        
        # Treeview
        tree_frame = Frame(all_win, bg="white")
        tree_frame.pack(fill=BOTH, expand=True, padx=10, pady=10)
        
        tree = ttk.Treeview(tree_frame, columns=("Code", "Name", "Email", "Contact", "Status"), show="headings", height=20)
        
        # Define columns
        tree.heading("Code", text="Emp Code")
        tree.heading("Name", text="Name")
        tree.heading("Email", text="Email")
        tree.heading("Contact", text="Contact")
        tree.heading("Status", text="Status")
        
        tree.column("Code", width=80)
        tree.column("Name", width=150)
        tree.column("Email", width=150)
        tree.column("Contact", width=100)
        tree.column("Status", width=80)
        
        tree.pack(side=LEFT, fill=BOTH, expand=True)
        
        # Scrollbar
        scrollbar = Scrollbar(tree_frame, orient=VERTICAL, command=tree.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        tree.configure(yscrollcommand=scrollbar.set)
        
        # Load all employees
        employees = self.backend.get_all_employees()
        
        for emp in employees:
            tree.insert("", END, values=(
                emp.get("employee_code", ""),
                emp.get("name", ""),
                emp.get("email", ""),
                emp.get("contact", ""),
                emp.get("status", "")
            ))
        
        # Total count
        Label(
            all_win,
            text=f"Total Employees: {len(employees)}",
            font=("Arial", 12, "bold"),
            bg="white"
        ).pack(pady=10)
    
    # ========== CALCULATION METHODS ==========
    
    def calculate_monthly_salary(self):
        """Calculate monthly salary based on attendance"""
        try:
            basic = self.entries["basic_salary"].get()
            total_days = self.entries["total_days"].get()
            absent_days = self.entries["absent_days"].get()
            medical = self.entries["medical"].get()
            pf = self.entries["pf"].get()
            
            net_salary = self.backend.calculate_monthly_salary(basic, total_days, absent_days, medical, pf)
            
            self.entries["net_salary"].delete(0, END)
            self.entries["net_salary"].insert(0, f"{net_salary:.2f}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")
    
    def calculate_salary(self):
        """Calculate salary using salary calculator"""
        try:
            basic = self.salary_entries[0].get()
            allowances = self.salary_entries[1].get()
            deductions = self.salary_entries[2].get()
            overtime = self.salary_entries[3].get()
            bonus = self.salary_entries[4].get()
            
            net_salary = self.backend.calculate_net_salary(basic, allowances, deductions, overtime, bonus)
            
            self.salary_entries[5].config(state="normal")
            self.salary_entries[5].delete(0, END)
            self.salary_entries[5].insert(0, f"{net_salary:.2f}")
            self.salary_entries[5].config(state="readonly")
            
        except Exception as e:
            messagebox.showerror("Error", f"Salary calculation error: {str(e)}")
    
    def on_calc_button_click(self, text):
        """Handle calculator button clicks"""
        current = self.calc_display.get()
        
        if text == "=":
            try:
                result = eval(current)
                self.calc_display.delete(0, END)
                self.calc_display.insert(0, str(result))
            except:
                self.calc_display.delete(0, END)
                self.calc_display.insert(0, "Error")
        elif text == "C":
            self.calc_display.delete(0, END)
            self.calc_display.insert(0, "0")
        elif text == "⌫":
            if current and current != "0":
                new_text = current[:-1]
                self.calc_display.delete(0, END)
                self.calc_display.insert(0, new_text if new_text else "0")
        else:
            if current == "0":
                self.calc_display.delete(0, END)
                self.calc_display.insert(0, text)
            else:
                self.calc_display.insert(END, text)
    
    # ========== UTILITY METHODS ==========
    
    def clear_form(self):
        """Clear all form fields"""
        for field_name, widget in self.entries.items():
            if isinstance(widget, Text):
                widget.delete("1.0", END)
            elif isinstance(widget, Entry):
                widget.delete(0, END)
        
        # Reset calculator
        self.calc_display.delete(0, END)
        self.calc_display.insert(0, "0")
    
    def clear_monthly_fields(self):
        """Clear monthly calculation fields"""
        monthly_fields = ["months", "years", "basic_salary", "total_days", 
                         "absent_days", "medical", "pf", "net_salary"]
        
        for field in monthly_fields:
            if field in self.entries:
                self.entries[field].delete(0, END)
        
        # Clear salary calculator
        for entry in self.salary_entries:
            entry.config(state="normal")
            entry.delete(0, END)
            if entry == self.salary_entries[5]:  # Net salary field
                entry.config(state="readonly")


# ========== MAIN APPLICATION ==========
if __name__ == "__main__":
    root = Tk()
    app = EmployeeSystem(root)
    root.mainloop()