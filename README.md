# aquasec-cli

Aqua Security CLI

## Installation

```bash
>>> python -m pip install aquasec-cli
```

## Usage

__Help Menu of all Groups:__

```bash
aquasec-cli  --help    
Usage: aquasec-cli [OPTIONS] COMMAND [ARGS]...

  AquaSec CLI tool to manage AquaSec Tenant

Options:
  --help  Show this message and exit.

Commands:
  delapi   Deletes created API Auth
  initapi  Initializes API Auth
  reports  Generate CIS Bench Reports
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
aquasec-cli  reports --report_type kube_bench --report_location /Users/username/var/tmp
Report completed Saving
Report written out to /Users/adamt/var/tmp/aquasec_report_type_kube_bench_20230424T153825.json
```

__Delete API Auth:__

```bash
>>> aquasec-cli delete                                              
Are you sure you want to delete the auth api token? [y/N]: y
Deleted Auth
```

## Version

| Version | Build | Changes |
| ------- | ----- | ------- |
| __0.0.1__ | __a1__ | issues with dataclasses getting installed under normal condition |

### Warnings

Use at your own risk!!!
