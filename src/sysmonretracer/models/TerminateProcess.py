import pandas as pd
from dataclasses import dataclass
from sysmonretracer.models.Base import BaseEvent
from sysmonretracer.utils import parse_str_to_datetime

# EventID: 05
@dataclass
class TerminateProcessEvent(BaseEvent):

    @classmethod
    def from_dict(cls, df: pd.DataFrame):
        return cls(
            ProcessGuid=df['Event.EventData.ProcessGuid'],
            ProcessId=df['Event.EventData.ProcessId'],
            ParentProcessGuid=df['Event.EventData.ParentProcessGuid'],
            Timestamp=parse_str_to_datetime(df['Event.EventData.UtcTime']),
        )
