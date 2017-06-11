import os

# external imports
import click


@click.group(name="django")
def django():
    """ django manangement command"""
    pass


@click.command(name="manage")
@click.argument('args', nargs=-1)
def manage(args):
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "invento.conf.settings")

    args = [elem for elem in args]
    args.insert(0, 'manage')

    try:
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(args)

django.add_command(manage)
