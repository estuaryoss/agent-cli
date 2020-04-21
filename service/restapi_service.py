import requests


class RestApiService:
    def __init__(self, connection):
        self.connection = connection

    def send(self, command):
        url_format = f"http://{self.connection.get('ip')}:{self.connection.get('port')}/command"
        body = requests.post(url_format, headers={'Token': self.connection.get('token')}, data=command, timeout=5).json()

        # here an error occurred, because the type should be dict
        if type(body['message']) is str:
            return body.get('message')

        details = body.get('message').get('commands').get(command).get('details')

        return details.get('out') if details.get('err') == "" else details.get('err')
