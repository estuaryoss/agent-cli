import sys

from utils.ssh_cli import SSHCli


class CommandHolder:
    commands = {
        "quit": {
            "--method": sys.exit,
            "--args": [0]
        },
        "trump": {
            "--method": sys.exit,
            "--args": [0]
        },
        "cli-file --upload": {
            "--method": SSHCli.upload_file,
            "--args": []
        },
        "cli-file --download": {
            "--method": SSHCli.download_file,
            "--args": []
        },
    }

    @classmethod
    def cmd_check(cls, service, command):
        for key in cls.commands.keys():
            if key in command:
                cls.commands.get(key)["--args"] = list(map(lambda x: x.strip(), command.partition("--args")[2].split(";"))) if \
                command.partition("--args")[2] else [0]
                cls.commands.get(key)["--args"].insert(0, service) if command.partition("--args")[2] else None
                print(f"Executed {command}")
                return cls.commands.get(key).get("--method")(*CommandHolder.commands.get(key).get("--args"))

        return None