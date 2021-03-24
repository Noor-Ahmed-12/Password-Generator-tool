                    #################################################################################################################
                    #                   *************************Password Generator tool*****************************               #
                    #                                           Developer: @Noor-Ahmed-12(github)                                   #
                    #                               generator strong and secure password for your accounts                          #
                    #                                               Be secure and safe!                                             #
                    #################################################################################################################

import string
import random

def generatePasswd():
    s1=string.ascii_lowercase
    s2=string.ascii_uppercase
    s3=string.punctuation
    s4=string.digits
    
    passwd=[]
    passwd.extend(list(s1))
    passwd.extend(list(s2))
    passwd.extend(list(s3))
    passwd.extend(list(s4))

    random.shuffle(passwd)
    print("Your Strong password: ")
    print("".join(passwd[0:passLen]))

if __name__ == '__main__':
    while True:
        try:
            passLen = int(input("Enter Password Length:\n"))
            break
        except:
            print("Please Enter the number only!")
    if passLen <8:
        print("Password must be at least 8 characters!")
    else:
        generatePasswd()