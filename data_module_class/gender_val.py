# import logging

# # Configure logging
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# # File handler
# file_handler = logging.FileHandler('gender_validation.log')
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# # Console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

# # Add handlers to the logger
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)

from logging_config import configure_logging
login_file_name = ("gender_validation.log")
logger = configure_logging(login_file_name)


def validate_gender(gender):
    try:
        if gender is None:
            logger.error("Validation failed: gender cannot be None")
            raise ValueError("gender cannot be None")
        elif not isinstance(gender, str):
            logger.error("Validation failed: gender must be a string")
            raise TypeError("gender must be a string")
        elif gender.strip() == "":
            logger.error("Validation failed: gender cannot be empty or whitespace")
            raise ValueError("gender cannot be empty or whitespace")
        
        
        valid_genders = {
            'M': 'Male', 'F': 'Female', 'O': 'Other',
            'MALE': 'Male', 'FEMALE': 'Female', 'OTHER': 'Other'
        }
        
        gender_upper = gender.upper()
        if gender_upper not in valid_genders:
            logger.error(f"Validation failed: '{gender}' is not a valid gender")
            raise ValueError("gender must be 'M', 'F', 'O', 'Male', 'Female', or 'Other'")
        
        full_gender = valid_genders[gender_upper]
        logger.info(f"Validation successful: '{gender}' is a valid gender ({full_gender})")
        return full_gender
    except (ValueError, TypeError) as e:
        logger.exception(f"Exception occurred: {e}")
        return None

def test_gender_validation(genders):
    for gender in genders:
        full_gender = validate_gender(gender)
        if full_gender:
            print(f"'{gender}' is valid and corresponds to {full_gender}")
        else:
            print(f"'{gender}' is invalid")

# Function call
genders = input("Enter genders (M for male, F for female, O for others): ").strip().split()
test_gender_validation(genders)