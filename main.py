#!/usr/bin/env python3

__author__ = "Catalin Dinuta"

import click
import re
import yaml

from about import properties
from runners.interactive_runner import InteractiveRunner
from runners.non_interactive_runner import NonInteractiveRunner
from service.restapi_service import RestApiService


@click.command()
@click.option('--ip', prompt='ip/hostname',
              help='The IP/hostname of the target machine where Agent is deployed')
@click.option('--port', type=int, prompt='port',
              help='The port number of the target machine where Agent is deployed')
@click.option('--username', prompt='username',
              help='The username used for the Basic authentication')
@click.option('--password', prompt='password', hide_input=True,
              help='The password used for the Basic authentication')
@click.option('--protocol', help='The protocol with which the Agent was deployed. Default is http. E.g. https')
@click.option('--cert', help='The certificate with which the Agent was deployed. E.g. https/cert.pem')
@click.option('--endpoint', help='The endpoint to sent the request. Default is "/command"')
@click.option('--keep_state', type=bool, default=False,
              help='Whenever to keep the current working dir. Default is "False"')
@click.option('--cmds', help='The commands to be sent separated by ";". Useful for non-interactive mode.')
def cli(ip, port, username, password, protocol, cert, endpoint, keep_state, cmds):
    click.echo(f"CLI version: {properties.get('version')}\n")

    connection = {
        "ip": ip,
        "port": port,
        "username": username,
        "password": password,
        "protocol": protocol if protocol is not None else "http",
        "cert": cert if cert is not None else "https/cert.pem",
        "endpoint": endpoint if endpoint is not None else "/commands"
    }
    service = RestApiService(connection)

    # check if can connect
    try:
        service.send("echo hello")
    except Exception as e:
        print("\nException({})".format(e.__str__()))
        exit(1)

    click.echo(f"Worker information: \n{yaml.dump(service.about())}\n")

    wo_dir = "."  # remote path on the agent
    wo_dir_cmd = service.get_wd_cmd()

    if cmds is not None:
        NonInteractiveRunner.run_commands(service=service, cmds=cmds, keep_state=keep_state, wd=wo_dir,
                                          wd_cmd=wo_dir_cmd)
        exit(0)

    # stay in loop. ctrl+c to exit or send '-quit/-trump'
    while True:
        command = input(">> ")
        command = command.strip()

        # return prompt if empty or just tabs or spaces
        if re.compile(r"^\s+$").search(command) or command == "":
            continue
        wo_dir = InteractiveRunner.run_command(service=service, command=command, keep_state=keep_state, wd=wo_dir,
                                               wd_cmd=wo_dir_cmd)


if __name__ == "__main__":
    cli()
