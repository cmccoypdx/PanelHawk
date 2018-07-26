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

# Debug code that prints cbr contents
#for f in cbr.infolist():
#  print (f.filename, f.file_size)
#  if f.filename == 'README':
#    print(rf.read(f))

#for fn in cbr.namelist():
#  print(fn)

# Extract all pages in cbr to temp folder 'comic'
cbr.extractall(path='./temp/comic', members=cbr.infolist())

# Build list of page filenames
pages = os.listdir('./temp/comic')

class Gui(App):

  def build(self):
    return Image(source = './temp/comic/' + pages[0])

if __name__ == '__main__':

  # Start GUI
  Gui().run()

  # Empty temp folder on app exit
  shutil.rmtree('./temp/comic')
