# pylint: disable=line-too-long
"""Commands API"""

import os
import pickle
import contextlib
from pathlib import Path
import click
from aquasec.api import API

from aquasec_cli.utils import (abort_if_false, get_tmpdir)


@click.command()
@click.option("--csp_roles", default=["api_auditor"], type=click.STRING, multiple=True, help="Creates Aquasec auth token")
@click.option("--endpoints", default=["ANY"], type=click.STRING, multiple=True, help="Endpoint Call Allowed")
def init(csp_roles, endpoints):
    """Initializes API Auth

    Args:
        csp_roles (_type_): _description_
        endpoints (_type_): _description_
    """
    click.echo("Initializing API")
    tmpdir = get_tmpdir()
    pkl_filename = Path.joinpath(tmpdir, 'aqua_api.pkl')
    csp_role = list(csp_roles)
    endpoint = [end.upper() for end in endpoints]
    api = API(csp_roles=csp_role, allowed_endpoints=endpoint)
    with open(pkl_filename, 'wb') as f:
        # Encode with base64 before dumping to file
        # pkl_file = codecs.encode(pickle.dumps(api.workload_auth), "base64").decode()
        pickle.dump(api.workload_auth, f)


@click.command()
@click.option("--yes", is_flag=True, callback=abort_if_false, expose_value=False, prompt="Are you sure you want to delete the auth api token?")
def delete():
    """Deletes created API Auth
    """
    tmpdir = get_tmpdir()
    pkl_filename = Path.joinpath(tmpdir, 'aqua_api.pkl')
    # Use supress to suppress error if file is already deleted
    with contextlib.suppress(FileNotFoundError):
        os.remove(pkl_filename)
    click.secho("Deleted Auth", color="green")
