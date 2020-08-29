#!/usr/bin/env python3

import click

__author__ = "Catalin Dinuta"

from service.restapi_service import RestApiService
from runners.interactive_runner import InteractiveRunner
from runners.non_interactive_runner import NonInteractiveRunner


@click.command()
@click.option('--ip', prompt='ip/hostname',
              help='The IP/hostname of the target machine where estuary-testrunner is deployed')
@click.option('--port', prompt='port',
              help='The port number of the target machine where estuary-testrunner is deployed')
@click.option('--token', prompt='token', hide_input=True,
              help='The authentication token that will be sent via \'Token\' header. '
                   'Use \'None\' if estuary-testrunner is deployed unsecured')
@click.option('--endpoint', help='The endpoint to sent the request. Default is "/command"')
@click.option('--cmds', help='The commands to be sent separated by ";". Useful for non-interactive mode.')
def cli(ip, port, token, endpoint, cmds):
    connection = {
        "ip": ip,
        "port": port,
        "token": token,
        "endpoint": endpoint if endpoint is not None else "/command"
    }
    service = RestApiService(connection)

    # check if can connect
    try:
        service.send("ls")
    except Exception as e:
        print("\nException({})".format(e.__str__()))
        exit(1)

    if cmds is not None:
        NonInteractiveRunner.run_commands(service=service, cmds=cmds)
        exit(0)

    # stay in loop. ctrl+c to exit or send 'quit/trump'
    while True:
        command = input(">> ")
        InteractiveRunner.run_command(service=service, command=command)


if __name__ == "__main__":
    cli()
