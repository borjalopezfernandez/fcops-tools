# fcops-tools
FLEX Core Payload Data Ground Segment Operations Service

## Installation

Install from the built wheel package:

```bash
pip install dist/fcops-0.0.0-py3-none-any.whl
```

## Usage

After installation, the CLI tool is available as `fcops_mpf_ppf2kml`:

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

## Testing

After wheel installation, verify the config command works:

```bash
python test_config_after_install.py
```

Or run the full integration test suite:

```bash
python -m pytest test/test_cli_integration.py -v
```
