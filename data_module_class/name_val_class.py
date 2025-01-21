import os
import re
from logging_config import configure_logging

class NameValidator:
    def __init__(self, user):
        self.user = user
        log_folder = "D:\\Bizmetric Intership\\logs"
        os.makedirs(log_folder, exist_ok=True)
        log_file_name = os.path.join(log_folder, f"login Id_\'\'{self.user}\'\'name_validation.log")
        self.logger = configure_logging(log_file_name)

    def validate_name(self, name):
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
        
        self.logger.info("Validation successful: name is valid")
        return name.title()

    def test_name_validation(self, name):
        try:
            validated_name = self.validate_name(name)
            print(f"'{name}' is valid")
            print(f"Hello, {validated_name}!")
        except (ValueError, TypeError) as err:
            print(f"'{name}' is invalid: {err}")

if __name__ == "__main__":
    user = input("User Name or User ID:->")
    validator = NameValidator(user)
    name = input("Enter your name: ").strip()
    validator.test_name_validation(name)