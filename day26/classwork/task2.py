full_name = "saba gogoladze"
result = ""

for name in full_name: 
    print(full_name)
    if name == "s":
        result += "S" 
    elif name == "a": 
        result += "A"
    elif name == "b":
        result += "B"
    else :
        result += " " 

print(result)