import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image

import unrar
import rarfile
import sys
import shutil
import os

cbr = rarfile.RarFile(sys.argv[1])
for f in cbr.infolist():
  print (f.filename, f.file_size)
  if f.filename == 'README':
    print(rf.read(f))

for fn in cbr.namelist():
  print(fn)

comic = (cbr.infolist()[5]).filename
print(type(comic))

#cbr.extractall(path='./temp/comic', members=cbr.infolist())
pages = os.listdir('./temp/comic')

class Gui(App):

  def build(self):
    #return Label(text='PanelHawk')
    #print(pages[0])
    return Image(source = './temp/comic/' + pages[0])
    #return Image(source='./temp/comic/Unnatural001.jpg')

if __name__ == '__main__':
  Gui().run()
  #shutil.rmtree('./temp/comic')
