f = open('english_random.txt', 'r')
s = f.read()
f.close()

def generateKey(string, key):
    key = list(key)
    if len(string) == len(key):
        return(key)
    else:
        for i in range(len(string) -
                       len(key)):
            key.append(key[i % len(key)])
    return("".join(key))
def cipherText(string, key):
    cipher_text = []
    for i in range(len(string)):
        x = (ord(string[i]) +
             ord(key[i])) % 26
        x += ord('A')
        cipher_text.append(chr(x))
    return("" . join(cipher_text))
    
key = generateKey(s,'LEMON')
cipher_text = cipherText(s,key)
print("Ciphertext :", cipher_text)