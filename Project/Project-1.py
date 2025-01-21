import logging
import re
import os

# Function to create logger with the user's name and specified log folder
def create_logger(username, log_folder='D:\\Bizmetric Intership\\project_log'):
    if not os.path.exists(log_folder):
        os.makedirs(log_folder)
    log_file_path = os.path.join(log_folder, f'{username}.log')
    logger = logging.getLogger(username)
    logger.setLevel(logging.INFO)
    
    # File handler
    fh = logging.FileHandler(log_file_path)
    fh.setLevel(logging.INFO)
    formatter = logging.Formatter(f'%(asctime)s - %(levelname)s - {username} - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    
    # Stream handler (console)
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    
    logger.info(f"Logger created for user '{username}' with log file at '{log_file_path}'")
    return logger

class CollegeAdmission:
    def __init__(self, logger):
        self.logger = logger
        self.students = []
        self.admins = []
        self.course_choices = []
        self.departments = []
        
    def validate_student(self, name, email, mobile_no, gender, dob, marks10th, marks12th):
        try:
            # Name validation
            if name is None:
                self.logger.error("Validation failed: name cannot be None")
                raise TypeError("Name cannot be None")
            if not isinstance(name, str):
                self.logger.error("Validation failed: name must be a string")
                raise TypeError("Name must be a string")
            if len(name) < 2:
                self.logger.error("Validation failed: name must have at least two characters")
                raise ValueError("Name must have at least two characters")
            if not re.match(r'^[a-zA-Z]+ [a-zA-Z]+$', name):
                self.logger.error("Validation failed: name must contain first name and last name separated by a space")
                raise ValueError("Name must contain first name and last name separated by a space")
            
            # Email validation
            email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            email_regexes = r"^[a-zA-Z_0-9.]{1,25}[@][gmail]{5}[.][com]{3}$"
            
            if email is None:
                self.logger.error(f"Validation failed: {email} email cannot be None")
                raise TypeError("Email cannot be None")
            
            if len(email) < 6:
                self.logger.error(f"Validation failed: {email} email must have at least 6 characters")
                raise ValueError("Email must have at least 6 characters")
            
            if "@" not in email:
                self.logger.error(f"Validation failed: {email} email must contain @")
                raise TypeError("Email must contain @")
            
            if "." not in email:
                self.logger.error(f"Validation failed: {email} email must contain .")
                raise TypeError("Email must contain .")
            
            if email.startswith("@"):
                self.logger.error(f"Validation failed: {email} email cannot start with @")
                raise TypeError("Email cannot start with @")
            
            if email.endswith("@"):
                self.logger.error(f"Validation failed: {email} email cannot end with @")
                raise TypeError("Email cannot end with @")
            
            if email.startswith("."):
                self.logger.error(f"Validation failed: {email} email cannot start with .")
                raise ValueError("Email cannot start with .")
            
            if email.endswith("."):
                self.logger.error(f"Validation failed: {email} email cannot end with .")
                raise TypeError("Email cannot end with .")
            
            if email.count("@") > 1:
                self.logger.error(f"Validation failed: {email} email cannot contain more than one @")
                raise TypeError("Email cannot contain more than one @")
            
            if email.count(".") > 1:
                self.logger.error(f"Validation failed: {email} email cannot contain more than one .")
                raise TypeError("Email cannot contain more than one .")
            
            if email.count(" ") > 0:
                self.logger.error(f"Validation failed: {email} email cannot contain spaces")
                raise ValueError("Email cannot contain spaces")
            
            if not re.match(email_regex, email):
                self.logger.error(f"Validation failed: {email} email is not valid")
                raise ValueError("Email is not valid")
            
            if not re.match(email_regexes, email):
                self.logger.error(f"Validation failed: {email} email is not valid")
                raise ValueError("Email is not valid")

            self.logger.info(f"Validation successful: {email} email is valid")

            # Mobile number validation
            if mobile_no is None:
                self.logger.error("Validation failed: mobile_no number cannot be None")
                raise TypeError("Mobile number cannot be None")
            if not isinstance(mobile_no, str):
                self.logger.error("Validation failed: mobile_no number must be a string")
                raise ValueError("Mobile number must be a string")
            if not mobile_no.isdigit():
                self.logger.error("Validation failed: mobile_no number must contain only digits")
                raise TypeError("Mobile number must contain only digits")
            if len(mobile_no) != 10:
                self.logger.error("Validation failed: mobile_no number must be 10 digits long")
                raise TypeError("Mobile number must be 10 digits long")
            self.logger.info("Validation successful: mobile number is valid")
                
            # Gender validation
            if gender is None:
                self.logger.error("Validation failed: gender cannot be None")
                raise ValueError("Gender cannot be None")
            if not isinstance(gender, str):
                self.logger.error("Validation failed: gender must be a string")
                raise TypeError("Gender must be a string")
            if gender.strip() == "":
                self.logger.error("Validation failed: gender cannot be empty or whitespace")
                raise ValueError("Gender cannot be empty or whitespace")
            
            valid_genders = {
                'M': 'Male', 'F': 'Female', 'O': 'Other',
                'MALE': 'Male', 'FEMALE': 'Female', 'OTHER': 'Other'
            }
            
            gender_upper = gender.upper()
            if gender_upper not in valid_genders:
                self.logger.error(f"Validation failed: '{gender}' is not a valid gender")
                raise ValueError("Gender must be 'M', 'F', 'O', 'Male', 'Female', or 'Other'")
            
            full_gender = valid_genders[gender_upper]
            self.logger.info(f"Validation successful: '{gender}' is a valid gender ({full_gender})")


            # Date of birth validation
            if not re.match(r"\d{2}[-/]\d{2}[-/]\d{4}", dob):
                raise ValueError("Date of birth must be in DD-MM-YYYY or DD/MM/YYYY format")
            day, month, year = map(int, re.split('[-/]', dob))
            if not (1950 <= year <= 2012):
                raise ValueError("Year of birth must be between 1950 and 2012")
            if not (1 <= month <= 12):
                raise ValueError("Month of birth must be between 1 and 12")
            if not (1 <= day <= 31):
                raise ValueError("Day of birth must be between 1 and 31")
            
            # 10 Marks validation
            if not (0 <= marks10th <= 100):
                raise ValueError("10th marks must be between 0 and 100")
            if marks10th is None:
                self.logger.error("Validation failed: marks10th cannot be None")
                raise ValueError("Percentage cannot be None")
            if not isinstance(marks10th, (int, float)):
                self.logger.error("Validation failed: marks10th must be a number")
                raise TypeError("Percentage must be a number")
            if isinstance(marks10th, float) and len(str(marks10th).split('.')[1]) > 2:
                self.logger.error(f"Validation failed: '{marks10th}' has more than two decimal places")
                raise ValueError("Percentage cannot have more than two decimal places")
            
            # 12 Marks validation
            if not (0 <= marks12th <= 100):
                raise ValueError("12th marks must be between 0 and 100")
            if marks12th is None:
                self.logger.error("Validation failed: marks12th cannot be None")
                raise ValueError("Percentage cannot be None")
            if not isinstance(marks12th, (int, float)):
                self.logger.error("Validation failed: marks12th must be a number")
                raise TypeError("Percentage must be a number")
            if marks12th < 40:
                self.logger.error(f"Validation failed: '{marks12th} is not within the valid range (40-100)")
                raise ValueError(f"Not Eligible, your {marks12th}% is less than 40%")
            if marks12th > 100:
                self.logger.error(f"Validation failed: '{marks12th}' is not within the valid range (40-100)")
                raise TypeError(f"{marks12th}% is a wrong marks12th, it should be under 100%")
            if isinstance(marks12th, float) and len(str(marks12th).split('.')[1]) > 2:
                self.logger.error(f"Validation failed: '{marks12th}' has more than two decimal places")
                raise ValueError("Percentage cannot have more than two decimal places")
            
            self.logger.info("Student validation successful")
            return True
        except (ValueError, TypeError) as err:
            self.logger.error(f"Validation error: {err}")
            return False
            
    def add_student(self, name, email, mobile_no, address, gender, dob, marks10th, marks12th):
        if self.validate_student(name, email, mobile_no, gender, dob, marks10th, marks12th):
            student_id = len(self.students) + 1
            student = {
                'StudentID': student_id,
                'Name': name,
                'Email': email,
                'MobileNo': mobile_no,
                'Address': address,
                'Gender': gender,
                'DOB': dob,
                'Marks10th': marks10th,
                'Marks12th': marks12th
            }
            self.students.append(student)
            self.logger.info(f"Student added: {student}")
            print(f"Student added: {student}")
        else:
            self.logger.error("Failed to add student due to validation errors")
    
    def allocate_seat(self, student_id, course_preferences):
        valid_departments = [
            'Civil Engineering', 
            'Information Technology', 
            'Electrical Engineering', 
            'Computer Engineering', 
            'Mechanical Engineering', 
            'Electronics Engineering'
        ]
        student = next((s for s in self.students if s['StudentID'] == student_id), None)
        if student:
            avg_marks = (student['Marks10th'] + student['Marks12th']) / 2
            if avg_marks >= 55:
                for course_name in course_preferences:
                    if course_name in valid_departments:
                        dept = next((dept for dept in self.departments if dept['DepartmentName'] == course_name), None)
                        if dept and dept['AllocatedSeat'] == 'No':
                            dept['AllocatedSeat'] = 'Yes'
                            self.logger.info(f"Seat allocated to student {student_id} in {course_name}")
                            print(f"Seat allocated to student {student_id} in {course_name}")
                            return
                        else:
                            self.logger.warning(f"No available seats in {course_name} department")
                    else:
                        self.logger.error(f"Invalid department: {course_name}")
                self.logger.warning(f"Student {student_id} does not meet the marks criteria for seat allocation")
                print(f"Student {student_id} does not meet the marks criteria for seat allocation")
            else:
                self.logger.warning(f"Student {student_id} does not meet the marks criteria for seat allocation")
                print(f"Student {student_id} does not meet the marks criteria for seat allocation")
        else:
            self.logger.error(f"Student ID {student_id} not found")
            print(f"Student ID {student_id} not found")
    
    def add_department(self, department_name):
        dept_id = len(self.departments) + 1
        department = {
            'DeptId': dept_id,
            'DepartmentName': department_name,
            'AllocatedSeat': 'No'
        }
        self.departments.append(department)
        self.logger.info(f"Department added: {department}")
        print(f"Department added: {department}")

def get_user_input():
    username = input("Enter your username: ")
    logger = create_logger(username)
    
    name = input("Enter student name First_Name Last Name: ")
    email = input("Enter student email: ")
    mobile_no = input("Enter mobile number: ")
    address = input("Enter address: ")
    gender = input("Enter gender (Male/Female/Other): ")
    dob = input("Enter date of birth (DD-MM-YYYY or DD/MM/YYYY): ")
    marks10th = float(input("Enter 10th marks (0-100): "))
    marks12th = float(input("Enter 12th marks (0-100): "))
    
    courses = {
        1: 'Civil Engineering',
        2: 'Information Technology',
        3: 'Electrical Engineering',
        4: 'Computer Engineering',
        5: 'Mechanical Engineering',
        6: 'Electronics Engineering'
    }
    
    print("Available courses:")
    for key, value in courses.items():
        print(f"{key}: {value}")

   #print(" 1: 'Civil Engineering', \n2: 'Information Technology', \n3: 'Electrical Engineering', \n4: 'Computer Engineering' \n5: 'Mechanical Engineering' \n6: 'Electronics Engineering'")
    course_choices = input("Enter the numbers corresponding to your preferred courses, separated by commas: ").split(",")
    course_preferences = [courses[int(choice.strip())] for choice in course_choices if int(choice.strip()) in courses]
    
    return username, logger, name, email, mobile_no, address, gender, dob, marks10th, marks12th, course_preferences

# Example usage:
if __name__ == "__main__":
    username, logger, name, email, mobile_no, address, gender, dob, marks10th, marks12th, course_preferences = get_user_input()
    college = CollegeAdmission(logger)
    college.add_student(name, email, mobile_no, address, gender, dob, marks10th, marks12th)

    departments = [
        'Civil Engineering', 
        'Information Technology', 
        'Electrical Engineering', 
        'Computer Engineering', 
        'Mechanical Engineering', 
        'Electronics Engineering'
    ]
    for dept in departments:
        college.add_department(dept)

    # Allocate seat to the first student based on their course choice and marks
    college.allocate_seat(1, course_preferences)