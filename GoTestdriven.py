import sublime, sublime_plugin, os.path

class GoTestdrivenCommand(sublime_plugin.WindowCommand):
  def openTwoColumns(self):
    self.window.set_layout({
        "cols": [0, 0.5, 1],
        "rows": [0, 1],
        "cells": [[0, 0, 1, 1], [1, 0, 2, 1]]
    })

  def run(self):
    filePath = self.window.active_view().file_name()
    fileName = os.path.basename(filePath)
    currentDirectory = os.path.dirname(filePath)

    self.openTwoColumns()

    if '.spec' in fileName:
      fileToOpen = fileName.replace('.spec', '')
      # In case code file is already open, move it to right group.
      codeFileView = self.window.find_open_file(fileToOpen);
      if codeFileView:
        self.window.set_view_index(codeFileView, 1, 0)

      self.window.focus_group(1)
    else:
      # Move code file to rightmost group.
      self.window.focus_group(0)
      self.window.set_view_index(self.window.active_view(), 1, 0)
      self.window.focus_group(0)
      # Open .spec file.
      fileToOpen = fileName.replace('.js', '.spec.js')

    fullPath = os.path.join(currentDirectory, fileToOpen)
    normalizedPath = os.path.normpath(fullPath)
    self.window.open_file(normalizedPath)
