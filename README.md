# fondat-salesforce

[![PyPI](https://badge.fury.io/py/fondat-salesforce.svg)](https://badge.fury.io/py/fondat-salesforce)
[![Python](https://img.shields.io/pypi/pyversions/fondat-core)](https://python.org/)
[![GitHub](https://img.shields.io/badge/github-main-blue.svg)](https://github.com/fondat/fondat-salesforce/)
[![Test](https://github.com/fondat/fondat-salesforce/workflows/test/badge.svg)](https://github.com/fondat/fondat-salesforce/actions?query=workflow/test)
[![License](https://img.shields.io/github/license/fondat/fondat-salesforce.svg)](https://github.com/fondat/fondat-salesforce/blob/main/LICENSE)
[![Black](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)

Fondat package for Salesforce.

## Develop

```
poetry install
poetry run pre-commit install
```

## Test

Set up
```
# set this for sandbox; default is login.salesforce.com
export FONDAT_SALESFORCE_ENDPOINT=https://test.salesforce.com

# creds
export FONDAT_SALESFORCE_CLIENT_ID=
export FONDAT_SALESFORCE_CLIENT_SECRET=
# ... only for password
export FONDAT_SALESFORCE_USERNAME=
export FONDAT_SALESFORCE_PASSWORD=
# ... only for refresh
export FONDAT_SALESFORCE_REFRESH_TOKEN=
```

Run
```
poetry run pytest -v --auth password
poetry run pytest -v --auth refresh
```
