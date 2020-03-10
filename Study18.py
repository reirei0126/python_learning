#関数の応用
#map関数
def getTaxPrice(price,tax=1.08):
    return int(price*tax)
prices=[100,250,370,1000]
for price in map(getTaxPrice,prices):
    print(price)

onTaxPrinces=list(map(getTaxPrice,prices))
print(onTaxPrinces)

#map関数を使って関数を一つずつ回す

#無名関数
prices=[100,130,543]
onTaxPrinces=list(map(lambda price,tax=1.08:int(price*tax),prices))
print(onTaxPrinces)
prices=[100,130,543]
onTaxPrinces=[int(price*1.08)for price in prices]
print(onTaxPrinces)

#Filter def
def over1000(price):
    return price>=1000
prices=[100,1130,543,9000]
for price in filter(over1000,prices):
    print(price)
for price in map(over1000,prices):
    print(price)
for price in filter(lambda price : price>=1000,prices):
    print(price)
over1000Prices=[price for price in prices if price>=1000]
print(over1000Prices)

#辞書のsort
teams={"ZAKU":"Ateam","Bash":"Ateam","Ken":"Bteam","Take":"Ateam"}
print("名前の昇順")
for player in sorted(teams.items(),key=lambda k:k[0]):
    print(player[0],player[1])
print("名前の降順")
for player in sorted(teams.items(),key=lambda k:k[1]):
    print(player[0],player[1])
print("\n")
for player in sorted(teams.items()):
    print(player[0],player[1])

#ジェネレータ関数
def weekdays():
    wdays=["Sun","Mon","The","Wen","Tue","Fri","Sat"]
    for w in wdays:
        yield w
w=weekdays()
print(next(w))
print(next(w))
print("一休み")
#w=weekdays()
for x in w:
    print(x)
wdays=["Sun","Mon","The","Wen","Tue","Fri","Sat"]
w=(w for w in wdays)
for x in w:
    print(x)