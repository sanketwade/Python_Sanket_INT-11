from logging_config import configure_logging
log_file_name = 'name_validation.log'
logger = configure_logging(log_file_name)

def validate_name(name):
    if name is None:
        logger.error("Validation failed: name cannot be None")
        raise ValueError("name cannot be None")
    elif not isinstance(name, str):
        logger.error("Validation failed: name must be a string")
        raise ValueError("name must be a string")
    elif len(name) < 2:
        logger.error("Validation failed: name must have at least two characters")
        raise ValueError("name must have at least two characters")
    elif not name.isalpha():
        logger.error("Validation failed: name must be alphabetic")
        raise TypeError("name must be alphabetic")
    else:
        logger.info("Validation successful: name is valid")
        first_name = name.title()
    return first_name

print("_________________________________________________________")

# # Configure logging
# logger = logging.getLogger()
# logger.setLevel(logging.INFO)

# # File handler
# file_handler = logging.FileHandler('name_validation.log')
# file_handler.setLevel(logging.INFO)
# file_handler.setFormatter(logging.Formatter('%(asctiime)s:%(levelname)s - %(message)s'))

# # Console handler
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)
# console_handler.setFormatter(logging.Formatter('%(asctiime)s:%(levelname)s - %(message)s'))

# # Add handlers to the logger
# logger.addHandler(file_handler)
# logger.addHandler(console_handler)

print("_____________________________________________________________________")

name = input("Enter your name: ").strip()
try:
    validate_name(name)
    print("Name is valid")
    print(f"Hello, {name}!") #uncomment this line to print the name
except (ValueError, TypeError) as err:
    print(err)
    print("Name is invalid")

