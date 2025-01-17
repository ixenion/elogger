# -------------- #
# System imports #



# ------------------- #
# Third party imports #



# ------------- #
# Local imports #




# ------- #
# CLASSES #
# ------- #


class LoggerAttributeError(AttributeError):
    """
        There is no attribute that you are probbly misstyped.
    """

    def __init__(self, attr_name:str) -> None:
        self.message = f"Logger has no attribute '{attr_name}'. Create it first."
        super().__init__(self.message)


class ModuleNotFoundException(Exception):
    """
        There is no module you are calling...
    """

    def __init__(self, module_name:str) -> None:
        self.message = f"There is no module you are calling: {module_name}"
        super().__init__(self.message)
