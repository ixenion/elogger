# -------------- #
# System imports #
from os             import path as os_path
from pathlib        import Path
from sys            import path as sys_path, stdout, stderr
# Next two lines are nessesary for pytest
# Othervise it imports __init__.py and cant find main.py
# (which is strange)
main_path = str( Path(os_path.abspath(__file__)).parent.parent )
sys_path.append(main_path)

# pytets-loguru
# import logging
# from loguru import logger as _logger
# from loguru._logger import Logger as _Logger_def, Core
# from pytest_loguru.plugin import caplog  # noqa: F401


# ------------------- #
# Third party imports #



# ------------- #
# Local imports #

from main           import Logger
from utils.datastructures   import Const

# --------- #
# CONSTANTS #
# --------- #


# ------- #
# CLASSES #
# ------- #


class TestDefaultLogger:

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


    def test_logger_default_sink(self, tmp_path) -> None:
        """
            Here we try to make log entry and confirm that it was created.

            parameters:

            - tmp_path:     Is a fixture. Points to the root dir:
                            log_system.
        """

        # Create logger object (singleton)
        self.logger = Logger(folder_path=tmp_path)
        # Make one entry
        message = f"Test info message"
        self.logger.main.info(message)
        # Construct log path
        module_name:str = self.logger._default_module_name
        module_ext:Const.Extentions = self.logger._default_module_ext
        module = module_name + module_ext.value
        log_path = tmp_path / module
        # Read the log (will contain one line)
        with open(log_path, 'r') as f:
            content = f.read()

        assert message in content


    def test_logger_default_levels(self, tmp_path) -> None:
        """
            Here we try to make several log entries and check their level.

            parameters:

            - tmp_path:     Is a fixture. Points to the root dir:
                            log_system.
        """

        # Create logger object (singleton)
        self.logger = Logger(folder_path=tmp_path)
        message = f"Test info message"
        # Write all sorts of levels log
        self.logger.main.trace(message)
        self.logger.main.debug(message)
        self.logger.main.info(message)
        self.logger.main.info(message)
        self.logger.main.success(message)
        self.logger.main.warning(message)
        self.logger.main.error(message)
        self.logger.main.critical(message)
        # Construct log path
        module_name:str = self.logger._default_module_name
        module_ext:Const.Extentions = self.logger._default_module_ext
        module = module_name + module_ext.value
        log_path = tmp_path / module
        # Read the log (will contain one line)
        with open(log_path, 'r') as f:
            content = f.read()

        success = "TRACE" and "DEBUG" and "INFO" and "SUCCESS" and \
                "WARNING" and "ERROR" and "CRITICAL" in content

        assert success == True

    
    #TODO
    def test_logger_default_stdout(self, tmp_path, caplog, capsys) -> None:
        """
            Here we try to make log entry and catch STDOUT.

            parameters:

            - tmp_path:     Is a fixture. Points to the root dir:
                            log_system.
        """

        # Create logger object (singleton)
        self.logger = Logger(folder_path=tmp_path)
        # Set up (enable) STDOUT for default module
        self.logger.main.stdout_mode(enable=True)
        
        # Write log
        magic_handler_id = \
                self.logger.main.add(sink=caplog.handler, level=0)
                # self.logger.main.add(sink=capsys.handler, level=0)
        
        message = f"Test info message"
        self.logger.main.info(message)

        # tmp = capsys.readouterr().out
        tmp = caplog.text

        self.logger.main.remove(magic_handler_id)
        self.logger.main.stdout_mode(enable=False)

        assert message in tmp
