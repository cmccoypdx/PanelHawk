import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

import rarfile
import sys

cbr = rarfile.RarFile(sys.argv[1])
#for f in cbr.infolist():
#  print (f.filename, f.file_size)
#  if f.filename == 'README':
#    print(rf.read(f))

#for fn in cbr.namelist():
#  print(fn)

comic = cbr.open(cbr.infolist()[0])
print(type(comic))
class Gui(App):

  def build(self):
    return Label(text='PanelHawk')
    #return Image(comic[0])

if __name__ == '__main__':
  Gui().run()

