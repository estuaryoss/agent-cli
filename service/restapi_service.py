import re
import requests
from requests.auth import HTTPBasicAuth

from utils.io_utils import IOUtils


class RestApiService:
    def __init__(self, connection):
        self.conn = connection

    def upload_file(self, remote_path, local_path):
        url_format = f"{self.conn.get('protocol')}://{self.conn.get('ip')}:{self.conn.get('port')}/file"
        headers = {
            "File-Path": remote_path,
            "Content-Type": "application/octet-stream"
        }
        response = requests.post(url_format, headers=headers, data=IOUtils.read_file(local_path),
                                 verify=self.conn.get('cert'),
                                 auth=HTTPBasicAuth(self.conn.get('username'), self.conn.get('password')))

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            raise BaseException("Error: Http code: {}. Http body: {}".format(response.status_code, response.text))

        body = response.json()

        return body.get('description')

    def download_file(self, remote_path, local_path):
        url_format = f"{self.conn.get('protocol')}://{self.conn.get('ip')}:{self.conn.get('port')}/file"
        headers = {
            "File-Path": remote_path,
            "Content-Type": "application/octet-stream"
        }
        response = requests.get(url_format, headers=headers, stream=True, verify=self.conn.get('cert'),
                                auth=HTTPBasicAuth(self.conn.get('username'), self.conn.get('password')))
        response.raw.decode_content = True

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            raise BaseException("Error: Http code: {}.".format(response.status_code))
        IOUtils.write_to_file_binary(local_path, raw_response=response.raw)

        return f"Saved at location {local_path}"

    def send(self, command, keep_state=False, wd=".", wd_cmd="pwd"):
        command = command.strip()
        url_format = f"{self.conn.get('protocol')}://{self.conn.get('ip')}:{self.conn.get('port')}{self.conn.get('endpoint')}"
        headers = {
            "Content-Type": "text/plain"
        }

        cd_cmd = f"cd {wd}&&{command}&&{wd_cmd}" if keep_state else command
        response = requests.post(url_format, headers=headers, data=cd_cmd, timeout=5,
                                 verify=self.conn.get('cert'),
                                 auth=HTTPBasicAuth(self.conn.get('username'), self.conn.get('password')))

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            raise BaseException("Error: Http code: {}. Http body: {}".format(response.status_code, response.text))

        body = response.json()

        # error, the type should be dict
        if isinstance(body['description'], str):
            return body.get('description'), wd

        details = body.get('description').get('commands').get(cd_cmd).get('details')
        if re.compile(r"cd\s+(.*)").search(command) and details.get('out') and keep_state:
            wd = details.get('out').split("\n")[-2]

        return details.get('out') if details.get('err') == "" else details.get('err'), wd.rstrip()

    def about(self):
        url_format = f"{self.conn.get('protocol')}://{self.conn.get('ip')}:{self.conn.get('port')}/about"
        headers = {
            "Content-Type": "application/json"
        }

        response = requests.get(url_format, headers=headers, timeout=5, verify=self.conn.get('cert'),
                                auth=HTTPBasicAuth(self.conn.get('username'), self.conn.get('password')))

        # error, server sent non 200 OK response code
        if response.status_code != 200:
            raise BaseException("Error: Http code: {}. Http body: {}".format(response.status_code, response.text))

        body = response.json()

        # error, the type should be dict
        if isinstance(body['description'], str):
            return body.get('description')

        return body.get('description')

    def get_os(self):
        return self.about().get("system")

    def get_wd_cmd(self):
        pwd_cmd = "cd" if self.get_os().lower() == "Windows".lower() else "pwd"

        return pwd_cmd
