 
def pad(text, target):
    output = text
    while len(output) < target:
        output += text
    if len(output) > target:
        return output[:target]
    return output
def encrypt(text, key):
    cipher = ""
    text = text.lower()
    key = pad(key.lower(), len(text))
    pairs = list(zip(text, key))
    #print(pairs)
    for a, b in pairs:
        a, b = ord(a)-96, ord(b)-96
        char = a + b
        while char > 26:
            char -= 26
        #print(a, b, char)
        cipher += chr(char + 96)
    return cipher
def decrypt(cipher, key):
    text = ""
    cipher = cipher.lower()
    key = pad(key.lower(), len(cipher))
    pairs = list(zip(cipher, key))
    #print(key, pairs)
    for a, b in pairs:
        a, b = ord(a)-96, ord(b)-96
        char = a - b
        while char < 1:
            char += 26
        #print(a, b, char)
        text += chr(char + 96)
    return text
while True:
    text = input("Tekst: ")
    key = input("Klucz: ")
    print("Zaszyfrowane:  " + encrypt(text, key))
    print("Zdeszyfrowane: " + decrypt(text, key))  
