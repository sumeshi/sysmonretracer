from sysmonretracer.controller.EvtxController import EvtxController
from sysmonretracer.controller.ModelController import ModelController

import click

__version__ = '0.1.0'

@click.group()
@click.help_option('-h', '--help')
@click.version_option(__version__, '-v', '--version', message='v%(version)s')
def cmd():
    pass


@cmd.command()
@click.argument('query')
@click.argument('eventlog')
@click.option('-k', '--key', type=click.Choice(['commandline', 'hash', 'image'], case_sensitive=False), default='image', help='')
@click.option('-i', '--ignore-case', is_flag=True, help='')
@click.option('-F', '--fixed-strings', is_flag=True, help='')
@click.option('-sd', '--start-date', help='')
@click.option('-ed', '--end-date', help='')
@click.help_option('-h', '--help')
def find(
    query: str,
    eventlog: str,
    key: str,
    ignore_case: bool,
    fixed_strings: bool,
    start_date: str,
    end_date: str,
):
    key_dict = {
        'commandline': 'Event.EventData.CommandLine',
        'hash': 'Event.EventData.Hashes',
        'image': 'Event.EventData.Image',
    }
    
    df = EvtxController.load_to_dataframe(eventlog)
    df = df[df[key_dict.get(key)].str.contains(query, regex=not fixed_strings, case=not ignore_case, na=False)]
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
