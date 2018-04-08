import subprocess


class Executor:

    def __init__(self, commands):
        self.__commands = commands

    def execute(self):
        for command in self.__commands:
            print("execute command:", command)
            result = subprocess.run(command, shell=True, check=True)
            if result.returncode != 0:
                print("Finished command with error:", result)

