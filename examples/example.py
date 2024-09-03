# -
# Imports only for demo purpose

from os import path as os_path
from pathlib import Path
import sys 
main_path = str( Path(os_path.abspath(__file__)).parent.parent )
sys.path.append(main_path)
from main import logger

# -
# But one should use
# from logger import Logger
# Because 'logger' folder is a python module with __init__.py


# Use default 'main' logger module which will store logs to 'logs/main.log'
# Demo of all logger levels.
logger.main.info(f"This is info")
logger.main.debug(f"This is debug")
logger.main.warning(f"This is warning")
logger.main.error(f"This is error")
logger.main.critical(f"This is critical")
# Also logger inherits from dict, so we can do:
logger["main"].info(f"Also Im a dict!")


# Create another custom logger module with separate .log file
logger.create("mymodule")
logger.mymodule.info(f"This is info from 'mymodule'.")


# All logger modules supports stdout.
# Enable example:
# By default every logger module has disabled stdout.
logger.mymodule.info(f"STDOUT disabled.")
logger.mymodule.stdout_mode(True)
logger.mymodule.info(f"STDOUT enabled.")
logger.mymodule.stdout_mode(False)
