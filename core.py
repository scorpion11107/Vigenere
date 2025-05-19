import string

def generate_table():
    table = {}
    for i in range(26):
        table[string.ascii_lowercase[i]] = string.ascii_lowercase[i:] + string.ascii_lowercase[:i]
    
    return table

def generate_key(key, length):
    generatedKey = ""
    while len(generatedKey) < length:
        for c in key:
            if c not in string.ascii_lowercase:
                continue
            generatedKey += c
    
    return generatedKey[:length]

def code(text, key, table):
    if not key:
        return "No key"
    elif not text:
        return "No input text"

    key = generate_key(key, len(text))
    
    result = ""
    key_index = 0

    for i in range(len(text)):
        if text[i] not in string.ascii_lowercase:
            result += text[i]
            continue
        result += table[key[key_index]][string.ascii_lowercase.index(text[i])]
        key_index += 1
    
    return result
    
def decode(text, key, table):
    if not key:
        return "No key"
    elif not text:
        return "No input text"
    
    key = generate_key(key, len(text))
    
    result = ""
    key_index = 0

    for i in range(len(text)):
        if text[i] not in string.ascii_lowercase:
            result += text[i]
            continue
        result += string.ascii_lowercase[table[key[key_index]].index(text[i])]
        key_index += 1
    
    return result

def code_command(keyTextArea, inputTextArea, resultTextArea):
    key = keyTextArea.get("1.0", "end")[:-1].lower()
    text = inputTextArea.get("1.0", "end")[:-1].lower()
    result = code(text, key, generate_table())
    
    resultTextArea.delete("1.0", "end")
    resultTextArea.insert("1.0", result)

def decode_command(keyTextArea, inputTextArea, resultTextArea):
    key = keyTextArea.get("1.0", "end")[:-1].lower()
    text = inputTextArea.get("1.0", "end")[:-1].lower()
    result = decode(text, key, generate_table())
    
    resultTextArea.delete("1.0", "end")
    resultTextArea.insert("1.0", result)