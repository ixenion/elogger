# -------------- #
# System imports #

from os             import path as os_path
from pathlib        import Path
from sys            import path as sys_path
# Next two lines are nessesary for pytest
# Othervise it imports __init__.py and cant find main.py
# (which is strange)
main_path = str( Path(os_path.abspath(__file__)).parent.parent )
sys_path.append(main_path)


# ------------------- #
# Third party imports #


# ------------- #
# Local imports #

from main           import Logger


# --------- #
# CONSTANTS #
# --------- #


# ------- #
# CLASSES #
# ------- #


class TestDependenciesImport:

    def setup_method(self, method) -> None:
        """
            Fires before test. Usefull for test preps
            (create some objects etc)
        """

        # As Logger is Singleton and we need to test different Logger
        # instances between test_* files - need to reset Singleton.
        Logger._reset_instance()
        self.logger:None|Logger = None


    def teardown_method(self, method) -> None:
        """
            Fires after test was done. Usefull for test preps
            (delete some objects etc)
        """

        del self.logger


    def test_dependencies_import(self) -> None:
        """ Test that required libs are installed."""

        try:
            from loguru import logger
            installed = True
        except ImportError as e:
            installed = False

        assert installed == True
