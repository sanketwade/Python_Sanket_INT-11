import logging
import os
import re
from logging_config import configure_logging

class EmailValidator:
    def __init__(self, user):
        self.user = user
        log_folder = "D:\\Bizmetric Intership\\logs"
        os.makedirs(log_folder, exist_ok=True)
        log_file_name = os.path.join(log_folder, f"login Id_\'\'{self.user}_email_validation.log")
        self.logger = configure_logging(log_file_name)

    def validate_email(self, email):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
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
        return email.lower()

    def test_email_validation(self, email):
        try:
            validated_email = self.validate_email(email)
            print(f"'{email}' is valid")
        except (ValueError, TypeError) as err:
            print(f"'{email}' is invalid: {err}")

if __name__ == "__main__":
    user = input("User Name or User ID:->")
    validator = EmailValidator(user)
    email = input("Enter your email: ").strip()
    validator.test_email_validation(email)