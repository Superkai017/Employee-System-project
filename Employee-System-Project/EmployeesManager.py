from Employee import EmployeeDatabase

class EmployeeBackend:
    def __init__(self):
        self.db = EmployeeDatabase()
    
    def add_new_employee(self, employee_data):
        """Add new employee with validation"""
        # Required fields validation
        required_fields = ["name", "email", "contact"]
        for field in required_fields:
            if not employee_data.get(field, "").strip():
                return False, f"{field.title()} is required"
        
        try:
            emp_code = self.db.add_employee(employee_data)
            return True, f"Employee added successfully! Employee Code: {emp_code}"
        except Exception as e:
            return False, f"Error adding employee: {str(e)}"
    
    def update_employee(self, employee_code, employee_data):
        """Update existing employee"""
        if not employee_code or not employee_code.strip():
            return False, "Employee code is required"
        
        # Check if employee exists
        existing = self.db.get_employee_by_code(employee_code)
        if not existing:
            return False, f"Employee with code {employee_code} not found"
        
        try:
            success = self.db.update_employee(employee_code, employee_data)
            if success:
                return True, f"Employee {employee_code} updated successfully"
            return False, f"Failed to update employee {employee_code}"
        except Exception as e:
            return False, f"Error updating employee: {str(e)}"
    
    def delete_employee(self, employee_code):
        """Delete employee record"""
        if not employee_code or not employee_code.strip():
            return False, "Employee code is required"
        
        try:
            success = self.db.delete_employee(employee_code)
            if success:
                return True, f"Employee {employee_code} deleted successfully"
            return False, f"Employee {employee_code} not found"
        except Exception as e:
            return False, f"Error deleting employee: {str(e)}"
    
    def search_employees(self, search_term="", search_by="all"):
        """Search for employees"""
        return self.db.search_employee(search_term, search_by)
    
    def get_employee_by_code(self, employee_code):
        """Get single employee by code"""
        return self.db.get_employee_by_code(employee_code)
    
    def get_all_employees(self):
        """Get all employees"""
        return self.db.get_all_employees()
    
    def calculate_net_salary(self, basic_salary, allowances, deductions, overtime_hours, bonus):
        """Calculate net salary"""
        try:
            basic = float(basic_salary or 0)
            allowance = float(allowances or 0)
            deduction = float(deductions or 0)
            overtime = float(overtime_hours or 0)
            bonus_amt = float(bonus or 0)
            
            # Calculate overtime (assuming 1.5x rate)
            # Hourly rate = basic salary / (8 hours/day * 22 days/month)
            hourly_rate = basic / (8 * 22) if basic > 0 else 0
            overtime_pay = overtime * hourly_rate * 1.5
            
            net_salary = basic + allowance - deduction + overtime_pay + bonus_amt
            return round(max(net_salary, 0), 2)  # Ensure non-negative
        except (ValueError, TypeError):
            return 0.0
    
    def calculate_monthly_salary(self, basic_salary, total_days, absent_days, medical, pf):
        """Calculate monthly salary based on attendance"""
        try:
            basic = float(basic_salary or 0)
            total = float(total_days or 0)
            absent = float(absent_days or 0)
            med = float(medical or 0)
            pf_amount = float(pf or 0)
            
            if total <= 0:
                return 0.0
            
            if absent > total:
                absent = total
            
            daily_rate = basic / total
            salary_for_days = (total - absent) * daily_rate
            net_salary = salary_for_days - med - pf_amount
            
            return round(max(net_salary, 0), 2)  # Ensure non-negative
        except (ValueError, TypeError):
            return 0.0