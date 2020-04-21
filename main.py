import click

__author__ = "Catalin Dinuta"

from service.restapi_service import RestApiService


@click.command()
@click.option('--ip', prompt='ip/hostname',
              help='The IP/hostname of the target machine where estuary-testrunner is running')
@click.option('--port', prompt='port',
              help='The port number of the target machine where estuary-testrunner is running')
@click.option('--token', prompt='Auth token [Use \'None\' if estuary-testrunner is not secured]', hide_input=True,
              confirmation_prompt=True, help='The authentication token that will be sent via \'Token\' header')
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

    # stay in loop. ctrl+c to exit
    while True:
        commands = input(">> ")
        response = service.send(commands)
        click.echo(response)


if __name__ == "__main__":
    cli()
