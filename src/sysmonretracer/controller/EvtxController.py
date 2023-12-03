import orjson
import pandas as pd
from evtx import PyEvtxParser

class EvtxController(object):

    @staticmethod
    def load_to_dataframe(evtxfile_path: str) -> pd.DataFrame:
        parser = PyEvtxParser(evtxfile_path)
        df = pd.concat([pd.json_normalize(orjson.loads(r['data'])) for r in parser.records_json()])
        return df
