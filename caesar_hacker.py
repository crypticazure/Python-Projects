"""This program can hack messages encrypted with caesar_cipher.py, even if you do not know the key. There are only 26 possible keys for the Caesar cipher, so this program is an example of a brute-force attack.
The one drawback of this program is that it cannot tell when it has used the correct key, and requires a human to read the output to determine which key is correct."""

#Let the user specify the messag to hack
print("Enther the encrypted Caesar cipher message to hack.")
message = input('> ')

#Every possible symbol that can be encrypted/decrpyted
#This must match the symbols list used when encrypting the message
symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for key in range(len(symbols)): #loop through every possible key
    translated = ''

    #Decrypt each symbol in the message:
    for symbol in message:
        if symbol in symbols:
            num = symbols.find(symbol) #get the number of the symbol
            num = num - key #Decrypt the number

            #Handle the wrap-around if num is less than 0:
            if num < 0:
                num = num + len(symbols)
            
            #Add decrypted number's symbol to translated:
            translated = translated + symbols[num]
        else:
            #Just add the symbol without decrypting:
            translated = translated + symbol
    #Display the key being tested, along with its decrypted text:
    print("Key #{}: {}".format(key, translated))