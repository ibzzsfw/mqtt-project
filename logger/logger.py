import logging


class Logger:
    """
    A standardized logger class that reducing redundancy, 
    simplifying the debugging process, and ensuring consistency. 

    Any class that needs to log information can extend this class to gain necessary logging functions.
    """

    def __init__(self, name):
        self.name = name  # name of the logger
        self.logger = logging.getLogger(self.name)  # create a logger
        self.logger.setLevel(logging.DEBUG)  # set the level of the logger
        fh = logging.FileHandler(self.name+'.log')  # create a file handler
        fh.setLevel(logging.DEBUG)  # set the level of the file handler
        ch = logging.StreamHandler()  # create a console handler
        ch.setLevel(logging.DEBUG)  # set the level of the console handler
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # create a formatter
        fh.setFormatter(formatter)  # set the formatter of the file handler
        ch.setFormatter(formatter)  # set the formatter of the console handler
        self.logger.addHandler(fh)  # add the file handler to the logger
        self.logger.addHandler(ch)  # add the console handler to the logger

    def info(self, msg):
        self.logger.info(msg)

    def debug(self, msg):
        self.logger.debug(msg)

    def warning(self, msg):
        self.logger.warning(msg)

    def error(self, msg):
        self.logger.error(msg)

    def critical(self, msg):
        self.logger.critical(msg)
