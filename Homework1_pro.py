﻿# Exercise 1
class Goods:
    def __init__(self,name,models,display,color):
        self.name=name
        self.models=models
        self.display=display
        self.color=color
    def slogan(self):
        return f"{self.name} slogan ### Is the best choice 2022"
    def __str__(self):
        return f"{self.name},{self.models},{self.display},{self.color}"
Goods_1=Goods("tv - ","***SAMSUNG***","IPS","black")
Goods_2=Goods("mobile telephone - ","***MOTOROLA***","AMOLED","Grey")
print(Goods_1,Goods_2,sep="\n")
print(Goods_1.slogan())
print(Goods_2.slogan())


#Exercise 2
class Buyer:
    def __init__(self,surname,name,age,telephone,nationality):
        self.surname=surname
        self.name=name
        self.age=age
        self.telephone=telephone
        self.nationality=nationality
    def __str__(self):
        return f"{self.surname},{self.name},{self.age},{self.telephone},{self.nationality}"
buyer_one=Buyer("Smith","George","55","08009379992","Englishman")
buyer_two=Buyer("McCallister","Kevin","12","+3901234567","American")
buer_three=Buyer("Rowling","Joanna","60","+8501234567899","Englishwoman")
print(buyer_one,buyer_two,buer_three,sep="\n")

#Exercise 3
class Order:
    def __init__(self,product,brend,model,color,surname,name,age,telephone,total_cost):
        self.product=product
        self.brend=brend
        self.model=model
        self.color=color
        self.surname=surname
        self.name=name
        self.age=age
        self.telephone=telephone
        self.total_cost=15000
    def __str__(self):
        return f"{self.product},{self.brend},{self.model},{self.color},{self.surname},{self.name},{self.age},{self.telephone},{self.total_cost}"
Order_one=Order("tv - ","***SAMSUNG***","NEO QLed","black","Smith","George","55","08009379992","")
Order_two=Order("mobile telephone - ","***MOTOROLA***","G60","Grey","McCallister","Kevin","12","+3901234567","")
print(Order_one,Order_two,sep="\n")
       
#Exercise_3

class Order_George:
    def __init__(self,product,brend,model,color,surname,name,age,telephone,cost):
        self.product=product
        self.brend=brend
        self.model=model
        self.color=color
        self.surname=surname
        self.name=name
        self.age=age
        self.telephone=telephone
        self.cost=cost
    def __str__(self):
        return f"{self.product},{self.brend},{self.model},{self.color},{self.surname},{self.name},{self.age},{self.telephone},{self.cost}"
Order_one=Order_George("tv - ","***SAMSUNG***","NEO QLed","black","Smith","George","55","08009379992",15000)
class Order_Kevin:
    def __init__(self,product,brend,model,color,surname,name,age,telephone,cost):
        self.product=product
        self.brend=brend
        self.model=model
        self.color=color
        self.surname=surname
        self.name=name
        self.age=age
        self.telephone=telephone
        self.cost=cost
    def __str__(self):
        return f"{self.product},{self.brend},{self.model},{self.color},{self.surname},{self.name},{self.age},{self.telephone},{self.cost}"
Order_two=Order_Kevin("mobile telephone - ","***MOTOROLA***","G60","Grey","McCallister","Kevin","12","+3901234567",9000)
print(Order_one,Order_two,sep="\n")
