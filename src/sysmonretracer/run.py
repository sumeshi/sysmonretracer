import sys
from sysmonretracer.controller.EvtxController import EvtxController
from sysmonretracer.controller.ModelController import ModelController

def main():
    df = EvtxController.load_to_dataframe(sys.argv[1])
    gen_models = ModelController.generate_models(df)

    for m in gen_models:
        print(m)

if __name__ == '__main__':
    main()