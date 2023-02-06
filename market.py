from datetime import datetime

name=input("Enter your name:")

lists="""
Rice   Rs 35/kg
Suger  Rs 25/kg
Salt   Rs 18/kg
Oil    Rs 120/liter
Magi   Rs 120/kg
Boost  Rs 90/each
Paneer Rs 110/kg
Water  Rs 20/liter
Milk   Rs 25/each
Eggs   Rs 5/each
"""
#declaration
price=0
pricelist=[]
totalprice=0
Finalfinalprice=0
ilist=[]
qlist=[]
plist=[]

#rates for items
items={'rice':35,
'suger':25,
'salt':18,
'oil':120,
'magi':120,
'boost':90,
'paneer':110,
'water':20,
'milk':25,
'eggs':5}
option=int(input("for list of items press 1:"))
if option==1:
    print(lists)
for i in range(len(items)):
    inpl=int(input("if you want to buy press 1 or 2 for exist:"))
    if inpl==2:
        break
    if inpl==1:
        item=input("Enter your items:") 
        quantity=int(input("Enter quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,quantity,items,price))
            totalprice+=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
            print("sorry you enterted item is not avilable")
    else:
        print("you enterted wrong number")
    inp=input("can i bill items yes or no:")
    if inp=='yes':
        pass
        if finalamount!=0:
            print(25*"*","Krishna supermarket",25*"*")
            print(28*"  ","Kakinada")
            print("Name:",name,30*" ","Date:",datetime.now())
            print(75*"-")
            print("Sno",12*" ",'items',5*" ",'Quantity',3*" ",'price')
            for i in range(len(pricelist)):
                print(i,8*' ',6*' ',ilist[i],5*" ",qlist[i],6*" ",plist[i])
                print(75*"-")
                print(50*" ",'totalamount:','Rs',totalprice)
                print("gst amount",50*" ",'Rs',gst)
                print(75*"-")
                print(50*" ",'Finalamount:','Rs',totalprice)
                print(75*"-")
                print(50*"","Thanks for visting")


