import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget

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
path = './temp/comic/'
# Handle case where CBR has top level dir
if len(os.listdir(path)) == 1:
  path += os.listdir(path)[0]
  path += '/'
pages = os.listdir(path)
print(pages)

class Comic(Widget):
  pageIndex = 0
  #page = Image(source= './temp/comic/' + pages[pageIndex])

  def __init__(self, **kwargs):
    super(Comic, self).__init__(**kwargs)
    with self.canvas:
      self.bg = Image(source = path + pages[self.pageIndex], pos=self.pos, size=self.size)

  def update(self):
    page = Image(source= './temp/comic/' + pages[self.pageIndex])

  def page_turn(self, touch):
    if touch.x < self.width / 3:
      if self.pageIndex > 0:
        self.pageIndex -= 1
    if touch.x > self.width - self.width / 3:
      if self.pageIndex < len(pages) - 1:
        self.pageIndex += 1
    update()

  def build(self):
    return page

class Gui(App):

  def build(self):
    return Comic()

if __name__ == '__main__':

  # Start GUI
  Gui().run()

  # Empty temp folder on app exit
  shutil.rmtree('./temp/comic')
