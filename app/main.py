import os


class CleanUpFile:
    def __init__(self, filename):
        self.filename = filename
    def __enter__(self):
        return self
    def __exit__(self, type, value, traceback):
        if os.path.isfile(self.filename):
            os.remove(self.filename)
