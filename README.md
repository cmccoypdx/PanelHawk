# PanelHawk: Detect individual comic panels for reading and capturing
Copyright (c) 2018 Colin McCoy

This program reads compressed comic book files in the popular .cbr and .cbz (not yet implemented, medium priority) formats. In 
addition to the usual page-by-page reading style, PanelHawk will detect panels within the pages, and allow the user to zoom in 
on these panels or capture individual screenshots of them (Not yet implemented, high priority). 

PanelHawk uses the Kivy framework for its GUI, which should allow it to be easily ported to mobile device operating systems. 
Porting it to Android is a medium-high level priority, iOS may follow. Kivy is licensed under the MIT license, and can be found 
at https://kivy.org. 

PanelHawk currently only opens the most popular digital comic book format, .cbr, and does so using the python module rarfile, 
which is licensed under the ISC license, and can be found at https://github.com/markokr/rarfile. 

Neither kivy nor rarfile are distributed with PanelHawk, but both can be found at the above URLs, or installed with your
package manager of choice.

### Requirements:
kivy version 1.11 or higher,
rarfile version 3.0 or higher,
python version 3.5 or higher

### Build and run:
I have not yet attempted to build PanelHawk into a binary executable. The first binary release will likely be targeted 
at Android, and I plan to make that available here when it is ready. For now, PanelHawck can be run in the python interpreter 
(version 3.5 or higher). Be sure to install kivy and rarfile into your python environment (I recommend using an
environment manager). NOTE: the kivy documentation officially states that kivy is not yet compatible with python versions
above 3.5, however, I have gotten PanelHawk to run successfully on python 3.6.5, using the most recent dev version of kivy
(version 1.11). You may attempt to use PanelHawk with a non-dev kivy installation, but be aware that it may not work
with python versions above 3.5, and remember to change the kivy require statement to match the version that you are using
(I recommend at least version 1.8).

The current version of PanelHawk has no menu, and so the path to the .cbr file that you wish to read must be passed as 
an argument when running the program, e.g. 'python3 PanelHawk.py /path/to/comic.cbr'

### License
This program is licensed under the GNU General Public License. Please see the file COPYING in this distribution for the
details of this license.
