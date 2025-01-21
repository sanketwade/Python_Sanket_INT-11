import os
from logging_config import configure_logging

class TwelthMarksValidator:
    def __init__(self, user):
        self.user = user
        log_folder = "D:\\Bizmetric Intership\\logs"
        os.makedirs(log_folder, exist_ok=True)
        log_file_name = os.path.join(log_folder, f"login Id_\'\'{self.user}\'\'_twelth_mark_validation.log")
        self.logger = configure_logging(log_file_name)

    def validate_twelth_percentage(self, percentage):
        try:
            if percentage is None:
                self.logger.error("Validation failed: percentage cannot be None")
                raise ValueError("Percentage cannot be None")
            if not isinstance(percentage, (int, float)):
                self.logger.error("Validation failed: percentage must be a number")
                raise TypeError("Percentage must be a number")
            if percentage < 40:
                self.logger.error(f"Validation failed: '{percentage}' is not within the valid range (40-100)")
                raise ValueError(f"Not Eligible, your {percentage}% is less than 40%")
            if percentage > 100:
                self.logger.error(f"Validation failed: '{percentage}' is not within the valid range (40-100)")
                raise TypeError(f"{percentage}% is a wrong percentage, it should be under 100%")
            if isinstance(percentage, float) and len(str(percentage).split('.')[1]) > 2:
                self.logger.error(f"Validation failed: '{percentage}' has more than two decimal places")
                raise ValueError("Percentage cannot have more than two decimal places")
            
            self.logger.info(f"Validation successful: '{percentage}' is a valid percentage")
            return True
        except (ValueError, TypeError) as err:
            self.logger.exception(f"Exception occurred: {err}")
            return False

if __name__ == "__main__":
    user = input("User Name or User ID:->")
    validator = TwelthMarksValidator(user)
    percentage_input = float(input("Enter your percentage: ").strip())
    if validator.validate_twelth_percentage(percentage_input):
        print(f"'{percentage_input}' is valid")
    else:
        print(f"'{percentage_input}' is invalid")