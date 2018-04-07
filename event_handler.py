import subprocess

from watchdog.events import FileSystemEventHandler


class ChangeEventHandler(FileSystemEventHandler):

    def __init__(self, command):
        self.__command = command

    def on_moved(self, event):
        self.run_command()

    def on_created(self, event):
        self.run_command()

    def on_deleted(self, event):
        self.run_command()

    def on_modified(self, event):
        self.run_command()

    def run_command(self):
        result = subprocess.run(self.__command, shell=True, check=True)
        if result.returncode != 0:
            print("Finished command with error:", result)
