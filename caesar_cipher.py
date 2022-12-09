"""The Caesar cipher is a shift cipher that uses addition and subtraction to encrypt and decrypt letters.
More info on this at https://en.wikipedia.org/wiki/Caesar_cipher"""

try:
    import pyperclip #pyperclip copies text to the clipboard
except ImportError:
    pass #pyperclip not being installed is not a big deal

"""Every possible symbol that cn be encrypted/decrypted:
(!) You can ad numbers and punctuation marks to encrypt those
symbols as well"""

symbols = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#Let the user enter if they are encrypting or decrypting:
while True: #Keep asking until the user enters e or d
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    response = input('> ').lower()
    if response.startswith('e'):
        mode = 'encrypt'
        break
    elif response.startswith('d'):
        mode = 'decrypt'
        break
    print("Please enter the leter e or d")

#Let the user enter the key to use:
while True: #keep asking until the user enters a valid key
    maxKey = len(symbols) - 1
    print("Please enter the key (0 to {}) to use.".format(maxKey))
    response = input('> ').upper()
    if not response.isdecimal():
        continue
    if 0 <= int(response) < len(symbols):
        key = int(response)
        break

#Let the user enter the message to encrypt/decrypt:
print("Enter the message to {}.".format(mode))
message = input('> ')

#Caesar cipher only works on uppercase letters:
message = message.upper()

#Stores the encrypted/decrypted form of the message:
translated = ''

#Encrypt/decrypt each symbol in the message:
for symbol in message:
    if symbol in symbols:
        #Get the encrypted (or decrypted) number for this symbol
        num = symbols.find(symbol) #Get the number for the symbol
        if mode == 'encrypt':
            num = num + key
        elif mode == 'decrypt':
            num = num - key

        #Handle the wrap-around if num is larger than the length of symbols or less than 0
        if num >= len(symbols):
            num = num - len(symbols)
        elif num < 0:
            num = num + len(symbols)

        #Add encrypted/decrypted number's symbol to translated list
        translated = translated + symbol

#Display the encrypted/decrypted string to the screen:
print(translated)

try:
    pyperclip.copy(translated)
    print('Full {}ed text copied to clipboard.'.format(mode))
except:
    pass #Do nothing if pyperclip wasn't installed