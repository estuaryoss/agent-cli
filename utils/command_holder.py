import sys


class CommandHolder:
    commands = {
        "quit": sys.exit,
        "trump": sys.exit
    }

    @staticmethod
    def check_cmd(command):
        if CommandHolder.commands.get(command) is not None:
            print(f"Executed {command}")
            CommandHolder.commands.get(command)(0)
