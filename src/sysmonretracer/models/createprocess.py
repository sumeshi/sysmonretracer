import pandas as pd
from dataclasses import dataclass
from sysmonretracer.models.base import BaseEvent
from sysmonretracer.utils import parse_str_to_datetime

# EventID: 01
@dataclass
class CreateProcessEvent(BaseEvent):

    @classmethod
    def from_dict(cls, df: pd.DataFrame):
        return cls(
            ProcessGuid=df['Event.EventData.ProcessGuid'],
            ProcessId=df['Event.EventData.ProcessId'],
            ParentProcessGuid=df['Event.EventData.ParentProcessGuid'],
            EventId=df['Event.System.EventID'],
            Timestamp=parse_str_to_datetime(df['Event.EventData.UtcTime']),
        )
