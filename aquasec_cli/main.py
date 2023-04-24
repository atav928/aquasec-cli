"""Main CLI Script"""

import click

from aquasec_cli.commands import (api, report)


@click.group()
def cli():
    """AquaSec CLI tool to manage AquaSec Tenant"""


cli.add_command(api.init)
cli.add_command(report.reports)
cli.add_command(api.delete)

if __name__ == "__main__":
    cli()
