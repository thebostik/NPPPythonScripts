# The lines up to and including sys.stderr should always come first
# Then any errors that occur later get reported to the console
# If you'd prefer to report errors to a file, you can do that instead here.
import sys
from Npp import *

# Set the stderr to the normal console as early as possible, in case of early errors
sys.stderr = console

# Define a class for writing to the console in red
class ConsoleError:
	def __init__(self):
		global console
		self._console = console;
		
	def write(self, text):
		self._console.writeError(text);
	
	def flush(self):
		pass
# Set the stderr to write errors in red
sys.stderr = ConsoleError()

# This imports the "normal" functions, including "help"
import site

# This sets the stdout to be the currently active document, so print "hello world", 
# will insert "hello world" at the current cursor position of the current document
sys.stdout = editor

wantedColumn = int(notepad.prompt("Enter the column to jump to (>0): ", "Jump to Column", "1"))

line = editor.getLine(0)
commaCount = 0
cursorPos = 0

for letter in line:
	if letter == ',':
		commaCount += 1
	if commaCount >= wantedColumn:
		break
	cursorPos += 1
	
notepad.setStatusBar(STATUSBARSECTION.DOCSIZE,"CSV Column: " + str(wantedColumn))
editor.setCurrentPos(cursorPos)