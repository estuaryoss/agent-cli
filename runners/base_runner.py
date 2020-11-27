import click

from utils.command_holder import CommandHolder


class BaseRunner:

    @staticmethod
    def run_command(service, command, keep_state=False, wd=".", wd_cmd="pwd"):
        result = CommandHolder.cmd_check(service=service, command=command)

        if result is None:
            try:
                response = service.send(command=command, keep_state=keep_state, wd=wd, wd_cmd=wd_cmd)
                click.echo(response[0])
            except Exception as e:
                print("\nException({})".format(e.__str__()))
        else:
            click.echo(result)

        return response[1]