from logging_config import configure_logging
log_file_name = "tenth_marks_validation.log"
logger = configure_logging(log_file_name)


def validate_tenth_percentage(percentage):
    try:
        if percentage is None:
            logger.error("Validation failed: percentage cannot be None")
            raise ValueError("percentage cannot be None")
        elif not isinstance(percentage, (int, float)):
            logger.error("Validation failed: percentage must be a number")
            raise TypeError("percentage must be a number")
        elif percentage < 40:
            logger.error(f"Validation failed: '{percentage}' is not within the valid range (40-100)")
            raise ValueError(f"Not Eligible your {percentage}% less than 40%")
        elif percentage > 100:
            logger.error(f"Validation failed: '{percentage}' is not within the valid range (40-100)")
            raise TypeError(f" {percentage}% Wrong Percentage it's under 100%")

        elif isinstance(percentage, float) and len(str(percentage).split('.')[1]) > 2:
            logger.error(f"Validation failed: '{percentage}' has more than two decimal places")
            raise ValueError("percentage cannot have more than two decimal places")
        
        logger.info(f"Validation successful: '{percentage}' is a valid percentage")
        return True
    except (ValueError, TypeError) as e:
        logger.exception(f"Exception occurred: {e}")
        return False

def percentage_validation(percentages):
    for percentage in percentages:
        if validate_tenth_percentage(percentage):
            print(f"'{percentage}' is valid")
        else:
            print(f"'{percentage}' is invalid")


percentages_input = input("Enter percentages: ").strip().split()
percentages_list = [float(percentage) for percentage in percentages_input]
percentage_validation(percentages_list)