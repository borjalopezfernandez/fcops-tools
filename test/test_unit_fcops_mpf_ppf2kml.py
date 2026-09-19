#!/usr/bin/env python3
"""
Integration tests for the FCOPS CLI after wheel installation.
"""

import unittest
import subprocess
import sys
from pathlib import Path

from loguru import logger
logger = logger.patch(lambda record: record.update(name=record["file"].name))

class TestCLIIntegration(unittest.TestCase):
    """Test CLI commands after wheel installation."""

    def setUp(self):
        """Set up test fixtures."""
        # Find the installed fcops_mpf_ppf2kml command
        self.cli_command = None
        try:
            # Try to find the command in PATH
            result = subprocess.run(['which', 'fcops_mpf_ppf2kml'],
                                  capture_output=True, text=True, timeout=10)
            if result.returncode == 0:
                self.cli_command = result.stdout.strip()
        except (subprocess.TimeoutExpired, FileNotFoundError):
            pass

        # If not found in PATH, try common installation locations
        if not self.cli_command:
            common_paths = [
                Path.home() / '.local' / 'bin' / 'fcops_mpf_ppf2kml',
                Path('/usr/local/bin/fcops_mpf_ppf2kml'),
                Path('/usr/bin/fcops_mpf_ppf2kml'),
            ]
            for path in common_paths:
                if path.exists():
                    self.cli_command = str(path)
                    break

    def test_cli_command_available(self):
        """Test that the CLI command is available after installation."""
        self.assertIsNotNone(self.cli_command,
                           "fcops-ppf-parser command not found. "
                           "Make sure the wheel package is installed.")

    def test_config_command_exists(self):
        """Test that the config command is available."""
        if not self.cli_command:
            self.skipTest("CLI command not available")

        result = subprocess.run([self.cli_command, '--help'],
                              capture_output=True, text=True, timeout=10)

        self.assertEqual(result.returncode, 0,
                        f"CLI help failed: {result.stderr}")
        self.assertIn('config', result.stdout,
                     "config command not found in CLI help")

    def test_config_command_output(self):
        """Test that the config command produces expected output."""
        if not self.cli_command:
            self.skipTest("CLI command not available")

        result = subprocess.run([self.cli_command, 'config'],
                              capture_output=True, text=True, timeout=30)

        self.assertEqual(result.returncode, 0,
                        f"Config command failed: {result.stderr}")

        # Check for expected content in output
        output = result.stdout
        self.assertIn('FLX_OPER_MPL_ORBSCT', output,
                     "Config file name not found in output")


    def test_command_file_config(self):
        """Test that the config command shows the correct file path."""
        if not self.cli_command:
            self.skipTest("CLI command not available")

        result = subprocess.run([self.cli_command, 'config'],
                              capture_output=True, text=True, timeout=30)

        self.assertEqual(result.returncode, 0,
                        f"Config command failed: {result.stderr}")

        output = result.stdout
        # The orbit scenario file should be in the package data directory
        self.assertRegex(output, r'.*/fcops/data/FLX_OPER_MPL_ORBSCT_.*\.EOF',
                        "Config file path not found or incorrect in output")


    def test_version_option(self):
        """Test that the --version option shows version and library information."""
        if not self.cli_command:
            self.skipTest("CLI command not available")

        result = subprocess.run([self.cli_command, '--version'],
                              capture_output=True, text=True, timeout=10)

        self.assertEqual(result.returncode, 0,
                        f"Version option failed: {result.stderr}")

        output = result.stdout.strip()
        # Check for expected content in output
        lines = output.split('\n')
        
        # Should have at least 6 lines
        self.assertGreaterEqual(len(lines), 6, f"Version output should have at least 6 lines, got {len(lines)}")
        
        # Check fcops version line
        self.assertIn('fcops_mpf_ppf2kml - 0.', lines[0],
                     "fcops version line not found or incorrect")
        
        # Check CFI libraries header
        self.assertEqual(lines[4], 'Current Earth Explorer CFI libraries:',
                        "CFI libraries header not found")


    def test_process_nppf(self):
        """Test that the --version option shows version and library information."""
        if not self.cli_command:
            self.skipTest("CLI command not available")

        cmd = 'fcops_mpf_ppf2kml list test/data/FLX_OPER_MPL_NPPF___20260901T000000_20260928T000000_0001.xml'
        logger.debug(cmd)


    def test_process_nppf_kml(self):
        """Test that the --version option shows version and library information."""
        if not self.cli_command:
            self.skipTest("CLI command not available")
        cmd = 'fcops_mpf_ppf2kml list --kml test/data/FLX_OPER_MPL_NPPF___20260901T000000_20260928T000000_0001.xml > test/data/FLX_OPER_MPL_NPPF___20260901T000000_20260928T000000_0001.kml'
        logger.debug(cmd)

    
    def test_process_nppf_kml_orbit(self):
        """ test the orbit """
        if not self.cli_command:
            self.skipTest("CLI command not available")
        cmd = 'fcops_mpf_ppf2kml list --orbit test/data/FLX_OPER_MPL_ORBSCT_20230703T000001_99999999T999999_0001.EOF --kml test/data/FLX_OPER_MPL_NPPF___20230703T000000_20230730T000000_0002.xml > test/data/FLX_OPER_MPL_NPPF___20230703T000000_20230730T000000_0002.kml'
        logger.debug(cmd)

    # python -m pytest -s test/test_unit_fcops_mpf_ppf2kml.py::TestCLIIntegration::test_process_nppf_kml_orbit_svt3 -v
    def test_process_nppf_kml_orbit_svt3(self):
        """ Test SVT-3 plan """
        if not self.cli_command:
            self.skipTest("CLI command not available")
        cmd = 'fcops_mpf_ppf2kml list --orbit test/data/FLX_OPER_MPL_ORBSCT_20251005T233811_99999999T999999_0001.EOF --kml test/data/FLX_OPER_MPL_NPPF___20251006T000000_20251102T000000_0005.xml > test/data/FLX_OPER_MPL_NPPF___20251006T000000_20251102T000000_0005.kml'
        print(cmd)
        logger.debug(cmd)

    def test_process_nppf_kml_com_1(self):
        """ Test SVT-3 plan """
        if not self.cli_command:
            self.skipTest("CLI command not available")
        cmd = 'fcops_mpf_ppf2kml list --orbit test/data/FLX_OPER_MPL_ORBSCT_20260915T044228_99999999T999999_0001.EOF --kml test/data/FLX_OPER_MPL_NPPF___20260921T000000_20261018T000000_0001.xml > test/data/FLX_OPER_MPL_NPPF___20260921T000000_20261018T000000_0001.kml'
        print(cmd)
        logger.debug(cmd)

if __name__ == '__main__':
    unittest.main()