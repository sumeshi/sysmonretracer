from sysmonretracer.controller.EvtxController import EvtxController
from sysmonretracer.controller.ModelController import ModelController

import click

__version__ = '0.1.0'

@click.command()
@click.argument('eventlog')
# @click.option('-sd', '--start-date', help='')
# @click.option('-ed', '--end-date', help='')
@click.help_option('-h', '--help')
@click.version_option(__version__, '-v', '--version', message='%(prog)s v%(version)s')
def main(
    eventlog: str,
    start_date: str,
    end_date: str,
):
    df = EvtxController.load_to_dataframe(eventlog)
    gen_models = ModelController.generate_models(df)

    for m in gen_models:
        print(m)

if __name__ == '__main__':
    main()
