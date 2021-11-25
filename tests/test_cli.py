#!/usr/bin/env python3
import unittest
from click.testing import CliRunner

from main import cli
from tests.cmd_utils import CmdUtils


class FlaskServerTestCase(unittest.TestCase):
    ip = "localhost"
    port = "8080"
    username = "admin"
    password = "estuaryoss123!"
    cmds = "ls"
    endpoint = "/docker/command"

    def test_cli_invalid_password_n(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": "invalidPasswd"
        }
        command = "ps -ef"

        runner = CliRunner()
        try:
            runner.invoke(cli,
                          input=f"{cli_args.get('ip')}\n"
                                f"{cli_args.get('port')}\n"
                                f"{cli_args.get('username')}\n"
                                f"{cli_args.get('password')}\n"
                                f"{command}\n")
        except BaseException as e:
            self.assertIn("401", e.__str__())

    def test_cli_invalid_ip_n(self):
        cli_args = {
            "ip": "whatsoever",
            "port": self.port,
            "username": self.username,
            "password": self.password,
        }
        command = "ps -ef"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}\n"
                                     f"{command}\n")
        self.assertIn("Exception", result.output)

    def test_cli_invalid_port_n(self):
        cli_args = {
            "ip": self.ip,
            "port": "15555",
            "username": self.username,
            "password": self.password,
        }
        command = "ls"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}\n"
                                     f"{command}\n")

        self.assertIn("Exception", result.output)

    def test_cli_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        command = self.cmds

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}\n"
                                     f"{command}\n")

        self.assertIn("requirements.txt", result.output)

    def test_cli_non_interactive_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "cmds": self.cmds
        }
        response = CmdUtils.run_cmd_shell_true(f"python main.py "
                                               f"--ip={cli_args.get('ip')} "
                                               f"--port={cli_args.get('port')} "
                                               f"--username={cli_args.get('username')} "
                                               f"--password={cli_args.get('password')} "
                                               f"--cmds={cli_args.get('cmds')}")

        self.assertEqual(0, response.get('code'))
        self.assertIn("requirements.txt", response.get('out'))

    def test_cli_non_interactive_file_down_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "cmds": "-get --args README.md;ceva.md;;-trump"
        }
        response = CmdUtils.run_cmd_shell_true(f"python main.py "
                                               f"--ip={cli_args.get('ip')} "
                                               f"--port={cli_args.get('port')} "
                                               f"--username={cli_args.get('username')} "
                                               f"--password={cli_args.get('password')} "
                                               f"--cmds=\"{cli_args.get('cmds')}\"")

        # print(response.get("err"))
        self.assertIn("Saved at location", response.get('out'))
        self.assertEqual(0, response.get('code'))

    def test_cli_non_interactive_file_up_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "cmds": "-put --args README.md;altceva.md;;-trump"
        }
        response = CmdUtils.run_cmd_shell_true(f"python main.py "
                                               f"--ip={cli_args.get('ip')} "
                                               f"--port={cli_args.get('port')} "
                                               f"--username={cli_args.get('username')} "
                                               f"--password={cli_args.get('password')} "
                                               f"--cmds=\"{cli_args.get('cmds')}\"")

        # print(response.get("err"))
        self.assertIn("Success", response.get('out'))
        self.assertEqual(0, response.get('code'))

    def test_cli_non_interactive_multiple_cmds_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "cmds": self.cmds
        }
        response = CmdUtils.run_cmd_shell_true(f"python main.py "
                                               f"--ip={cli_args.get('ip')} "
                                               f"--port={cli_args.get('port')} "
                                               f"--username={cli_args.get('username')} "
                                               f"--password={cli_args.get('password')} "
                                               f"--cmds=\"{cli_args.get('cmds')};;cat requirements.txt\"")

        self.assertIn("requirements.txt", response.get('out'))
        self.assertIn("pyinstaller", response.get('out'))
        self.assertEqual(0, response.get('code'))

    def test_cli_non_interactive_stateful_wd_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "keep_state": True,
            "cmds": "cd docs;;ls;;-trump"
        }
        response = CmdUtils.run_cmd_shell_true(f"python main.py "
                                               f"--ip={cli_args.get('ip')} "
                                               f"--port={cli_args.get('port')} "
                                               f"--username={cli_args.get('username')} "
                                               f"--password={cli_args.get('password')} "
                                               f"--keep_state={cli_args.get('keep_state')} "
                                               f"--cmds=\"{cli_args.get('cmds')}\"")

        self.assertIn("images", response.get('out'))
        self.assertEqual(0, response.get('code'))

    def test_cli_non_interactive_different_endpoint_n(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password,
            "cmds": self.cmds,
            "endpoint": self.endpoint
        }
        response = CmdUtils.run_cmd_shell_true(f"python main.py "
                                               f"--ip={cli_args.get('ip')} "
                                               f"--port={cli_args.get('port')} "
                                               f"--username={cli_args.get('username')} "
                                               f"--password={cli_args.get('password')} "
                                               f"--cmds=\"{cli_args.get('cmds')}\" "
                                               f"--endpoint={cli_args.get('endpoint')}")

        self.assertIn("Error: Http code: 404", response.get('err'))

    def test_cli_empty_command_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        command = " \n \n \n      \n \n \n \n \n \n \n"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}"
                                     f"\n{command}")

        self.assertEqual(result.output.count(">>"), command.count("\n") + 1)

    def test_cli_command_with_spaces_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        command = "ca"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}\n"
                                     f"{command}  \n")

        self.assertIn(command, result.output)
        self.assertIn("not", result.output)

    def test_cli_command_with_tabs_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        command = "ca"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}\n"
                                     f"{command}\t\t  \n")

        self.assertIn(command, result.output)
        self.assertIn("not", result.output)

    def test_cli_quit_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        command = "-quit"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}\n"
                                     f"{command}\n")

        self.assertIn(f"Executed {command}", result.output)

    def test_cli_trump_p(self):
        cli_args = {
            "ip": self.ip,
            "port": self.port,
            "username": self.username,
            "password": self.password
        }
        command = "-trump"

        runner = CliRunner()
        result = runner.invoke(cli,
                               input=f"{cli_args.get('ip')}\n"
                                     f"{cli_args.get('port')}\n"
                                     f"{cli_args.get('username')}\n"
                                     f"{cli_args.get('password')}\n"
                                     f"{command}\n")

        self.assertIn(f"Executed {command}", result.output)


if __name__ == '__main__':
    unittest.main()
