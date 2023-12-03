from sysmonretracer.models.Base import BaseEvent
from sysmonretracer.models.CreateProcess import CreateProcessEvent
from sysmonretracer.models.TerminateProcess import TerminateProcessEvent

import pandas as pd


class ModelController(object):
    models = {
        1: CreateProcessEvent,
        5: TerminateProcessEvent,
    }

    @staticmethod
    def generate_models(df: pd.DataFrame) -> BaseEvent:
        for _, df in df.iterrows():
            try:
                event_model = ModelController.models[df['Event.System.EventID']]
                event = event_model.from_dict(df)
                yield event

            except KeyError:
                pass