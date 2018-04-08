from watchdog.events import FileSystemEventHandler


class ChangeEventHandler(FileSystemEventHandler):

    def __init__(self, executor):
        self.__executor = executor

    def on_moved(self, event):
        print("Detect move change in: ", event)
        self.__executor.execute()

    def on_created(self, event):
        print("Detect create change in: ", event)
        self.__executor.execute()

    def on_deleted(self, event):
        print("Detect delete change in: ", event)
        self.__executor.execute()

    def on_modified(self, event):
        print("Detect modify change in: ", event)
        self.__executor.execute()
