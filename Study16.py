list=["A","B"]
def add_C(list_items):
    list_items.append("C")
add_C(list)
print(list)

x=0
def setCount(y):
    x=y
def setCount2(y):
    global x
    x=y
y=10
setCount(y)
print(x)
y=12
setCount2(y)
print(x)