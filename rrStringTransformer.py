

STRING= "id, name, email, type(id, name, customFields(c1, c2, c3)), externalId"
print("Given " + STRING)

def transform_string(s):
    nestedLevel = 0
    result = []
    currentProp = ""


    for char in s:
        if char == ',':
            if currentProp.strip():
                result.append((nestedLevel, currentProp.strip()))
                currentProp = ''
        elif char == '(':
            if currentProp.strip():
                result.append((nestedLevel, currentProp.strip()))
                nestedLevel += 1
                currentProp = ''
        elif char == ')':
            if currentProp.strip():
                result.append((nestedLevel, currentProp.strip()))
                nestedLevel -= 1
                currentProp = ''
        else:
                currentProp += char

    if currentProp.strip():
        result.append((nestedLevel, currentProp.strip()))

    return result

originalString=STRING
print("Transformed String:")

for nestedLevel, data in transform_string(originalString):
    indent = "  " * nestedLevel
    print(f"{indent}- {data}")