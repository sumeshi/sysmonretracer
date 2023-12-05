from sysmonretracer.controller.EvtxController import EvtxController
from sysmonretracer.controller.ModelController import ModelController

import click

__version__ = '0.1.0'

@click.group()
@click.help_option('-h', '--help')
@click.version_option(__version__, '-v', '--version', message='%(prog)s v%(version)s')
def cmd():
    pass


@cmd.command()
@click.argument('query')
@click.argument('eventlog')
@click.option('-sd', '--start-date', help='')
@click.option('-ed', '--end-date', help='')
@click.option('-F', '--fixed-strings', is_flag=False, help='')
@click.help_option('-h', '--help')
def find(
    eventlog: str,
    query: str,
    start_date: str,
    end_date: str,
    fixed_strings: bool,
):
    df = EvtxController.load_to_dataframe(eventlog)
    df['Event.EventData.Image'].str.contains(query, regex=fixed_strings)
    print(df)


@cmd.command()
@click.argument('eventlog')
@click.option('-sd', '--start-date', help='')
@click.option('-ed', '--end-date', help='')
@click.help_option('-h', '--help')
def retrace(
    eventlog: str,
    start_date: str,
    end_date: str,
):
    df = EvtxController.load_to_dataframe(eventlog)
    gen_models = ModelController.generate_models(df)

    for m in gen_models:
        print(m)

if __name__ == '__main__':
    cmd(obj={})
