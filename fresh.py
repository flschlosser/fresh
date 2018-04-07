import time

import yaml
from watchdog.observers import Observer

import event_handler


def main():
    freshfile = read_freshfile()

    # if freshfile['runOnStart']:
    #     run_command(freshfile['command'])

    observe(freshfile['path'], freshfile['command'])


def read_freshfile():
    with open('Freshfile', 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None


def observe(path, command):
    observer = Observer()
    observer.schedule(event_handler.ChangeEventHandler(command), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
