"""
FCOPS - FLEX Mission Operations Tools

A Python package for parsing and analyzing FLEX mission planning files.
"""

__version__ = "1.0.0"
__author__ = "FCOPS Team"

from fcops.floris_modes import get_floris_mode_label

from fcops.parser_xml_ppf import parse_file_ppf, PlanningFile, Header, Event

__all__ = [
    'parse_file_ppf',
    'PlanningFile',
    'Header',
    'Event',
    'get_floris_mode_label'
]
