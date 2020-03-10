def cal(*num,mode):
    total=0
    if mode=="+":
        for i in num:
            total+=i
    if mode=="-":
        for i in num:
            total-=i
    return total

print(cal(1,2,3,4,5,mode="+"))
print(cal(1,2,3,4,5,mode="-"))

def insert_data(**data):
    print(data)
insert_data(name="ooya",blood="A",age="15")

bigger=lambda num1,num2: num1 if num1>num2 else num2
print(bigger(9,6))
print(bigger(3,6))
getPrice=lambda price,tax=1.1: int(price*tax)
print(getPrice(1000))
print(getPrice(1000,1.08))