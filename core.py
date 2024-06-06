import string

def generateTable():
    table = {}
    for i in range(26):
        table[string.ascii_lowercase[i]] = string.ascii_lowercase[i:] + string.ascii_lowercase[:i]
    return table

def code(text, key, table):
    if not key:
        return "No key"
    elif not text:
        return "No input text"

    generatedKey = ""
    while len(generatedKey) < len(text):
        generatedKey += key
    
    result = ""
    for i in range(len(text)):
        result += table[generatedKey[i]][string.ascii_lowercase.index(text[i])]
    
    return result
    
def decode(text, key, table):
    if not key:
        return "No key"
    elif not text:
        return "No input text"
    
    generatedKey = ""
    while len(generatedKey) < len(text):
        generatedKey += key
    
    result = ""
    for i in range(len(text)):
        result += string.ascii_lowercase[table[generatedKey[i]].index(text[i])]
    
    return result

def codeCommand(keyTextArea, inputTextArea, resultTextArea):
    key = keyTextArea.get("1.0", "end")[:-1]
    text = inputTextArea.get("1.0", "end")[:-1]
    result = code(text, key, generateTable())
    
    resultTextArea.delete("1.0", "end")
    resultTextArea.insert("1.0", result)

def decodeCommand(keyTextArea, inputTextArea, resultTextArea):
    key = keyTextArea.get("1.0", "end")[:-1]
    text = inputTextArea.get("1.0", "end")[:-1]
    result = decode(text, key, generateTable())
    
    resultTextArea.delete("1.0", "end")
    resultTextArea.insert("1.0", result)