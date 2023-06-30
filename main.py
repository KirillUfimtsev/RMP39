from kivy.config import Config
Config.set('graphics', 'width', '360')
Config.set('graphics', 'height', '800')
Config.set('graphics', 'resizable', 'false')
import kivymd
from kivymd.uix.floatlayout import FloatLayout
from kivymd.app import MDApp
from kivymd.uix.pickers import MDTimePicker

class Time(FloatLayout):
    def open_time_picker(self):
        time_dialog = MDTimePicker()
        time_dialog.bind(on_save =self.on_save, on_cancel=self.on_cancel)
        time_dialog.open()
    
    def on_save(self, instance , value):
        self.ids.select_time.text = str(value)
    
    def on_cancel(self, instance, value):
        self.ids.select_time.text = "Отменено"
    
class MainApp(MDApp):
    def build(self):
        return Time()

if __name__=="__main__":
    MainApp().run()