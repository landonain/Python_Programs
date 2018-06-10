#! python3
'''
        mcb.pyw - Saves and loads pieces of text to the clipboard.
        Usage: py.exe mcb.pyw save <keyword> - Saves clipboard to keyword.
        py.exe mcb.pyw <keyword> - Loads keyword to clipboard.
        py.exe mcb.pyw list - Loads all keywords to clipboard.
        Saves the copy text to a shelf for storage
        There is a file in system32 that is a batch file so I can run this from
        the run window (win + r).
'''


import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
	mcbShelf[sys.argv[2]] = pyperclip.paste()
elif len(sys.argv) == 2:
	# List keywords and load content.
	if sys.argv[1].lower() == 'list':
		pyperclip.copy(str(list(mcbShelf.keys())))
	elif sys.argv[1] in mcbShelf:
		pyperclip.copy(mcbShelf[sys.argv[1]])
		text = pyperclip.paste()
		lines = text.split(r"\n")
		for i in range(len(lines)):
			lines[i] = '* ' + lines[i]
		text = '\n'.join(lines)
		pyperclip.copy(text)
mcbShelf.close()
