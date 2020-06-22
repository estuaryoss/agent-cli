import re
import requests


class RestApiService:
    def __init__(self, connection):
        self.connection = connection

    def send(self, command):
        url_format = f"http://{self.connection.get('ip')}:{self.connection.get('port')}/command"
        headers = {
            "Token": self.connection.get('token'),
            "Content-Type": "text/plain"
        }

        # return prompt if empty or spaces
        if re.compile(r"^\s+$").search(command) or command == "":
            return ""

        response = requests.post(url_format, headers=headers, data=command, timeout=5)

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            return "Error: Http code: {}. Http body: {}".format(response.status_code, response.text)

        body = response.json()

        # error, the type should be dict
        if isinstance(body['description'], str):
            return body.get('description')

        details = body.get('description').get('commands').get(command).get('details')
        return details.get('out') if details.get('err') == "" else details.get('err')
