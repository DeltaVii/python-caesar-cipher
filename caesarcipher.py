######
##Kelly Norris
##
##11/8/16
##
##Caesar Cipher
######

#Variables needed for functions
type = None
messageCharList = []
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

##Functions##
#getting encrypt or decrypt
def userInput():
    print('Would you like to decrypt or encrypt?',"Type 'encrypt' or 'decrypt'")
    userType = input()

    if userType == 'decrypt':
        decrypt()
    if userType == 'encrypt':
        encrypt()
    else:
        print('Input not understood, try again')
        userInput()

def encrypt():
    print('Enter the message you want encrypted.')
    message = str(input())
    encrypt_message = []
    for i in message:
        messageCharList.append(i)
    print(messageCharList)
    print('Enter the letter shift number, -27 through 27')
    shift = input()
    shift = int(shift)
    if shift < -27 or shift > 27:
        print('Input not understood, try again')
        encrypt()
    else:
        print('shift # is',shift)
        for i in messageCharList:
            print(i)
            if i == ' ':
                encrypt_message.append(' ')
            else:
                position = alphabet.index(i)
                position += shift
                if position > 26:
                    position = 0 + (26-position)
                encryptedChar = alphabet[position]
                encrypt_message.append(encryptedChar)
    print(encrypt_message)

def decrypt():
    print('Enter the message you want decrypted.')
    message = str(input())
    decrypt_message = []
    for i in message:
        messageCharList.append(i)
    print(messageCharList)
    print('Enter the letter shift number, -27 through 27')
    shift = input()
    #if type(shift) != int:
    #    print('Input not understood, try again')
    #    decrypt()
    shift = int(shift)
    if shift < -27 or shift > 27:
        print('Input not understood, try again')
        decrypt()
    else:
        print('shift # is', shift)
        for i in messageCharList:
            print(i)
            if i == ' ':
                decrypt_message.append(' ')
            else:
                position = alphabet.index[i]
                position -= shift
                if position > 27:
                    position = 0 + (27-position)
                decryptedChar = alphhabet[position]
                encrypt_message.append(decryptedChar)
    print(decrypt_message)
    

userInput()
if type == 'encrypt':
    encrypt()
if type == 'decrypt':
    decrypt()

print('Do you want to do another? y/n')
input = input()
input = str(input)
if input == 'y':
    userInput()
