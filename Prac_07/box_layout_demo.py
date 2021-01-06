from kivy.app import App
from kivy.lang import Builder

class BoxLayoutDemo(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def clear_button(self):
        """Clear all of the text field and the output label """
        self.root.ids.output_label.text=''
        self.root.ids.input_name.text = ''








BoxLayoutDemo().run()