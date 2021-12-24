from guizero import App, Text, PushButton

def clear_screen(app):
    while len(app.children) > 0:
        app.children[0].destroy()

class File:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory
