import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.label import Label

class Gui(App):

  def build(self):
    return Label(text='PanelHawk')

if __name__ == '__main__':
  Gui().run()

