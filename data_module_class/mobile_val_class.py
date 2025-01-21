import logging
import os
from logging_config import configure_logging

class MobileValidator:
    def __init__(self, user):
        self.user = user
        log_folder = "D:\\Bizmetric Intership\\logs"
        os.makedirs(log_folder, exist_ok=True)
        log_file_name = os.path.join(log_folder, f"login Id_\'\'{self.user}\'\'_mobile_validation.log")
        self.logger = configure_logging(log_file_name)

    def validate_mobile(self, mobile):
        if mobile is None:
            self.logger.error("Validation failed: mobile number cannot be None")
            raise TypeError("Mobile number cannot be None")
        if not isinstance(mobile, str):
            self.logger.error("Validation failed: mobile number must be a string")
            raise ValueError("Mobile number must be a string")
        if not mobile.isdigit():
            self.logger.error("Validation failed: mobile number must contain only digits")
            raise TypeError("Mobile number must contain only digits")
        if len(mobile) != 10:
            self.logger.error("Validation failed: mobile number must be 10 digits long")
            raise TypeError("Mobile number must be 10 digits long")
        self.logger.info("Validation successful: mobile number is valid")
        return mobile

    def test_mobile_validation(self, mobile):
        try:
            validated_mobile = self.validate_mobile(mobile)
            print(f"'{mobile}' is valid")
        except (ValueError, TypeError) as err:
            print(f"'{mobile}' is invalid: {err}")

if __name__ == "__main__":
    user = input("User Name or User ID:->")
    validator = MobileValidator(user)
    mobile = input("Enter your mobile number: ").strip()
    validator.test_mobile_validation(mobile)