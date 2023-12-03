from pprint import pprint
from sysmonretracer.models.createprocess import CreateProcessEvent

import orjson
from evtx import PyEvtxParser

def main():
    models = {
        1: CreateProcessEvent,
    }

    parser = PyEvtxParser("./LM_typical_IIS_webshell_sysmon_1_10_traces.evtx")
    for record in parser.records_json():
        d = orjson.loads(record['data'])

        event_model = models[d['Event']['System']['EventID']]
        event = event_model.from_dict(d)
        print(event)

        # try:
        # except:
        #     pass
        #     pprint(d)

if __name__ == '__main__':
    main()