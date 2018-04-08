import time

import yaml
from watchdog.observers import Observer

import event_handler
import executors


def main():
    freshfile = read_freshfile()

    executor = executors.Executor(freshfile['commands'])

    if freshfile['runOnStart']:
        executor.execute()

    observe(freshfile['path'], executor)


def read_freshfile():
    with open('Freshfile', 'r') as stream:
        try:
            return yaml.load(stream)
        except yaml.YAMLError as exc:
            print(exc)
            return None


def observe(path, executor):
    observer = Observer()
    observer.schedule(event_handler.ChangeEventHandler(executor), path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    main()
