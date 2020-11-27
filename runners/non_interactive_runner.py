from runners.base_runner import BaseRunner


class NonInteractiveRunner(BaseRunner):

    @staticmethod
    def run_commands(service, cmds, keep_state=False, wd=".", wd_cmd="pwd"):
        commands = cmds.split(";;")
        if len(commands) != 0:
            for command in commands:
                BaseRunner.run_command(service=service, command=command, keep_state=keep_state, wd=wd, wd_cmd=wd_cmd)
