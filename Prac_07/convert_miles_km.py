from kivy.app import App
from kivy.lang import Builder

miles_to_km= 1.60934

class MilesConverterApp(App):

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        value = self.handle_invalid_inputs()
        result = value * miles_to_km
        self.root.ids.output_label.text = str(result)

    def handle_increment(self,change):
        value = self.handle_invalid_inputs()+change
        self.root.ids.input_miles.text=str(value)
        self.handle_calculate()

    def handle_invalid_inputs(self):
        try:
            value = float(self.root.ids.input_miles.text)
            return (value)
        except ValueError:
            return 0


MilesConverterApp().run()