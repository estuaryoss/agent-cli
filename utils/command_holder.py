class CommandHolder:
    commands = {
        "quit": exit,
        "trump": exit,
    }

    @staticmethod
    def check_cmd(command):
        if CommandHolder.commands.get(command) is not None:
            print(f"Executed {command}")
            CommandHolder.commands.get(command)()
