from guizero import App, Text, PushButton
from Utils import clear_screen
from os import listdir

app = App(title='Luminosity3D',width=800,height=480)


files = listdir('print_files')

def home_page():
    """
    Actions
    """
    clear_screen(app)
    """
    Components
    """
    intro = Text(app, text='Luminosity3D')
    print = PushButton(app, text='Print', command=view_files)
    view_file = PushButton(app, text='View File')

def view_files():
    """
    Actions
    """
    clear_screen(app)
    """
    Components
    """
    for file in files:
        PushButton(app, text=file)
    PushButton(app, text='Go back', command=home_page)

home_page()
app.display()