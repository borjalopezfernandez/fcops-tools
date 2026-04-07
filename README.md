# fcops-tools
FLEX Core Payload Data Ground Segment Operations Service

## Installation

Install from the built wheel package:

```bash
pip install dist/fcops-x.y.z-py3-none-any.whl
```

## Usage

After installation, the FCOPS tool are available.


## fcops_maap_query_datatake

```bash
fcops_maap_query_datatake --type L1C_FLXSYN --start 2023-07-12T07:00:00Z --end 2023-07-12T09:00:00Z --baseline 01 -C
```


## fcops_maap_query_product

```bash
fcops_maap_query_product --id FLX_L1B_OBS____20230712T075954_20230712T080232_20260325T161900_0158_100_064_0021_01 | jq .properties
```


## fcops_mpf_ppf2kml

```bash
fcops_mpf_ppf2kml --help
fcops_mpf_ppf2kml --version  # Shows version and current date
```

Available commands:
- `info`: Display header information from a planning file
- `list`: List events from a planning file
- `stats`: Display statistics about events
- `search`: Search and filter events
- `export`: Export planning file data as JSON
- `analyze`: Perform detailed analysis
- `config`: Display the configuration file contents

