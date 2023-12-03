from dataclasses import dataclass
from sysmonretracer.models.base import BaseEvent
from sysmonretracer.utils import parse_str_to_datetime

# EventID: 01
@dataclass
class CreateProcessEvent(BaseEvent):

    @classmethod
    def from_dict(cls, d: dict):
        return cls(
            ProcessGuid=d['Event']['EventData']['ProcessGuid'],
            ProcessId=d['Event']['EventData']['ProcessId'],
            ParentProcessGuid=d['Event']['EventData']['ParentProcessGuid'],
            EventId=d['Event']['System']['EventID'],
            Timestamp=parse_str_to_datetime(d['Event']['EventData']['UtcTime']),
        )
