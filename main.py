import click

__author__ = "Catalin Dinuta"

from service.restapi_service import RestApiService
from utils.command_holder import CommandHolder


@click.command()
@click.option('--ip', prompt='ip/hostname',
              help='The IP/hostname of the target machine where estuary-testrunner is running')
@click.option('--port', prompt='port',
              help='The port number of the target machine where estuary-testrunner is running')
@click.option('--token', prompt='Auth token [Use \'None\' if estuary-testrunner is not secured]', hide_input=True,
              help='The authentication token that will be sent via \'Token\' header')
def cli(ip, port, token):
    connection = {
        "ip": ip,
        "port": port,
        "token": token
    }
    service = RestApiService(connection)

    # check if can connect
    try:
        service.send("whatever because does not matter")
    except Exception as e:
        print("\nException({0})".format(e.__str__()))
        exit(1)

    # stay in loop. ctrl+c to exit or send 'quit'
    while True:
        command = input(">> ")
        CommandHolder.check_cmd(command)
        try:
            response = service.send(command)
            click.echo(response)
        except Exception as e:
            print("\nException({0})".format(e.__str__()))


if __name__ == "__main__":
    cli()
