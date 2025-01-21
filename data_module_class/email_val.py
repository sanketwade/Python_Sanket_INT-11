import logging.config
import os
import re



def validate_email(email):
    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler('email_validation.log')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)


    email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    email_regexes = r"^[a-zA-Z_0-9.]{1,25}[@][gmail]{5}[.][com]{3}$"
    if email == None:
        logging.error(f"Validation failed:{email} email cannot be None")
        raise ValueError("email can not be None")
    
    elif len(email) < 6:
        logging.error(f"Validation failed:{email} email must have at least 6 characters",)
        raise ValueError("email must have at least 6 characters")
    
    elif not "@" in email:
        logging.error(f"Validation failed:{email} email must contain @")
        raise ValueError("email must contain @")
    
    elif not "." in email:
        logging.error(f"Validation failed:{email} email must contain .")
        raise ValueError("email must contain .")
    
    elif email.startswith("@"):
        logging.error(f"Validation failed:{email} email can not start with @")
        raise ValueError("email can not start with @")
    elif email.endswith("@"):
        logging.error(f"Validation failed:{email} email can not end with @")    
        raise ValueError("email can not end with @")
    elif email.startswith("."):
        logging.error(f"Validation failed:{email} email can not start with .")
        raise ValueError("email can not start with .")
    elif email.endswith("."):
        logging.error(f"Validation failed:{email} email can not end with .")
        raise ValueError("email can not end with .")
    elif email.count("@") > 1:
        logging.error(f"Validation failed:{email} email can not contain more than one @")  
        raise ValueError("email can not contain more than one @")
    elif email.count(".") > 1:
        logging.error(f"Validation failed:{email} email can not contain more than one .")
        raise ValueError("email can not contain more than one .")
    elif email.count("@") < 1:
        logging.error(f"Validation failed:{email} email must contain @")
        raise ValueError("email must contain @") 
    elif email.count(".") < 1:
        logging.error(f"Validation failed:{email} email must contain .")
        raise ValueError("email must contain .")
    elif email.count(" ") > 0:
        logging.error(f"Validation failed:{email} email can not contain spaces")
        raise ValueError("email can not contain spaces")
    elif not re.match(email_regex, email):
        logging.error(f"Validation failed:{email} email is not valid")
        raise ValueError("email is not valid")
    elif not re.match(email_regexes, email):
        logging.error(f"Validation failed:{email} email is not valid")
        raise ValueError("email is not valid")

    else:
        logging.info(f"Validation successful:{email} email is valid")
        return email.lower()
    

def test_email_validation(test_emails):
    for email in test_emails:
        try:
            validate_email(email)
            print(f"'{email}' is valid")
        except ValueError as e:
            print(f"'{email}' is invalid: {e}")
    return "".join(test_emails).lower()

# Function call
test_emails = input("Enter your emails separated by spaces: ").strip().split()
test_email_validation(test_emails)
print("_____________________________________________________________________")

