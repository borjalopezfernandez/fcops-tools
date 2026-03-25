#!/usr/bin/env python3
"""
Unit tests for the FLEX planning XML parser.
"""

import unittest
import tempfile
from pathlib import Path
from datetime import datetime

from src.fcops.parser_xml_ppf import (
    parse_file, parse_file_string, Header, Event, PlanningFile,
    _parse_datetime, _parse_int, _parse_float, _try_convert_value
)


class TestHelperFunctions(unittest.TestCase):
    """Test helper parsing functions."""

    def test_parse_datetime_valid(self):
        """Test parsing valid ISO datetime."""
        result = _parse_datetime("2026-09-01T22:00:00Z")
        self.assertIsNotNone(result)
        self.assertEqual(result.year, 2026)
        self.assertEqual(result.month, 9)
        self.assertEqual(result.day, 1)

    def test_parse_datetime_with_microseconds(self):
        """Test parsing datetime with microseconds."""
        result = _parse_datetime("2026-09-01T22:46:28.887Z")
        self.assertIsNotNone(result)

    def test_parse_datetime_empty(self):
        """Test parsing empty datetime string."""
        result = _parse_datetime("")
        self.assertIsNone(result)

    def test_parse_datetime_invalid(self):
        """Test parsing invalid datetime."""
        result = _parse_datetime("invalid")
        self.assertIsNone(result)

    def test_parse_int_valid(self):
        """Test parsing valid integer."""
        self.assertEqual(_parse_int("42"), 42)

    def test_parse_int_invalid(self):
        """Test parsing invalid integer."""
        self.assertEqual(_parse_int("invalid"), 0)

    def test_parse_int_empty(self):
        """Test parsing empty integer."""
        self.assertEqual(_parse_int(""), 0)

    def test_parse_float_valid(self):
        """Test parsing valid float."""
        self.assertEqual(_parse_float("3.14"), 3.14)

    def test_parse_float_invalid(self):
        """Test parsing invalid float."""
        self.assertEqual(_parse_float("invalid"), 0.0)

    def test_try_convert_value_int(self):
        """Test value conversion to int."""
        self.assertEqual(_try_convert_value("42"), 42)
        self.assertIsInstance(_try_convert_value("42"), int)

    def test_try_convert_value_float(self):
        """Test value conversion to float."""
        self.assertEqual(_try_convert_value("3.14"), 3.14)
        self.assertIsInstance(_try_convert_value("3.14"), float)

    def test_try_convert_value_string(self):
        """Test value conversion keeps string."""
        self.assertEqual(_try_convert_value("hello"), "hello")
        self.assertIsInstance(_try_convert_value("hello"), str)


class TestHeader(unittest.TestCase):
    """Test Header class."""

    def setUp(self):
        """Set up test fixtures."""
        self.header_dict = {
            'format_version': '1',
            'gen_time': '2026-03-19T11:13:10Z',
            'validity_start': '2026-09-01T22:00:00Z',
            'validity_end': '2026-09-14T00:00:00Z',
            'spacecraft': 'FLEX',
            'purpose': 'Delta Nominal Payload Planning File',
            'icd_version': 'ESA-EOPG-EOEP-TN-0028-1.2',
            'filename': 'FLX_OPER_MPL_DNPPF__20260901T220000_0001'
        }

    def test_header_to_dict(self):
        """Test converting header to dictionary."""
        header = Header(
            format_version='1',
            gen_time=datetime(2026, 3, 19, 11, 13, 10),
            validity_start=datetime(2026, 9, 1, 22, 0, 0),
            validity_end=datetime(2026, 9, 14, 0, 0, 0),
            spacecraft='FLEX',
            purpose='Test',
            icd_version='1.0',
            filename='test.xml'
        )
        result = header.to_dict()
        self.assertEqual(result['spacecraft'], 'FLEX')
        self.assertEqual(result['format_version'], '1')


class TestEvent(unittest.TestCase):
    """Test Event class."""

    def setUp(self):
        """Set up test fixtures."""
        self.event_xml = """
        <event isEvent="true" time="2026-09-01T22:46:28.887Z" id="XPREPARE" 
               description="Prepare X-band Data Transmission" source="PDGS" 
               type="Orbital Angle tagged SRC Sequence" count="545430927" 
               absolute_orbit="54543" relative_orbit="257" sec_from_anx="927.890" 
               deg_from_anx="55.190" group_id="4436" parameter_count="0"/>
        """

    def test_event_to_dict(self):
        """Test converting event to dictionary."""
        import xml.etree.ElementTree as ET
        elem = ET.fromstring(self.event_xml)
        event = Event.from_element(elem)
        result = event.to_dict()
        
        self.assertEqual(result['event_id'], 'XPREPARE')
        self.assertEqual(result['absolute_orbit'], 54543)
        self.assertEqual(result['group_id'], 4436)

    def test_event_with_parameters(self):
        """Test event with additional parameters."""
        event_xml_with_params = """
        <event isEvent="true" time="2026-09-01T23:01:57.508Z" id="FPOBS_ID" 
               description="Set Calibration ID" source="PDGS" 
               type="Orbital Angle tagged SRC Sequence" count="545431856" 
               absolute_orbit="54543" relative_orbit="257" sec_from_anx="1856.511" 
               deg_from_anx="110.476" group_id="3524" parameter_count="1" 
               CALIB_ID_EOB="31"/>
        """
        import xml.etree.ElementTree as ET
        elem = ET.fromstring(event_xml_with_params)
        event = Event.from_element(elem)
        
        self.assertEqual(event.parameter_count, 1)
        self.assertIn('CALIB_ID_EOB', event.parameters)
        # Parameters are automatically converted to appropriate types (int, float, or string)
        self.assertEqual(event.parameters['CALIB_ID_EOB'], 31)


class TestPlanningFile(unittest.TestCase):
    """Test PlanningFile class."""

    def setUp(self):
        """Set up test fixtures."""
        self.planning_xml = """<?xml version="1.0"?>
        <eventfile xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
          <header format_version="1" gen_time="2026-03-19T11:13:10Z" 
                  validity_start="2026-09-01T22:00:00Z" 
                  validity_end="2026-09-14T00:00:00Z" spacecraft="FLEX" 
                  purpose="Test" icd_version="1.0" filename="test.xml"/>
          <events>
            <event isEvent="true" time="2026-09-01T22:46:28.887Z" id="XPREPARE" 
                   description="Test 1" source="PDGS" type="Type1" count="1" 
                   absolute_orbit="100" relative_orbit="1" sec_from_anx="100" 
                   deg_from_anx="10" group_id="1" parameter_count="0"/>
            <event isEvent="true" time="2026-09-02T22:46:28.887Z" id="XPREPARE" 
                   description="Test 2" source="PDGS" type="Type2" count="2" 
                   absolute_orbit="101" relative_orbit="2" sec_from_anx="200" 
                   deg_from_anx="20" group_id="2" parameter_count="0"/>
            <event isEvent="true" time="2026-09-03T22:46:28.887Z" id="XDMPSTRT" 
                   description="Test 3" source="PDGS" type="Type1" count="3" 
                   absolute_orbit="102" relative_orbit="3" sec_from_anx="300" 
                   deg_from_anx="30" group_id="3" parameter_count="0"/>
          </events>
        </eventfile>
        """

    def test_parse_file_string(self):
        """Test parsing from string."""
        planning = parse_file_string(self.planning_xml)
        self.assertIsNotNone(planning)
        self.assertEqual(planning.header.spacecraft, 'FLEX')
        self.assertEqual(len(planning.events), 3)

    def test_get_events_by_id(self):
        """Test filtering events by ID."""
        planning = parse_file_string(self.planning_xml)
        events = planning.get_events_by_id('XPREPARE')
        self.assertEqual(len(events), 2)

    def test_get_events_by_type(self):
        """Test filtering events by type."""
        planning = parse_file_string(self.planning_xml)
        events = planning.get_events_by_type('Type1')
        self.assertEqual(len(events), 2)

    def test_get_events_by_orbit(self):
        """Test filtering events by orbit."""
        planning = parse_file_string(self.planning_xml)
        events = planning.get_events_by_orbit(100)
        self.assertEqual(len(events), 1)
        self.assertEqual(events[0].event_id, 'XPREPARE')

    def test_get_events_by_time_range(self):
        """Test filtering events by time range."""
        import xml.etree.ElementTree as ET
        from datetime import timezone
        planning = parse_file_string(self.planning_xml)
        # Use timezone-aware datetimes to match parsed events
        start = datetime(2026, 9, 2, 0, 0, 0, tzinfo=timezone.utc)
        end = datetime(2026, 9, 2, 23, 59, 59, tzinfo=timezone.utc)
        events = planning.get_events_by_time_range(start, end)
        self.assertEqual(len(events), 1)

    def test_to_dict(self):
        """Test converting planning file to dictionary."""
        planning = parse_file_string(self.planning_xml)
        result = planning.to_dict()
        
        self.assertIn('header', result)
        self.assertIn('events', result)
        self.assertEqual(len(result['events']), 3)


class TestFileIntegration(unittest.TestCase):
    """Integration tests with actual file."""

    def test_parse_real_file(self):
        """Test parsing the actual test file."""
        test_file = Path("test/data/FLX_OPER_MPL_DNPPF__20260901T220000_20260914T000000_0001.xml")
        
        if not test_file.exists():
            self.skipTest(f"Test file not found: {test_file}")
        
        planning = parse_file(str(test_file))
        
        # Verify header
        self.assertEqual(planning.header.spacecraft, 'FLEX')
        self.assertEqual(planning.header.format_version, '1')
        
        # Verify events
        self.assertGreater(len(planning.events), 0)
        
        # Verify first event
        first_event = planning.events[0]
        self.assertIsNotNone(first_event.time)
        self.assertIsNotNone(first_event.event_id)
        self.assertIsNotNone(first_event.description)


if __name__ == '__main__':
    unittest.main()
