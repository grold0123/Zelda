import webbrowser,sys,pyperclip,pathlib

base_dir = pathlib.Path.cwd()
bookmark = base_dir/'bookmark.txt'

try:
    arg = sys.argv[1].lower().strip()
    if arg :
        match arg:
            case 'open': 
                webbrowser.open(bookmark.read_text())
            case 'save': 
                bookmark.write_text(pyperclip.paste())
except ValueError: print('Could not run script')