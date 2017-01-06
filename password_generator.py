'''
Write a password generator in Python. Be creative with how you generate passwords
 - strong passwords have a mix of lowercase letters, uppercase letters, numbers, 
 and symbols. The passwords should be random, generating a new password every 
 time the user asks for a new password. Include your run-time code in a main method.
'''
import random
import string

password_mask = []
password = []
#create 4 different lists or dictionaries as library to get content
def case0(): #Letter
    #print random.choice(string.letters)
    return random.choice(string.letters)
def case1(): #Symbols
    library = "!@#$%^&*()_<>?"
    #print random.choice(library)
    return random.choice(library)
def case2(): #Numerals
    #print  random.randint(0,9)
    return random.randint(0,9)

    
#password generator
def password_generator():
    global password_mask
    global password
    n = random.randint(8,16) #n created as the digit number of the password
    for i in range(n):
        password_mask.append(random.randint(0,2)) #each digit will call a random member from 3 different libraries
    for j in password_mask:
        if j == 0:
            password.append(case0())
        elif j == 1:
            password.append(case1())
        elif j == 2:
            password.append(case2())
        else:
            password.append("Sum Tim Wong")
    return "".join(str(v) for v in password)
    
print password_generator()
###DEBUGGING### print string.letters
###DEBUGGING### print password_mask
###DEBUGGING### print password


        
    