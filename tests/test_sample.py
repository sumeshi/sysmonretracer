import orjson
from pathlib import Path
from evtx import PyEvtxParser

def test_writesamplejson():
    parser = PyEvtxParser("./LM_typical_IIS_webshell_sysmon_1_10_traces.evtx")
    for record in parser.records_json():
        eventid = orjson.loads(record['data'])['Event']['System']['EventID']
        sample = Path('tests/cache/' + str(eventid) + '.json')
        if not sample.exists():
            sample.write_text(record['data'])