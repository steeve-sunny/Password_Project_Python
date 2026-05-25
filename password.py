import string
import random

login = {}
passwords = []

# A function that generates a password, sequence of random letters + letters
def CreatePassword(username):
    char = string.ascii_letters + string.digits + string.punctuation
    result = "".join(random.choice(char) for i in range(16))
    if result not in passwords:
        passwords.append(result)
        login[username] = result
    else:
        CreatePassword(username) # deals with if the random password occurs again, thefore recurssive call and randomise amother password
    return result

# we have to construct the strength of a particular password of a username
def StrengthOfPassword(username):
    strength = 0
    strength_storage = []
    if username in login:
        password = login[username]

        for ch in password:
            if (ch in string.punctuation) and (string.punctuation not in strength_storage):
                strength += 1
                strength_storage.append(string.punctuation)
            
            elif (ch in string.digits) and (string.digits not in strength_storage):
                strength += 1
                strength_storage.append(string.digits)
            
            elif (ch in string.ascii_lowercase) and (string.ascii_lowercase not in strength_storage):
                strength += 1
                strength_storage.append(string.ascii_lowercase)
            
            elif (ch in string.ascii_uppercase) and (string.ascii_uppercase not in strength_storage):
                strength += 1
                strength_storage.append(string.ascii_uppercase)
        
        Strenght_scale = strength / 4 * 100
        
        #we calculating the strength of password based on the value of strenght_scale
        if strength == 4:
            return f"The Stregth of the Password is Very Secure, with a stregth scale of {Strenght_scale:.0f}%"
        elif strength == 3:
            return f"The Stregth of the Password is Secure, with a stregth scale of {Strenght_scale:.0f}%"
        elif strength == 2:
            return f"The Stregth of the Password is Not That Secure, with a stregth scale of {Strenght_scale:.0f}%"
        elif strength == 1:
            return f"The Stregth of the Password is Not Secure, with a stregth scale of {Strenght_scale:.0f}%"
        else:
            return f"This is invalid Password, change it Immediately !!!!"

    else:
        return f"This Username {username} doesn't exist, Please Sign Up if you like"



# The commented code are invokes which are tools to check the streght of a password or to create a password
# uncomment the code below to use them.

#(CreatePassword()) # need to enter a username in order to create a password for a username
#print(StrengthOfPassword()) # enter the username in order to get the strength of the password
