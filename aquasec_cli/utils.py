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
