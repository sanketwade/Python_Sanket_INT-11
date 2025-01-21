from logging_config import configure_logging
from datetime import datetime
import logging
import os

class DOBValidator:
    def __init__(self, user):
        self.user = user
        log_folder = "D:\\Bizmetric Intership\\logs"
        os.makedirs(log_folder, exist_ok=True)
        log_file_name = os.path.join(log_folder, f"login Id_\'\'{self.user}\'\'_dob_validation.log")
        self.logger = configure_logging(log_file_name)

    def validate_date(self, date_str):
        if not date_str or not isinstance(date_str, str):
            self.logger.error(f"Validation failed: {date_str} is not a valid string.")
            raise ValueError("Date must be a non-empty string.")
        
        try:
            date_obj = datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            try:
                date_obj = datetime.strptime(date_str, '%d/%m/%Y')
            except ValueError:
                self.logger.error(f"Validation failed: {date_str} is not a valid date format.")
                raise ValueError("Date format must be DD-MM-YYYY or DD/MM/YYYY.")
        
        formatted_date = date_obj.strftime('%d-%m-%Y')
        self.logger.info(f"Validation successful: '{date_str}' is a valid date, converted to '{formatted_date}'")
        return formatted_date

    def test_date_validation(self, date_str):
        try:
            formatted_date = self.validate_date(date_str)
            print(f"'{date_str}' is valid, converted to '{formatted_date}'")
        except ValueError as err:
            print(f"'{date_str}' is invalid: {err}")

if __name__ == "__main__":
    user = input("User Name or User ID:->")
    validator = DOBValidator(user)
    date_str = input("Enter your DOB in DD-MM-YYYY or DD/MM/YYYY: ").strip()
    validator.test_date_validation(date_str)