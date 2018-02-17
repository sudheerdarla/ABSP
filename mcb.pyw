#! python3
# mcb.pyw - Saves and loads pieces of text to the clipboard.
# Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
# 		 py.exe mcb.pyw <keyboard> - Loads to clipboard.
# 	  	 py.exe mcb.pyw list - Loads all keywords clipboard.

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# Save clipboard content.
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()

elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])

	# to delete all the keywords with 'delete' command line arg.
	elif sys.argv[1].lower() == 'delete':
		print(mcbShelf)
		for i in list(mcbShelf.keys()):
			del mcbShelf[i]

# to delete a keyword with 'delete <keyword>' command line arg..
elif len(sys.argv) == 3 and sys.argv[1].lower() == 'delete':
	del mcbShelf[sys.argv[2]]

mcbShelf.close()

# for testing....
# Q:1. What is a relative path relative to?

# Q:2. What does an absolute path start with?

# Q:3. What do the os.getcwd() and os.chdir() functions do?














