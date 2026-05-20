

STRING= "id, name, email, type(id, name, customFields(c1, c2, c3)), externalId"
STRING_INPUT=[]

print(f"Given '({STRING})'")

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
    
    for i in range(len(items)):
        item = items[i]
        if '(' in item:
            item_name = item[:item.index('(')]
            nested_items = item[item.index('(')+1:item.rindex(')')]

        #recursively sort inner/nested stuff
            sorted_nested_item=split_then_sort(nested_items)
            items[i] = f"{item_name}({sorted_nested_item})"

    #Sort & Return lines
    items.sort()
    return ", ".join(items)

second_str=split_then_sort(STRING)
# print(f"split & Sort: {split_then_sort(STRING)}")

originalString=STRING
print(f"\nTransformed String:")

for nestedLevel, data in transform_string(originalString):
    indent = "  " * nestedLevel
    print(f"{indent}- {data}")
    
print(f"\nSorted Output:")
#Second Output
for nestedLevel, data in transform_string(second_str):
    indent = "  " * nestedLevel
    print(f"{indent}- {data}")