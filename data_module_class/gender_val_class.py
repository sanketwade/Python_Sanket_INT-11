import logging
import os
from logging_config import configure_logging

class GenderValidator:
    def __init__(self, user):
        self.user = user
        log_folder = "D:\\Bizmetric Intership\\logs"
        os.makedirs(log_folder, exist_ok=True)
        log_file_name = os.path.join(log_folder, f"login Id_\'\'{self.user}_gender_validation.log")
        self.logger = configure_logging(log_file_name)

    def validate_gender(self, gender):
        try:
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
            return full_gender
        except (ValueError, TypeError) as e:
            self.logger.exception(f"Exception occurred: {e}")
            return None

    def test_gender_validation(self, gender):
        full_gender = self.validate_gender(gender)
        if full_gender:
            print(f"'{gender}' is valid and corresponds to {full_gender}")
        else:
            print(f"'{gender}' is invalid")

if __name__ == "__main__":
    user = input("User Name or User ID:->")
    validator = GenderValidator(user)
    gender = input("Enter gender (M for male, F for female, O for others): ").strip()
    validator.test_gender_validation(gender)