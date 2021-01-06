from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label

class DynamicLabelApp(App):

    name_people = {"Bob Brown", "Cat Cyan", "Oren Ochre"}
    def build(self):
        self.title = "Dynamic Widgets"
        self.root = Builder.load_file('dynamic_labels.kv')
        return self.root

    def create_widgets(self):
        for name in self.name_people:
            temp_label=Label(text=name, id=name)
            self.root.ids.output_label.add_widget(temp_label)

    def clear_all(self):
        self.root.ids.output_label.clear_widgets()

DynamicLabelApp().run()