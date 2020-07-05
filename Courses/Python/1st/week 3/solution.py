class FileReader:
    def __init__(self, filepath):
        self.filepath = filepath

    def read(self):
        try:
            with open(self.filepath, 'r') as f:
                text = f.read()
        except FileNotFoundError:
            return ''
        else:
            return text
