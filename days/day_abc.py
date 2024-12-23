import abc
import logging
from datetime import datetime


class AbsDay(abc.ABC):
    @property
    def logger(self):
        return logging.getLogger("advent_of_code_2024")
    
    @abc.abstractmethod
    def run(self):
        pass

    def __init__(self):
        start_time = datetime.now()
        self.logger.info(f"New day starting at {start_time}")
        self.run()
        end_time = datetime.now()
        self.logger.info(f"Finished at {end_time} - time spent: {end_time - start_time}")
        self.logger.info("--------------------")
