import re

import requests

from utils.io_utils import IOUtils


class RestApiService:
    def __init__(self, connection):
        self.connection = connection

    def upload_file(self, remote_path, local_path):
        url_format = f"{self.connection.get('protocol')}://{self.connection.get('ip')}:{self.connection.get('port')}/file"
        headers = {
            "Token": self.connection.get('token'),
            "File-Path": remote_path,
            "Content-Type": "application/octet-stream"
        }
        response = requests.post(url_format, headers=headers, data=IOUtils.read_file(local_path), verify=self.connection.get('cert'))

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            return "Error: Http code: {}. Http body: {}".format(response.status_code, response.text)

        body = response.json()

        return body.get('description')

    def download_file(self, remote_path, local_path):
        url_format = f"{self.connection.get('protocol')}://{self.connection.get('ip')}:{self.connection.get('port')}/file"
        headers = {
            "Token": self.connection.get('token'),
            "File-Path": remote_path,
            "Content-Type": "application/octet-stream"
        }
        response = requests.get(url_format, headers=headers, stream=True, verify=self.connection.get('cert'))
        response.raw.decode_content = True

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            return "Error: Http code: {}.".format(response.status_code)
        IOUtils.write_to_file_binary(local_path, raw_response=response.raw)

        return f"File content was saved at location {local_path}"

    def send(self, command):
        command = command.strip()
        url_format = f"{self.connection.get('protocol')}://{self.connection.get('ip')}:{self.connection.get('port')}{self.connection.get('endpoint')}"
        headers = {
            "Token": self.connection.get('token'),
            "Content-Type": "text/plain"
        }

        # return prompt if empty or spaces
        if re.compile(r"^\s+$").search(command) or command == "":
            return ""

        response = requests.post(url_format, headers=headers, data=command, timeout=5, verify=self.connection.get('cert'))

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            return "Error: Http code: {}. Http body: {}".format(response.status_code, response.text)

        body = response.json()

        # error, the type should be dict
        if isinstance(body['description'], str):
            return body.get('description')

        details = body.get('description').get('commands').get(command).get('details')
        return details.get('out') if details.get('err') == "" else details.get('err')
