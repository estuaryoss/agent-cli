from runners.base_runner import BaseRunner


class NonInteractiveRunner(BaseRunner):

    @staticmethod
    def run_commands(service, cmds):
        commands = cmds.split(";;")
        if len(commands) != 0:
            for command in commands:
                BaseRunner.run_command(service=service, command=command)
