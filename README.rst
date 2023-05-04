aquasec-cli
===========

Aqua Security CLI

Installation
------------

.. code:: bash

   >>> python -m pip install aquasec-cli

Usage
-----

**Help Menu of all Groups:**

.. code:: bash

   aquasec-cli  --help    
   Usage: aquasec-cli [OPTIONS] COMMAND [ARGS]...

     AquaSec CLI tool to manage AquaSec Tenant

   Options:
     --help  Show this message and exit.

   Commands:
     delapi   Deletes created API Auth
     initapi  Initializes API Auth
     reports  Generate CIS Bench Reports

**NOTE:** Each subcommand has a help menu to assist with the calls being
made. This project relies on the yaml or localized configurations being
help as they are not passed in the commands as of this release.

**Create API Auth Token:**

.. code:: bash

   >>> aquasec-cli init --csp_roles="Auditor" --csp_roles="Admin" --endpoints="Any"
   Initializing API
   INFO    : Created WorkloadAuth Token for URL https://1234abcff1.cloud.aquasec.com

**Run Report:**

.. code:: bash

   aquasec-cli  reports --report_type kube_bench --report_location /Users/username/var/tmp
   Report completed Saving
   Report written out to /Users/adamt/var/tmp/aquasec_report_type_kube_bench_20230424T153825.json

**Delete API Auth:**

.. code:: bash

   >>> aquasec-cli delete                                              
   Are you sure you want to delete the auth api token? [y/N]: y
   Deleted Auth

Release Info
------------

v0.0.2
~~~~~~

-  Bug fix with requirements

Version
-------

+-------------------------+-----------------+-------------------------+
| Version                 | Build           | Changes                 |
+=========================+=================+=========================+
| **0.0.2**               | **a1**          | issues with dataclasses |
|                         |                 | getting installed under |
|                         |                 | normal condition        |
+-------------------------+-----------------+-------------------------+
| **0.0.2**               | **final**       | tested in pytest and    |
|                         |                 | seems to now accept the |
|                         |                 | dataclass               |
+-------------------------+-----------------+-------------------------+
| **0.0.3**               | **a1**          | issues with dataclasses |
|                         |                 | and now yaml getting    |
|                         |                 | installed under normal  |
|                         |                 | condition               |
+-------------------------+-----------------+-------------------------+

Warnings
~~~~~~~~

Use at your own risk!!!
