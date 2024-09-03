# -------------- #
# System imports #

from os             import path as os_path
from pathlib        import Path
from sys            import path as sys_path
# Next two lines are nessesary for pytest
# Othervise it imports __init__.py and cant find main.py
# (which is strange)
main_path = str( Path(os_path.abspath(__file__)).parent )
sys_path.append(main_path)



# ------------------- #
# Third party imports #



# ------------- #
# Local imports #

from main       import Logger
