import os
import tempfile


class File:
    def __init__(self, filename):
        self.filename = filename
        if not os.path.exists(filename):
            with open(filename, 'w') as f:
                f.write('')

    def __add__(self, other):
        obj = File(os.path.join(tempfile.gettempdir(), str(hash(self)) + str(hash(other))))
        obj.write(self.read() + other.read())
        return obj

    def __str__(self):
        return self.filename

    def __iter__(self):
        with open(self.filename) as f:
            self.lines = iter(f.readlines())
        return self

    def __next__(self):
        return next(self.lines)

    def read(self):
        with open(self.filename, 'r') as f:
            return f.read()

    def write(self, text):
        with open(self.filename, 'w') as f:
            f.write(text)
