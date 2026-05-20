

STRING="id, name, email, type(id, name, customFields(c1, c2, c3)), externalId"
print("Given" + STRING)

def transform_string(s):
    nestedLevel = 0
    result = []
    currentProp = ""

# Bash Equivalent
# printf "$STRING" | tr ',' '\n' | tr ')' ' ' | tr '(' '\n\t' | sed 's/^ *//' | sed 's/^/- /'


    return result

originalString=STRING
print("Transformed String:")

for nestedLevel, data in transform_string(originalString):
    indent = " " * nestedLevel
    print(f"- {indent}{data}")