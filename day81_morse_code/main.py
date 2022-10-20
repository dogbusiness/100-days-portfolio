MORSE_CODE_DICT = { 'a': '•—', 'b': '—•••', 'c': '—•—•',
                    'd': '—••', 'e': '•', 'f': '••—•', 
                    'g': '——•', 'h': '••••', 'i': '••', 
                    'j': '•———', 'k': '—•—', 'l': '•—••', 
                    'm': '——', 'n': '—•', 'o': '———', 
                    'p': '•——•', 'q': '——•—', 'r': '•—•', 
                    's': '•••', 't': '—', 'u': '••—', 
                    'v': '•••—', 'w': '•——', 'x': '—••—', 
                    'y': '—•——', 'z': '——••',
                    '1':'.----', '2':'..---', '3':'...--',
                    '4':'....-', '5':'.....', '6':'-....',
                    '7':'--...', '8':'---..', '9':'----.',
                    '0':'-----', ', ':'--..--', '.':'.-.-.-',
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-', ' ': ' '}

print('Welcome to Morze Code Translator / Добро пожаловать в переводчик Азбуки Морзе.\n')
print('Please type latin symbols to translate / Для перевода, пожалуйста, введите латинские символы.\n')
print('For exit type --exit-- / Для выхода напечатайте --exit--\n')

str_input = ''
str_output = ''

while str_input != '--exit--':
    str_input = input()
    if str_input == '--exit--':
        continue
    else:
        try:
            for symbol in str_input:
                last_idx = len(str_input) - 1
                if str_input.index(symbol) != last_idx and symbol != ' ':
                    str_output += f'{MORSE_CODE_DICT[symbol]} '
                else:
                    str_output += MORSE_CODE_DICT[symbol]
            print(str_output)        
        except KeyError:
            print('Unable to translate. / Невозможно перевести.')
        str_output = ''    