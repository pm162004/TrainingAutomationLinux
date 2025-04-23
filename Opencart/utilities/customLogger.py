import logging
import os


class LogGen():
    @staticmethod
    def loggen():
        path = "/home/web-h-028/PycharmProjects/TrainingAutomation/Opencart/utilities/logs/automation.log"

        # Make sure the log directory exists
        os.makedirs(os.path.dirname(path), exist_ok=True)

        # Create logger
        logger = logging.getLogger("SimpleLogger")
        logger.setLevel(logging.DEBUG)

        # Avoid adding multiple handlers
        if not logger.handlers:
            # File handler
            file_handler = logging.FileHandler(path)
            # Console handler
            console_handler = logging.StreamHandler()

            # Format for logs
            formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

            file_handler.setFormatter(formatter)
            console_handler.setFormatter(formatter)

            # Add handlers to logger
            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

        return logger
