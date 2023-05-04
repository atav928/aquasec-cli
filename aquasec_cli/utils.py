"""Utilities"""

from pathlib import Path
import platform
import tempfile


def get_tmpdir() -> Path:
    """Gets Temp Dir

    Returns:
        Path: _description_
    """
    tempdir = Path("/tmp" if platform.system() ==
                   "Darwin" else tempfile.gettempdir())
    return tempdir


def abort_if_false(ctx, param, value): # pylint: disable=unused-argument
    """Abort Value if false

    Args:
        ctx (_type_): _description_
        param (_type_): _description_
        value (_type_): _description_
    """
    if not value:
        ctx.abort()

def reformat_exception(error: Exception) -> str:
    """Reformates Exception to print out as a string pass for logging

    Args:
        error (Exception): _description_

    Returns:
        str: _description_
    """
    return f"{type(error).__name__}: {str(error)}" if error else ""
