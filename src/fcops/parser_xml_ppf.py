"""
Parser for FLEX mission planning XML files (FLX_OPER_MPL_*.xml).

This module provides functionality to decode and parse Delta Nominal Payload Planning Files (DNPPF),
Ground Station Planning Files (GSPLN), and other planning files in XML format.
"""

import xml.etree.ElementTree as ET
from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Any
from datetime import datetime


@dataclass
class Header:
    """Header information from the XML file."""
    format_version: str
    gen_time: datetime
    validity_start: datetime
    validity_end: datetime
    spacecraft: str
    purpose: str
    icd_version: str
    filename: str

    @classmethod
    def from_element(cls, element: ET.Element) -> 'Header':
        """Create a Header from an XML element."""
        return cls(
            format_version=element.get('format_version', ''),
            gen_time=_parse_datetime(element.get('gen_time', '')),
            validity_start=_parse_datetime(element.get('validity_start', '')),
            validity_end=_parse_datetime(element.get('validity_end', '')),
            spacecraft=element.get('spacecraft', ''),
            purpose=element.get('purpose', ''),
            icd_version=element.get('icd_version', ''),
            filename=element.get('filename', ''),
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert header to dictionary."""
        return {
            'format_version': self.format_version,
            'gen_time': self.gen_time.isoformat() if self.gen_time else None,
            'validity_start': self.validity_start.isoformat() if self.validity_start else None,
            'validity_end': self.validity_end.isoformat() if self.validity_end else None,
            'spacecraft': self.spacecraft,
            'purpose': self.purpose,
            'icd_version': self.icd_version,
            'filename': self.filename,
        }


@dataclass
class Event:
    """Represents a single event in the planning file."""
    time: datetime
    event_id: str
    description: str
    source: str
    event_type: str
    count: int
    absolute_orbit: int
    relative_orbit: int
    sec_from_anx: float
    deg_from_anx: float
    group_id: int
    parameter_count: int
    is_event: bool = True
    parameters: Dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_element(cls, element: ET.Element) -> 'Event':
        """Create an Event from an XML element."""
        # Extract standard attributes
        params = {}
        
        # Get all attributes from the element
        all_attrs = element.attrib
        
        # Extract and remove standard attributes
        time = _parse_datetime(all_attrs.get('time', ''))
        event_id = all_attrs.get('id', '')
        description = all_attrs.get('description', '')
        source = all_attrs.get('source', '')
        event_type = all_attrs.get('type', '')
        count = _parse_int(all_attrs.get('count', '0'))
        absolute_orbit = _parse_int(all_attrs.get('absolute_orbit', '0'))
        relative_orbit = _parse_int(all_attrs.get('relative_orbit', '0'))
        sec_from_anx = _parse_float(all_attrs.get('sec_from_anx', '0'))
        deg_from_anx = _parse_float(all_attrs.get('deg_from_anx', '0'))
        group_id = _parse_int(all_attrs.get('group_id', '0'))
        parameter_count = _parse_int(all_attrs.get('parameter_count', '0'))
        is_event = all_attrs.get('isEvent', 'true').lower() == 'true'
        
        # Standard attributes to exclude from parameters
        standard_attrs = {
            'time', 'id', 'description', 'source', 'type', 'count',
            'absolute_orbit', 'relative_orbit', 'sec_from_anx', 'deg_from_anx',
            'group_id', 'parameter_count', 'isEvent'
        }
        
        # Remaining attributes are parameters
        for key, value in all_attrs.items():
            if key not in standard_attrs:
                # Try to convert to number if possible
                params[key] = _try_convert_value(value)
        
        return cls(
            time=time,
            event_id=event_id,
            description=description,
            source=source,
            event_type=event_type,
            count=count,
            absolute_orbit=absolute_orbit,
            relative_orbit=relative_orbit,
            sec_from_anx=sec_from_anx,
            deg_from_anx=deg_from_anx,
            group_id=group_id,
            parameter_count=parameter_count,
            is_event=is_event,
            parameters=params,
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert event to dictionary."""
        return {
            'time': self.time.isoformat() if self.time else None,
            'event_id': self.event_id,
            'description': self.description,
            'source': self.source,
            'event_type': self.event_type,
            'count': self.count,
            'absolute_orbit': self.absolute_orbit,
            'relative_orbit': self.relative_orbit,
            'sec_from_anx': self.sec_from_anx,
            'deg_from_anx': self.deg_from_anx,
            'group_id': self.group_id,
            'parameter_count': self.parameter_count,
            'is_event': self.is_event,
            'parameters': self.parameters,
        }


@dataclass
class PlanningFile:
    """Represents a complete planning file document."""
    header: Header
    events: List[Event] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert planning file to dictionary."""
        return {
            'header': self.header.to_dict(),
            'events': [event.to_dict() for event in self.events],
        }

    def get_events_by_id(self, event_id: str) -> List[Event]:
        """Get all events with a specific ID."""
        return [e for e in self.events if e.event_id == event_id]

    def get_events_by_type(self, event_type: str) -> List[Event]:
        """Get all events of a specific type."""
        return [e for e in self.events if e.event_type == event_type]

    def get_events_by_time_range(self, start: datetime, end: datetime) -> List[Event]:
        """Get all events within a specific time range."""
        return [e for e in self.events if start <= e.time <= end]

    def get_events_by_orbit(self, orbit: int) -> List[Event]:
        """Get all events for a specific orbit."""
        return [e for e in self.events if e.absolute_orbit == orbit]


def parse_file(filepath: str) -> PlanningFile:
    """
    Parse a FLEX planning XML file.
    
    Args:
        filepath: Path to the XML file to parse.
        
    Returns:
        PlanningFile object containing the parsed data.
        
    Raises:
        FileNotFoundError: If the file does not exist.
        ET.ParseError: If the XML is malformed.
    """
    tree = ET.parse(filepath)
    root = tree.getroot()
    
    # Parse header
    header_elem = root.find('header')
    if header_elem is None:
        raise ValueError("No header element found in XML file")
    header = Header.from_element(header_elem)
    
    # Parse events
    events = []
    events_elem = root.find('events')
    if events_elem is not None:
        for event_elem in events_elem.findall('event'):
            events.append(Event.from_element(event_elem))
    
    return PlanningFile(header=header, events=events)


def parse_file_string(xml_string: str) -> PlanningFile:
    """
    Parse a FLEX planning XML from a string.
    
    Args:
        xml_string: XML content as a string.
        
    Returns:
        PlanningFile object containing the parsed data.
        
    Raises:
        ET.ParseError: If the XML is malformed.
    """
    root = ET.fromstring(xml_string)
    
    # Parse header
    header_elem = root.find('header')
    if header_elem is None:
        raise ValueError("No header element found in XML string")
    header = Header.from_element(header_elem)
    
    # Parse events
    events = []
    events_elem = root.find('events')
    if events_elem is not None:
        for event_elem in events_elem.findall('event'):
            events.append(Event.from_element(event_elem))
    
    return PlanningFile(header=header, events=events)


# Helper functions
def _parse_datetime(datetime_str: str) -> Optional[datetime]:
    """Parse ISO format datetime string."""
    if not datetime_str:
        return None
    try:
        # Remove 'Z' suffix if present and parse
        if datetime_str.endswith('Z'):
            datetime_str = datetime_str[:-1] + '+00:00'
        return datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
    except (ValueError, AttributeError):
        # Fallback for Python < 3.7
        try:
            return datetime.strptime(datetime_str.replace('Z', ''), '%Y-%m-%dT%H:%M:%S.%f')
        except ValueError:
            try:
                return datetime.strptime(datetime_str.replace('Z', ''), '%Y-%m-%dT%H:%M:%S')
            except ValueError:
                return None


def _parse_int(value: str) -> int:
    """Parse integer, returning 0 if invalid."""
    try:
        return int(value)
    except (ValueError, TypeError):
        return 0


def _parse_float(value: str) -> float:
    """Parse float, returning 0.0 if invalid."""
    try:
        return float(value)
    except (ValueError, TypeError):
        return 0.0


def _try_convert_value(value: str) -> Any:
    """Try to convert a string value to the appropriate type."""
    # Try int
    try:
        return int(value)
    except ValueError:
        pass
    
    # Try float
    try:
        return float(value)
    except ValueError:
        pass
    
    # Return as string
    return value
