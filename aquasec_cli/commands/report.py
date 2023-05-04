# pylint: disable=line-too-long
"""Report Commands"""

import sys
import json
import pickle
import datetime
from pathlib import Path

from aquasec.api import API
from aquasec.orchestration.bench_report import BenchReport

import click

from aquasec_cli.utils import get_tmpdir, reformat_exception


@click.command()
@click.option("--report_type", "-r", default="all", type=click.Choice(['cis', 'kube_bench', 'linux', 'openshift', 'disa_stig', 'all'], case_sensitive=True), help="Report type to genorate")
@click.option("--cluster_name", "-c", required=False, type=str, help="Supply Cluster name")
@click.option("--report_location", "-l", required=True, type=str, help="Directory to write out report to; please ensure proper formatting given the system you are on")
@click.option("--report_format", required=False, default="list",type=click.Choice(['list', 'flat_list', 'raw'], case_sensitive=True), help="Report Format")
def reports(report_type, cluster_name, report_location, report_format):
    """Generate CIS Bench Reports

    Used to generate CIS Bench Reports in different formats
    """
    # check on report directory
    if not Path.is_dir(Path(report_location)):
        click.secho(
            "Report Directory does not exist unable to run report", color="red")
        sys.exit()
    #  pull credentials
    try:
        tmpdir = get_tmpdir()
        pkl_filename = Path.joinpath(tmpdir, 'aqua_api.pkl')
        with open(pkl_filename, 'rb') as f:
            pkl_file = pickle.load(f)
        api: API = API(workload_auth=pkl_file)
        bench = BenchReport(api=api, report_type=report_type, report_format=report_format, cluster_name=cluster_name if cluster_name else "")
        bench.run()
        click.secho("Report completed Saving", color='green')
        filename = Path.joinpath(Path(
            report_location),
            f"aquasec_report_type_{report_type}_{datetime.datetime.now().strftime('%Y%m%dT%H%M%S')}.json")
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(bench.bench_report, f, indent=2)
        click.secho(f"Report written out to {filename}", color='green')
    except Exception as err:
        error = reformat_exception(err)
        click.secho(f"Error: {error}")
