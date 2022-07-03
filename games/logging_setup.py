"""Module defining the logging configuration of the application."""

# Standard library imports
from datetime import datetime
import logging
from pathlib import Path

# Local application imports
from games.all_game_constants.root_directory import ROOT_DIRECTORY


class LogConfiguration:

    def __init__(self,
                 log_file_name: str,
                 logging_path: Path = ROOT_DIRECTORY / "data" / "logging_data"):
        self.log_file_name = log_file_name
        self.logging_path = logging_path

    def logging_set_up(self) -> None:
        """Method to be called in order to initiate the logger."""
        logging_data_path = self.create_time_dependent_log_directory()
        logging.basicConfig(level=logging.INFO,
                            format='%(asctime)s %(levelname)s %(message)s',
                            datefmt='%Y-%m-%d %H:%M:%S',
                            filename=logging_data_path / self.log_file_name,
                            filemode="w")

    def create_time_dependent_log_directory(self) -> Path:
        """Method for creating the directory (and it's parents) for where the logging data will be saved."""
        time_dependent_end_directory = datetime.now().strftime("%Y_%m_%d_%H_%M")
        logging_data_path: Path = self.logging_path / time_dependent_end_directory
        if not logging_data_path.exists():
            logging_data_path.mkdir(parents=True)
        return logging_data_path
