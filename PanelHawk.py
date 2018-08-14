# PanelHawk Comic Book Reader
# Copyright 2018 Colin McCoy 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the 
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import kivy
kivy.require('1.11.0')

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.graphics import InstructionGroup
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout

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

# Best option for mobile
#Window.fullscreen = 'auto'

# Best option for desktop
Window.maximize()

class Comic(GridLayout):
  pageIndex = 0

  # Logic for binding page size to window taken from https://stackoverflow.com/questions/30207707/how-to-fill-canvas-with-an-image-in-kivy
  def __init__(self):
    super(Comic, self).__init__(cols=1)
    with self.canvas:
      self.page = Image(source = path + pages[self.pageIndex], pos=self.pos, size=self.size)

    
  # Bind page image size relative to size of app window
    self.bind(pos=self.update_bg)
    self.bind(size=self.update_bg)

  # Resize page image when app window is resized
  def update_bg(self, *args):
    self.page.pos = self.pos
    self.page.size = self.size

  # Clear canvas of current page and load page at pageIndex
  def update(self):
    self.canvas.clear()
    with self.canvas:
      self.page = Image(source = path + pages[self.pageIndex], pos=self.pos, size=self.size)

  # Move to next or previous page based on which third of the screen
  # was touched/clicked. Right third goes to next page, left third
  # goes to previous page. Middle third or already at furthest navigation
  # point does nothing.
  def on_touch_down(self, touch):
    if touch.x < self.width / 3:
      if self.pageIndex > 0:
        self.pageIndex -= 1
    if touch.x > self.width - self.width / 3:
      if self.pageIndex < len(pages) - 1:
        self.pageIndex += 1
    self.update()

class PanelHawk(App):

  def build(self):
    root = Comic()
    return root

if __name__ == '__main__':

  # Start GUI
  PanelHawk().run()

  # Empty temp folder on app exit
  shutil.rmtree('./temp/comic')
