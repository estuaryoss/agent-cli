#!/usr/bin/env python3
import unittest

from click.testing import CliRunner

from main import cli


class FlaskServerTestCase(unittest.TestCase):
    ip = "localhost"
    port = "8080"
    token = "None"

    def test_cli_invalid_token_n(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "token": "whatsoever"
        }
        command = "ps -ef"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n{cli_args.get('port')}\n{cli_args.get('token')}\n{command}\n")

        self.assertIn("Invalid Token", result.output)

    def test_cli_invalid_ip_n(self):
        cli_args = {
            "ip": "whatsoever",
            "port": self.port,
            "token": self.token
        }
        command = "ps -ef"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n{cli_args.get('port')}\n{cli_args.get('token')}\n{command}\n")

        self.assertIn("Exception", result.output)

    def test_cli_invalid_port_n(self):
        cli_args = {
            "ip": self.ip,
            "port": "15555",
            "token": self.token
        }
        command = "ls"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n{cli_args.get('port')}\n{cli_args.get('token')}\n{command}\n")

        self.assertIn("Exception", result.output)

    def test_cli_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "token": self.token
        }
        command = "ls"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n{cli_args.get('port')}\n{cli_args.get('token')}\n{command}\n")

        self.assertIn("requirements.txt", result.output)

    def test_cli_quit_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "token": self.token
        }
        command = "quit"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n{cli_args.get('port')}\n{cli_args.get('token')}\n{command}\n")

        self.assertIn(f"Executed {command}", result.output)

    def test_cli_trump_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "token": self.token
        }
        command = "trump"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n{cli_args.get('port')}\n{cli_args.get('token')}\n{command}\n")

        self.assertIn(f"Executed {command}", result.output)


if __name__ == '__main__':
    unittest.main()
