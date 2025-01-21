from logging_config import configure_logging
from datetime import datetime
import logging

# Ensure logging is configured

def validate_date(date_str):
    if not date_str or not isinstance(date_str, str):
        logging.error(f"Validation failed: {date_str} is not a valid string.")
        raise ValueError("Date must be a non-empty string.")
    
    try:
        date_obj = datetime.strptime(date_str, '%d-%m-%Y')
    except ValueError:
        try:
            date_obj = datetime.strptime(date_str, '%d/%m/%Y')
        except ValueError:
            logging.error(f"Validation failed: {date_str} is not a valid date format.")
            raise ValueError("Date format must be DD-MM-YYYY or DD/MM/YYYY.")
    
    formatted_date = date_obj.strftime('%d-%m-%Y')
    logging.info(f"Validation successful: '{date_str}' is a valid date, converted to '{formatted_date}'")
    return formatted_date

def test_date_validation(dates):
    for date_str in dates:
        try:
            formatted_date = validate_date(date_str)
            print(f"'{date_str}' is valid and converted to '{formatted_date}'")
        except ValueError as e:
            print(f"'{date_str}' is invalid: {e}")

# Example usage
dates = input("Enter date of birth (formats DD-MM-YYYY and DD/MM/YYYY): ").strip().split()
test_date_validation(dates)
