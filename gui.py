import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import InstructionGroup
from kivy.core.window import Window

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

# Debug code for printing just filenames in cbr
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
pages.sort()


class Comic(Widget):
  pageIndex = 0

  # Logic for binding page size to window taken from https://stackoverflow.com/questions/30207707/how-to-fill-canvas-with-an-image-in-kivy
  def __init__(self, **kwargs):
    super(Comic, self).__init__(**kwargs)
    with self.canvas:
      self.page = Image(source = path + pages[self.pageIndex], pos=self.pos, size=self.size)

    self.bind(pos=self.update_bg)
    self.bind(size=self.update_bg)

  def update_bg(self, *args):
    self.page.pos = self.pos
    self.page.size = self.size

  def update(self):
    self.canvas.clear()
    with self.canvas:
      self.page = Image(source = path + pages[self.pageIndex], pos=self.pos, size=self.size)

  def on_touch_down(self, touch):
    if touch.x < self.width / 3:
      if self.pageIndex > 0:
        self.pageIndex -= 1
    if touch.x > self.width - self.width / 3:
      if self.pageIndex < len(pages) - 1:
        self.pageIndex += 1
    self.update()


  def build(self):
    return page

class Gui(App):

  def build(self):
    root = Comic()
    return root

if __name__ == '__main__':

  # Start GUI
  Gui().run()

  # Empty temp folder on app exit
  shutil.rmtree('./temp/comic')
