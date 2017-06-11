import click

# internal imports
from invento.commands.django import django


@click.group()
@click.option('--verbose', '-v', default=False, help='Show verbose logs')
def main(verbose):
    """ invento cli commands"""
    pass

main.add_command(django)
