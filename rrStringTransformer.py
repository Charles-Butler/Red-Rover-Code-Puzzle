

STRING= "id, name, email, type(id, name, customFields(c1, c2, c3)), externalId"
STRING_INPUT=[]

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

def split_then_sort(usr_str):
    items = []
    current_item = ""
    n_level = 0

    for char in usr_str:
        if char == '(':
                n_level += 1
                current_item += char
        elif char == ')':

                n_level -= 1
                current_item += char

        elif char == ',' and n_level == 0:
                items.append((current_item.strip()))

                current_item = ''
        else:
                current_item += char

    if current_item.strip():
        items.append(current_item.strip())
        
    items.sort()

    return ", ".join(items)

print(f"split & Sort: {split_then_sort(STRING)}")

originalString=STRING
print("Transformed String:")

for nestedLevel, data in transform_string(originalString):
    indent = "  " * nestedLevel
    print(f"{indent}- {data}")
    