#!/usr/bin/env python3
"""
Test script to verify the config flag works after wheel installation.

This script can be run after installing the fcops wheel package to verify
that the config command is working correctly.

Usage:
    python test_config_after_install.py
"""

import subprocess
import sys
from pathlib import Path


def test_config_command():
    """Test that the config command works after wheel installation."""
    print("Testing fcops config command after wheel installation...")

    # Find the CLI command
    cli_command = None
    try:
        result = subprocess.run(['which', 'fcops_mpf_ppf2kml'],
                              capture_output=True, text=True, timeout=10)
        if result.returncode == 0:
            cli_command = result.stdout.strip()
    except (subprocess.TimeoutExpired, FileNotFoundError):
        pass

    if not cli_command:
        print("❌ ERROR: fcops_mpf_ppf2kml command not found in PATH")
        print("   Make sure the fcops wheel package is installed:")
        print("   pip install dist/fcops-0.0.0-py3-none-any.whl")
        return False

    print(f"✅ Found CLI command: {cli_command}")

    # Test that config command exists
    try:
        result = subprocess.run([cli_command, '--help'],
                              capture_output=True, text=True, timeout=10)
        if result.returncode != 0:
            print("❌ ERROR: CLI help command failed")
            return False

        if 'config' not in result.stdout:
            print("❌ ERROR: config command not found in CLI help")
            return False

        print("✅ Config command found in CLI help")
    except Exception as e:
        print(f"❌ ERROR: Failed to check CLI help: {e}")
        return False

    # Test config command output
    try:
        result = subprocess.run([cli_command, 'config'],
                              capture_output=True, text=True, timeout=30)

        if result.returncode != 0:
            print(f"❌ ERROR: Config command failed: {result.stderr}")
            return False

        output = result.stdout

        # Check for expected content
        checks = [
            ('FLX_OPER_MPL_ORBSCT' in output, "Config file name not found"),
        ]

        for check, error_msg in checks:
            if not check:
                print(f"❌ ERROR: {error_msg}")
                return False

        print("✅ Config command output contains expected content")
        print("✅ Config command test PASSED")

        return True

    except Exception as e:
        print(f"❌ ERROR: Failed to run config command: {e}")
        return False


if __name__ == '__main__':
    success = test_config_command()
    sys.exit(0 if success else 1)