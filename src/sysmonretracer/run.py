import io
from pprint import pprint
from sysmonretracer.models.createprocess import CreateProcessEvent

import orjson
import pandas as pd
from evtx import PyEvtxParser

def main():
    models = {
        1: CreateProcessEvent,
    }

    parser = PyEvtxParser("./LM_typical_IIS_webshell_sysmon_1_10_traces.evtx")
    df = pd.concat([pd.json_normalize(orjson.loads(r['data'])) for r in parser.records_json()])

    for _, df in df.iterrows():
        try:
            event_model = models[df['Event.System.EventID']]
            event = event_model.from_dict(df)
            print(event)
        except KeyError:
            pass

if __name__ == '__main__':
    main()