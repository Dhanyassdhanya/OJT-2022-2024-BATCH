# Keyword Arguments
# Example
def callme(str_value):
    print(str_value)

callme(str_value="Calling that function")

# Explanation
def empinfo(name, designation):
    print("Name:", name)
    print("Designation:", designation)

empinfo(name="ABC", designation="Dev")
# Variable Length Arguments

def callme(arg, *vartuple):
    print("India??")
    print(arg)
    for var in vartuple:
        print(var)

callme("Democracy", "or", "Gerontocracy")
