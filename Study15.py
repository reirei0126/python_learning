bin=[2**n for n in range(1,17,1)]
print(bin)
price=[100,250,300]
tax=1.1
total=[int(p*tax) for p in price]
print(total)
rank=[r+"ランク"for r in "ABCDEF"]
print (rank)
gusuu=[n for n in range(0,10,1) if n%2==0]
print(gusuu)
citys=["新潟県長岡市","東京都新宿区","新潟県三条市","北海道札幌市"]
niigata_citys=[city[3:] for city in citys if city.startswith("新潟県")]
print(niigata_citys)
test=[("A","合格"),("B","合格"),("C","不合格"),("D","合格")]
passed=[x[0] for x in test if x[1]=="合格"]
print(passed)
team=["a","b","c"]
point=[2,43,156]
team_dic={t:p for t,p in zip(team,point)}
print(team_dic)
team_dic={str(p):t for t,p in team_dic.items()}
print(team_dic)