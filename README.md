# aquasec-cli

Aqua Security CLI

## Installation

```bash
>>> python -m pip install aquasec-cli
```

## Usage

__Help Menu of all Groups:__

```bash
>>> aquasec-cli --help
Usage: aquasec-cli [OPTIONS] COMMAND [ARGS]...

  AquaSec CLI tool to manage AquaSec Tenant

Options:
  --help  Show this message and exit.

Commands:
  delete   Deletes created API Auth
  init     Initializes API Auth
  reports  Generate CIS Bench Reports
```

```bash
>>> aquasec-cli init --help   
Usage: aquasec-cli init [OPTIONS]

  Initializes API Authentication token used to run commands; required to
  generate before a command can be executed

Options:
  --csp_roles TEXT  Creates Aquasec auth token
  --endpoints TEXT  Endpoint Call Allowed
  --help            Show this message and exit.
```

```bash
>>> aquasec-cli reports --help
Usage: aquasec-cli reports [OPTIONS]

  Generate CIS Bench Reports

  Used to generate CIS Bench Reports in different formats

Options:
  -r, --report_type [cis|kube_bench|linux|openshift|disa_stig|all]
                                  Report type to genorate
  -c, --cluster_name TEXT         Supply Cluster name
  -l, --report_location TEXT      Directory to write out report to; please
                                  ensure proper formatting given the system
                                  you are on  [required]
  --report_format [list|flat_list|raw]
                                  Report Format
  --help                          Show this message and exit.
```

```bash
>>> aquasec-cli delete --help
Usage: aquasec-cli delete [OPTIONS]

  Deletes created API Auth

Options:
  --yes
  --help  Show this message and exit.
```

__NOTE:__ Each subcommand has a help menu to assist with the calls being made. This project relies on the yaml or localized configurations being help as they are not passed in the commands as of this release.

__Create API Auth Token:__

```bash
>>> aquasec-cli init --csp_roles="Auditor" --csp_roles="Admin" --endpoints="Any"
Initializing API
INFO    : Created WorkloadAuth Token for URL https://1234abcff1.cloud.aquasec.com
```

__Run Report:__

```bash
aquasec-cli  reports --report_type kube_bench --report_location /var/tmp --report_format list
Report completed Saving
Report written out to /var/tmp/aquasec_report_type_kube_bench_20230424T153825.json
```

__Delete API Auth:__

```bash
>>> aquasec-cli delete                                              
Are you sure you want to delete the auth api token? [y/N]: y
Deleted Auth
```

## Release Info

### v0.0.6

* Added error handling
* Added ability to generate different reports
* Updated requirements to new aquasec-api

### v0.0.5

* Updated Readme and changed type from RST to MD
* Reverted snyk workflow file

### v0.0.4

* fixed issue with broken aquasec-api v0.0.3

### v0.0.3

* Fixed installation and dependencies
* locked down dependencies
* added toml and setup.cfg to support furture installations

### v0.0.2

* Bug fix with requirements

## Version

| Version | Build | Changes |
| ------- | ----- | ------- |
| __0.0.2__ | __a1__ | issues with dataclasses getting installed under normal condition |
| __0.0.2__ | __final__ | tested in pytest and seems to now accept the dataclass |
| __0.0.3__ | __a1__ | issues with dataclasses and now yaml getting installed under normal condition |
| __0.0.3__ | __a3__ | migrating to toml and setup.cfg |
| __0.0.3__ | __a4__ | cleaned up utils and updated snyk to confirm pass locally; added to git ignore |
| __0.0.3__ | __a5__ | setup.cfg issues wiht pip |
| __0.0.3__ | __final__ | found issue with toml and other dependencies |
| __0.0.4__ | __final__ | fixed issue with aquaapi dependency |
| __0.0.5__ | __a1__ | fixed readme to point to md file; adjusting snyk |
| __0.0.5__ | __final__ | tested and released |
| __0.0.6__ | __a1__ | removed README.rst updated snyk |
| __0.0.6__ | __a2__ | make delete more efficent added adjustments to report |

### Warnings

Use at your own risk!!!
