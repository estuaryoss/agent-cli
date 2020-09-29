import click

from utils.command_holder import CommandHolder


class BaseRunner:

    @staticmethod
    def run_command(service, command):
        result = CommandHolder.cmd_check(service=service, command=command)

        if result is None:
            try:
                response = service.send(command)
                click.echo(response)
            except Exception as e:
                print("\nException({})".format(e.__str__()))
        else:
            click.echo(result)
