# Typing logic into latex by hand is annoying.
# Lets convert normal English into the latex commands.

import pyperclip

def main ():
    terms = {'and': '\land', 'or': '\lor', 'not': '\\neg', 'implies': '\implies','if':'','then':'\supset'}

    input_string = input('please type sentence: ')
    if input_string != ('quit'):
        print("The original string is : " + str(input_string))
        conversion = " ".join(terms.get(word, word) for word in input_string.split())
        print("LaTeX: " + str(conversion)) #I did have $$ each side for math mode but maybe not for now.
        pyperclip.copy(str(conversion))

    else:
        print('exiting')
        exit()
while True:
    main()
