import click

from utils.command_holder import CommandHolder


class BaseRunner:

    @staticmethod
    def run_command(service, command):
        CommandHolder.check_cmd(command)
        try:
            response = service.send(command)
            click.echo(response)
        except Exception as e:
            print("\nException({})".format(e.__str__()))