# Typing logic into latex by hand is annoying.
# Lets convert normal English into the latex commands.

import pyperclip
from tkinter import *

# tkinter setup and window config
root = Tk()
root.title("English2LatexLogic")
root.geometry("300x100")
root.resizable(width=False, height=False)
root.attributes('-topmost', True) # keep the window on top for when I'm writing logic from a text.
root.update()
input = Entry(root, width=40)
input.pack()
output = Text(height=3, width=30)
output.pack()

def submit_a(self):
    terms = {'and':'\land', 'or':'\lor', 'not':'\\neg', 'implies':'\implies', 'if':'', 'then': '\supset'}
    inputSubmit = input.get()
    if inputSubmit != ('quit'):
        conversion = " ".join(terms.get(word, word) for word in inputSubmit.split())
        print(conversion)
        output.insert(END, conversion + '\n')
        pyperclip.copy(str(conversion))
        input.delete(0, 'end')
    else:
        print('exiting')
        exit()
input.bind("<Return>", submit_a)
root.mainloop()