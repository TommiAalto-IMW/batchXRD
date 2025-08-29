from tkinter import Text
class TextOut(Text):
    def __init__(self, master, **kw):
        super().__init__(master, **kw)

    # required output function for a file-like object
    def write(self, message):
        self.insert("insert", message)