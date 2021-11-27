import random as r

#32 Characters
#DF32AW43-3214-UI31-341D-POI83C19N1Z5
#8 - 4 - 4 - 4 - 12

characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
charactersPlus = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "X", "x", "Y", "y", "Z", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "@", "#", "$", "%", "^", "&", "*", "!"]

def generateGUID():
    new_GUID = []
    i = 0
    while i < 32:
        index = r.randrange(len(characters))
        index = characters[index]
        new_GUID.append(index)
        i += 1
    new_GUID.insert(8, "-")
    new_GUID.insert(13, "-")
    new_GUID.insert(18, "-")
    new_GUID.insert(23, "-")
    new_GUID = ''.join(new_GUID).lower()
    return new_GUID

def generatePW():
    new_password = []
    i = 0
    while i <= 25:
        index = r.randrange(len(charactersPlus))
        index = charactersPlus[index]
        new_password.append(index)
        i += 1

    new_password = "".join(new_password)
    return new_password
