from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class NameDisplayer(App):

    def __init__(self):
        super().__init__()
        self.name_list = ['Bob Brown', 'Cat Cyan', 'Oren Ochre']

    def build(self):
        self.title = "Name Displayer"
        self.root = Builder.load_file('name_displayer.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create buttons from dictionary entries and add them to the GUI."""
        for name in self.name_list:
            temp_label = Label(text=name, id=name)
            self.root.ids.entries_label.add_widget(temp_label)


NameDisplayer().run()
