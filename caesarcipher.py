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
        type = 'decrypt'
    if userType == 'encrypt':
        encrypt()
    else:
        print('Input not understood, try again')
        userInput()

def encrypt():
    print('Enter the message you want decrypted.')
    message = str(input())
    for i in message:
        messageCharList.append(i)
    print(messageCharList)
    print('Enter the letter shift number, -27 through 27')
    shift = int(input())
    

userInput()
if type == 'encrypt':
    encrypt()
