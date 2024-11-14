import logging
import os

class Logger:
    def __init__(self, level="INFO"):
        
        # Verifying the existance of the logs directory
        d_logs = os.path.join(os.path.dirname(__file__), "../logs")
        os.makedirs(d_logs, exist_ok=True)

        # Logger configuration
        self.logger = logging.getLogger("PokeApp - Logger")
        self.logger.setLevel(level)

        # Format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

        # Stream Handler
        c_handler = logging.StreamHandler()
        #formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        c_handler.setFormatter(formatter)
        self.logger.addHandler(c_handler)

        # File Handler
        log_path = os.path.join(d_logs, "poke.log")
        f_handler = logging.FileHandler(log_path, mode="a")
        f_handler.setFormatter(formatter)
        self.logger.addHandler(f_handler)

    def log(self, level, message):
        if level == "INFO":
            self.logger.info(message)
        elif level == "ERROR":
            self.logger.error(message)
        elif level == "WARNING":
            self.logger.warning(message)
