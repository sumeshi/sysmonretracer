from abc import ABCMeta, abstractclassmethod
from datetime import datetime
from dataclasses import dataclass

@dataclass
class BaseEvent(metaclass=ABCMeta):
    ProcessGuid: str
    ProcessId: int
    ParentProcessGuid: str
    EventId: int
    Timestamp: datetime

    @abstractclassmethod
    def from_dict(cls):
        pass