import json
import os
from datetime import datetime

class EmployeeDatabase:
    def __init__(self, filename="employees.json"):
        self.filename = filename
        self.ensure_file_exists()
    
    def ensure_file_exists(self):
        """Create empty JSON file if it doesn't exist"""
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump({"employees": []}, f, indent=4)
    
    def load_data(self):
        """Load all employee data from JSON file"""
        try:
            with open(self.filename, 'r') as f:
                data = json.load(f)
                return data.get("employees", [])
        except (json.JSONDecodeError, FileNotFoundError):
            return []
    
    def save_data(self, employees):
        """Save employee data to JSON file"""
        data = {"employees": employees}
        with open(self.filename, 'w') as f:
            json.dump(data, f, indent=4)
    
    def get_next_id(self):
        """Generate next employee ID"""
        employees = self.load_data()
        if not employees:
            return 1
        
        max_id = 0
        for emp in employees:
            try:
                emp_id = int(emp.get("employee_code", 0))
                if emp_id > max_id:
                    max_id = emp_id
            except (ValueError, TypeError):
                pass
        
        return max_id + 1
    
    def add_employee(self, employee_data):
        """Add a new employee"""
        employees = self.load_data()
        
        # Generate employee code if not provided
        if not employee_data.get("employee_code") or employee_data.get("employee_code") == "":
            employee_data["employee_code"] = str(self.get_next_id())
        
        # Add timestamps
        employee_data["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        employee_data["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        employees.append(employee_data)
        self.save_data(employees)
        return employee_data["employee_code"]
    
    def update_employee(self, employee_code, updated_data):
        """Update employee information"""
        employees = self.load_data()
        
        for i, emp in enumerate(employees):
            if str(emp.get("employee_code")) == str(employee_code):
                # Preserve some fields
                updated_data["employee_code"] = employee_code
                updated_data["created_at"] = emp.get("created_at", "")
                updated_data["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                employees[i] = updated_data
                self.save_data(employees)
                return True
        return False
    
    def delete_employee(self, employee_code):
        """Delete employee by code"""
        employees = self.load_data()
        initial_count = len(employees)
        
        employees = [
            emp for emp in employees 
            if str(emp.get("employee_code", "")).strip() != str(employee_code).strip()
        ]
        
        if len(employees) < initial_count:
            self.save_data(employees)
            return True
        return False
    
    def search_employee(self, search_term="", search_by="employee_code"):
        """Search employees by various criteria"""
        employees = self.load_data()
        
        if not search_term or search_term.strip() == "":
            return employees
        
        search_term = str(search_term).lower().strip()
        results = []
        
        for emp in employees:
            emp_code = str(emp.get("employee_code", "")).lower().strip()
            emp_name = str(emp.get("name", "")).lower().strip()
            emp_email = str(emp.get("email", "")).lower().strip()
            emp_contact = str(emp.get("contact", "")).strip()
            
            if search_by == "employee_code":
                if search_term == emp_code:
                    results.append(emp)
            elif search_by == "name":
                if search_term in emp_name:
                    results.append(emp)
            elif search_by == "email":
                if search_term in emp_email:
                    results.append(emp)
            elif search_by == "contact":
                if search_term in emp_contact:
                    results.append(emp)
            elif search_by == "all":
                # Search in all fields
                if (search_term in emp_code or 
                    search_term in emp_name or 
                    search_term in emp_email or
                    search_term in emp_contact):
                    results.append(emp)
        
        return results
    
    def get_employee_by_code(self, employee_code):
        """Get single employee by code"""
        results = self.search_employee(employee_code, "employee_code")
        return results[0] if results else None
    
    def get_all_employees(self):
        """Get all employees"""
        return self.load_data()
    
    def export_data(self, filename="employees_export.json"):
        """Export data to separate file"""
        data = {
            "export_date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "total_employees": len(self.load_data()),
            "employees": self.load_data()
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=4)
        
        return True, f"Data exported to {filename}"