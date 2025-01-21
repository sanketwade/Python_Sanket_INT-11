###-----Import this function in other scripts to configure logging------#
# from logging_config import configure_logging

# # User-defined log file name
# log_file_name = 'gender_validation.log'
# logger = configure_logging(log_file_name)


import logging

def configure_logging(log_file_name):
    """###-----Import this function in other scripts to configure logging------#
                # from logging_config import configure_logging

                # # User-defined log file name
                # log_file_name = 'gender_validation.log'
                # logger = configure_logging(log_file_name)"""

    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # File handler
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger