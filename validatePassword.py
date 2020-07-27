# In this program, we will be taking a password as a combination of alphanumeric characters
# along with special characters, and check whether the password is valid or not with the help of few conditions.
#
# Primary conditions for password validation :
#
# Minimum 8 characters.
# The alphabets must be between [a-z]
# At least one alphabet should be of Upper Case [A-Z]
# At least 1 number or digit between [0-9].
# At least 1 character from [ _ or @ or $ ].

import re

def validatePassword(str):

    flag = True
    while True:
        if len(str) < 8:
            flag = False
            break
        elif not re.search("[a-z]", str):
            # if not any(char.islower() for char in passwd):
            flag = False
            break
        elif not re.search("[A-Z]", str):
        # if not any(char.isupper() for char in passwd):
            flag = False
            break
        elif not re.search("[0-9]", str):
        # if not any(char.isdigit() for char in passwd):
            flag = False
            break
        elif not re.search("[_@$]", str):
        # SpecialSym =['$', '@', '#', '%'] 
        # if not any(char in SpecialSym for char in passwd):
            flag = False
            break
        elif re.search("\s", str):
            flag = False
            break
        else:
            break

    return flag

str = "R@m@_f0rtu9e$"
str = "Rama_fortune$"
retFlag = validatePassword(str)
print(retFlag)