import os
os.system("cls")
from abc import *
from math import *
# #-------------------------------------
# #2-masala
# class Mashina:
#     def __init__(self, nomi:str, turi:str, yili:int, narxi:float=4000):
#         self.nomi = nomi
#         self.turi = turi
#         self.narxi  = narxi
#         self.yili = yili

#     def Malumot(self):
#         return f"""
# Nomi: {self.nomi}
# Turi: {self.turi}
# Narxi: {self.narxi}
# Yili: {self.yili}"""


# car1 = Mashina("K5",      "Yengil",2020,35000)
# car2 = Mashina("Opel",    'Yengil',2008, 10000)
# car3 = Mashina("nexia",   "yengil",2007,5000)
# car4 = Mashina("lasetti", "yengil",2013,11000)
# car5 = Mashina("matiz",   "yengil",2018)
# car6 = Mashina("malibu",  "yengil",2022,34000)
# car7 = Mashina("howo",    "ogir",  2015,40000)
# car8 = Mashina("mersedes","yengil",2002,8000)
# car9 = Mashina("bmw",     "yengil",2009,20000)
# car10 = Mashina("shaqman","ogir",  2014,36000)
# lst = [car1, car2, car3, car4, car5, car6, car7, car8, car9, car10]
# lst.sort(key=lambda x: x.yili)
# for i in range(len(lst)):
#      print(lst[i].Malumot())
# #------------------------------------------------------
# # 3-masala
# class Countries:
#     def __init__(self, nomi, poytaxti, aholisi, maydoni, prezidenti):
#         self.nomi = nomi
#         self.poytaxti = poytaxti
#         self.aholisi = aholisi
#         self.maydoni = maydoni
#         self.prizidenti = prezidenti

#     def Malumot(self):
#         return f"""
# Davlat nomi: {self.nomi}
# Poytaxti: {self.poytaxti}
# Aholis soni: {self.aholisi}
# Yer maydoni: {self.maydoni}
# Prezidenti: {self.prizidenti}"""


lst = []
for i in range(4):
    d=input("Davlat nomi:")
    p=input("poytaxti: ")
    a=int(input("Aholi soni: "))
    s=float(input("maydoni:"))
    _=input("Prezidenti: ")
    davlat = Countries(d,p,a,s,_)
    lst.append(davlat)
lst.sort(key=lambda x: x.nomi)
for i in range(len(lst)):
    print(lst[i].Malumot())

