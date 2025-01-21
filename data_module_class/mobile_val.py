import logging

# Configure logging
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# File handler
file_handler = logging.FileHandler('mobile_validation.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# Add handlers to the logger
logger.addHandler(file_handler)
logger.addHandler(console_handler)

def validate_mobile(mobile):
    if mobile is None:
        logger.error("Validation failed: mobile number cannot be None")
        raise ValueError("mobile number cannot be None")
    elif not isinstance(mobile, str):
        logger.error("Validation failed: mobile number must be a string")
        raise ValueError("mobile number must be a string")
    elif not mobile.isdigit():
        logger.error("Validation failed: mobile number must contain only digits")
        raise ValueError("mobile number must contain only digits")
    elif len(mobile) != 10:
        logger.error("Validation failed: mobile number must be 10 digits long")
        raise ValueError("mobile number must be 10 digits long")
    logger.info("Validation successful: mobile number is valid")
    return mobile

def test_mobile_validation(mobile_numbers):
    for mobile in mobile_numbers:
        try:
            validate_mobile(mobile)
            print(f"'{mobile}' is valid")
        except ValueError as e:
            print(f"'{mobile}' is invalid: {e}")

# Function call
mobile_numbers = input("Enter your mobile numbers separated by spaces: ").strip().split()
test_mobile_validation(mobile_numbers)