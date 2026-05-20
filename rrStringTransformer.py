

STRING= "id, name, email, type(id, name, customFields(c1, c2, c3)), externalId"
print("Given " + STRING)

def transform_string(s):
    nestedLevel = 0
    result = []
    currentProp = ""

# Bash Equivalent
# 1. | tr ',' '\n' -> take care of commas
# 2a. | tr ')' ' '  
# 2b. | tr '(' '\n\t' -> take care of ()
# 3a. | sed 's/^ *//'  
# 3b. | sed 's/^/- /' -> indention / dash and space

    for char in s:
        if char == ',':
            if currentProp.strip():
                result.append((nestedLevel, currentProp.strip()))
                currentProp = ''
        elif char == '(':
                result.append((nestedLevel, currentProp.strip()))
                currentProp = ''
        elif char == ')':                
                result.append((nestedLevel, currentProp.strip()))
                currentProp = ''
        else:
                currentProp += char

    if currentProp.strip():
        result.append((nestedLevel, currentProp.strip()))

    return result

originalString=STRING
print("Transformed String:")

for nestedLevel, data in transform_string(originalString):
    indent = " " * nestedLevel
    print(f"- {indent}{data}")