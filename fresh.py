import os
import time
import subprocess
import yaml


def main():
    freshfile = read_freshfile()

    if freshfile['runOnStart']:
        run_command(freshfile['command'])

    observe_path(freshfile['path'], freshfile['command'], freshfile['retentionTime'])


def read_freshfile():
    with open('Freshfile', 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None


def observe_path(path, action, retention_time=1):
    before = dict([(f, None) for f in os.listdir(path)])
    while 1:
        time.sleep(retention_time)
        after = dict([(f, None) for f in os.listdir(path)])
        added = [f for f in after if not f in before]
        removed = [f for f in before if not f in after]
        if added or removed:
            print("Info: change detected")
            run_command(action)
        before = after


def run_command(command):
    result = subprocess.run(command, shell=True, check=True)
    if result.returncode != 0:
        print("Finished command with error:", result)


if __name__ == "__main__":
    main()
