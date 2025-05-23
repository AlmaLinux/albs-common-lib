"""AlmaLinux Build System common error classes."""


class BuildError(Exception):
    """Base class for all kind of build errors."""

    pass


class BuildConfigurationError(BuildError):

    pass


class BuildExcluded(Exception):
    """Indicates that a build was excluded."""

    pass


class ConfigurationError(Exception):
    """Invalid configuration error."""

    pass


class DataNotFoundError(Exception):
    """Required data is not found error."""

    pass


class PermissionDeniedError(Exception):
    """Insufficient permissions error."""

    pass


class ConnectionError(Exception):
    """Network or database connection error."""

    pass


class DataSchemaError(Exception):
    """Data validation error."""

    pass


class WorkflowError(Exception):
    """
    A workflow violation error.

    It is used for the cases when code is trying to do things which aren't
    supported by our workflow (e.g. update a non-finished build).
    """

    pass


class DuplicateError(Exception):
    """A duplicate data insertion error."""

    pass


class CommandExecutionError(Exception):
    """Shell command execution error."""

    def __init__(
        self,
        message,
        exit_code,
        stdout,
        stderr,
        command=None,
    ):
        """
        Parameters
        ----------
        message : str or unicode
            Error message.
        exit_code : int
            Command exit code.
        stdout : str
            Command stdout.
        stderr : str
            Command stderr.
        command : list, optional
            Executed command.
        """
        super().__init__(message)
        self.exit_code = exit_code
        self.stdout = stdout
        self.stderr = stderr
        self.command = command


class LockError(Exception):
    """A resource lock acquiring error."""

    pass


class SignError(ValueError):
    pass


class PackageSignError(Exception):
    pass


class SpecParseError(ValueError):
    pass
