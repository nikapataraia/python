def encryptIndexSubstitutionCipher(txt):
    tempo = str(txt)
    result = ""
    for element in tempo:
        code = ord(element) - 96
        el = str(code)
        if(code < 10): el = str("0" + el)
        result = result + el + " "
    return result[:-1]
    


def decryptIndexSubstitutionCipher(code):
    tempo = str(code)
    result = ""
    a = 0
    tempocode = 0
    while(tempo):
        if(tempo[0:1] == "0"):  tempcode = int(tempo[1:2]) + 96
        else: tempcode = int(tempo[0:2]) + 96
        character = chr(tempcode)
        result = result + character
        tempo = tempo[3:]
    return result


mydict =  {
 'a': '._',
 'b': '_...',
 'c': '_._.',
 'd': '_..',
 'e': '.',
 'f': '.._.',
 'g': '__.',
 'h': '....',
 'i': '..',
 'j': '.___',
 'k': '_._',
 'l': '._..',
 'm': '__',
 'n': '_.',
 'o': '___',
 'p': '.__.',
 'q': '__._',
 'r': '._.',
 's': '...',
 't': '_',
 'u': '.._',
 'v': '..._',
 'w': '.__',
 'x': '_.._',
 'y': '_.__',
 'z': '__..'
 }

def  encryptMorseCode(text):
    temp = str(text)
    result = ""
    for element in temp:
        code = mydict[element]
        result = result + code + " "
    result = result[0:len(result)]
    return result

def get_key(val):
    for key, value in mydict.items():
         if val == value:
             return key
 
    return "key doesn't exist so instead of morse there will be this string :))) surrounded by morse :))"


def decryptMorseCode(morsecode):
    temp = str(morsecode)
    result = ""
    while(temp):
        index = 0
        for el in temp:
            index = index +1
            if(el == " "):
                index = index - 1
                break
        value = temp[0:index]
        key = get_key(value)
        result = result + key
        temp = temp[index + 1:]
    return result


print(encryptMorseCode("aabb"))

               


def encriptionalgorithm(a,b,x):
    return (a*x + b) % 26

def decriptionalgorithm(a,b,x):
    return  (pow(a,-1,26) * (x - b)) % 26

def encryptAffineCipher(text,A,B):
    result = ""
    temp = str(text)
    for ele in temp:
        preindex = ord(ele) - 97
        postindex = encriptionalgorithm(A,B,preindex) + 97
        result = result + chr(postindex)

    return result

def decryptAffineCipher(script,A,B):
    result = ""
    temp = str(script)
    for ele in temp:
        preindex = ord(ele) - 97
        postindex = int(decriptionalgorithm(A,B,preindex) + 97)
        result = result + chr(postindex)

    return result 




# a-z 97-122
# A-Z 65-90
#0-9 48-57
def shiftletterbykey(let,key):
    x = str(let)
    preindex = ord(let)
    if(x.isalpha()):
        if(x.islower()):
            postindex = (preindex - 97 + key)%26 + 97
            return chr(postindex)
        if(x.isupper()):
            postindex = (preindex - 65 + key)%26 + 65
            return chr(postindex)
    if(x.isnumeric()):
        postindex = (preindex - 48 + key)%10 + 48
        return chr(postindex)
    return x

def deshiftletterbykey(let,key):
    x = str(let)
    preindex = ord(let)
    if(x.isalpha()):
        if(x.islower()):
            postindex = (preindex - 97 - key)%26 + 97
            return chr(postindex)
        if(x.isupper()):
            postindex = (preindex - 65 - key)%26 + 65
            return chr(postindex)
    if(x.isnumeric()):
        postindex = (preindex - 48 - key)%10 + 48
        return chr(postindex)
    return x




def encryptCaesarCipher(text,key1,key2):
    x = 0
    result = ""
    for element in text:
        x = x+1
        if(x%2==1):
            result = result + shiftletterbykey(element,key1)
        else:
            result = result + shiftletterbykey(element,key2)
    return result

def decryptCaesarCipher(text,key1,key2):
    x = 0
    result = ""
    for element in text:
        x = x+1
        if(x%2==1):
            result = result + deshiftletterbykey(element,key1)
        else:
            result = result + deshiftletterbykey(element,key2)
    return result


def encryptTranspositionCipher(text,key):
    columnum = len(text)/key
    if(columnum > int(columnum)):
        columnum = int(columnum) +1
    columnum = int(columnum)
    columnlist = []
    result = ""
    for x in range(columnum):
        if(x == columnum): columnlist.append(text[x * key :])
        else: columnlist.append(text[x  *key : (x+1)*key])
    for x in range(key):
        for el in columnlist:
            if(len(el)>x):
             result = result + el[x]
    return result 



def  decryptTranspositionCipher(text,key):
    result = ""
    columnum = len(text)/key
    if(columnum > int(columnum)):
        columnum = int(columnum) +1
    columnum = int(columnum)
    columnlist = []
    laststringlen = len(text) - int(len(text)/key) * key
    for x in range(laststringlen):
        columnlist.append(text[(x) * columnum : (x+1) * columnum])


    if(laststringlen == 0):
     for y in range(key - laststringlen):
        columnlist.append(text[laststringlen * columnum + y * (columnum):laststringlen * columnum + (y+1) * (columnum)])
    else:
        for y in range(key - laststringlen):
         columnlist.append(text[laststringlen * columnum + y * (columnum-1):laststringlen * columnum + (y+1) * (columnum-1)])


    for x in range(columnum):
        for el in columnlist:
            if(len(el)>x):
             result = result + el[x]
        
         

    return result