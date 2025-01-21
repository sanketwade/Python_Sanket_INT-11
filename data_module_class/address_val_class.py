import logging
import re
import os
from logging_config import configure_logging

class AddressValidator:
    def __init__(self, user):
        self.user = user
        log_folder = "D:\\Bizmetric Intership\\logs"
        os.makedirs(log_folder, exist_ok=True)
        log_file_name = os.path.join(log_folder, f"login Id_\'\'{self.user}\'\'_address_validation.log")
        self.logger = configure_logging(log_file_name)

    def validate_address(self, address):
        try:
            if address is None:
                self.logger.error("Validation failed: address cannot be None")
                raise ValueError("Address cannot be None")
            if not isinstance(address, str):
                self.logger.error("Validation failed: address must be a string")
                raise ValueError("Address must be a string")
            if len(address) < 10:
                self.logger.error("Validation failed: address must have at least 10 characters")
                raise ValueError("Address must have at least 10 characters")
            if not re.match(r'^[a-zA-Z0-9\s,.-]+$', address):
                self.logger.error("Validation failed: address contains invalid characters")
                raise ValueError("Address contains invalid characters")
            self.logger.info("Validation successful: address is valid")
            return True
        except ValueError as err:
            self.logger.exception(f"Exception occurred: {err}")
            return False

    def test_address_validation(self, address):
        if self.validate_address(address):
            print(f"'{address}' is valid")
        else:
            print(f"'{address}' is invalid")

if __name__ == "__main__":
    user = input("User Name or User ID")
    validator = AddressValidator(user)
    address = input("Enter your address: ").strip()
    validator.test_address_validation(address)