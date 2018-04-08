from watchdog.events import FileSystemEventHandler


class ChangeEventHandler(FileSystemEventHandler):

    def __init__(self, executor, ignores):
        self.__executor = executor
        self.__ignores = ignores

    def on_moved(self, event):
        if self.is_ignored(event.src_path):
            return
        print("Detect move change in: ", event)
        self.__executor.execute(event)

    def on_created(self, event):
        if self.is_ignored(event.src_path):
            return
        print("Detect create change in: ", event)
        self.__executor.execute()

    def on_deleted(self, event):
        if self.is_ignored(event.src_path):
            return
        print("Detect delete change in: ", event)
        self.__executor.execute()

    def on_modified(self, event):
        if self.is_ignored(event.src_path):
            return
        print("Detect modify change in: ", event)
        self.__executor.execute()

    def is_ignored(self, file):
        for ignore in self.__ignores:
            if ignore in file:
                return True
        return False
