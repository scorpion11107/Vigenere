import string

def generateTable():
    table = {}
    for i in range(26):
        table[string.ascii_lowercase[i]] = string.ascii_lowercase[i:] + string.ascii_lowercase[:i]
    return table

def code(text, key, table):
    generatedKey = ""
    while len(generatedKey) < len(text):
        generatedKey += key
    
    result = ""
    for i in range(len(text)):
        result += table[generatedKey[i]][string.ascii_lowercase.index(text[i])]
    
    return result
    
def decode(text, key, table):
    generatedKey = ""
    while len(generatedKey) < len(text):
        generatedKey += key
    
    result = ""
    for i in range(len(text)):
        result += string.ascii_lowercase[table[generatedKey[i]].index(text[i])]
    
    return result