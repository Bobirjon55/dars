import os 
import random
os.system("cls")
"""
Masala:
MyList nomli class e`lon qling 
va unga listdan meros oling.
 MyListning random methodi parametr sifatida bitta N
, RAND_MIN*
, RAND_MAX* 
sonni qabul qilsin 
(RAND_MIN va RAND_MAX sonlariga qiymat berilmasiligi ham mumkin default: [-100, 100] oraliqda generatsiya qiling).
 N uzunlikdagi random sonlar bilan to'lgan arrayni
 foydalanuvchiga qaytaruvchi method tuzing.
"""
# class Mylist(list):
#     def random(self,n,rand_min=-100,rand_max=100):
#         a=[]
#         for i in range(n):
#             a.append(random.randint(rand_min,rand_max))
#         return a
        
# n=int(input("son kiriting"))
# a=Mylist()
# b=a.random(n,50)
# print(b)
"""
1) 1-class Soldat nomli, 
2-class esa Armiya nomli bo'lsin.
Ikkala classni vorislik orqali bog'lang
 va 18dan katta
 va jinsi erkaklarni chiqaring.
 Agar Soldat bo'yi<150 va vazni<75 bo'lsa,
 "Piyoda askarligiga" berilsin.
 Aks holda, "Tank qo'shinlariga" yo'nalish berilsin.
"""
#-+----------------------------------------------------------
# class Armiya(list):
#     def __init__(self):
#         self.ism=input("ism:")
#         self.yosh = int(input("yoshini kirit "))
#         self.vazn = int(input("vaznini kirit "))
#         self.boy = int(input("bo'yini kirit "))
#         self.jinsi = input("Jinsini kirit ")

# class Soldat(Armiya):
#     pass
#     def info(self):
#         return f"""
# Ismi - {self.ism}
# Yoshi-{self.yosh}
# Jinsi-{self.jinsi}
# Bo'yi-{self.boy}
# Vazni-{self.vazn}"""

# n=int(input("nechta soldat: "))
# soldatlar = []
# for i in range(n):
#     soldatlar.append(Soldat())
# piyoda=[]
# tank=[]
# for askar in soldatlar:
#     if askar.jinsi.lower() == "erkak" and askar.yosh > 18:
#          print(askar.ism,"xizmatga loyiq")
#          if askar.boy <150 and askar.vazn < 75:
#              piyoda.append(askar.info())
#          else:
#              tank.append(askar.info())
#     else:
#          print(askar.ism,"xizmatga noloyiq")
# print("tank qo'shinlari\n\n")
# print(*tank)
# print("\n\n piyoda askarlar\n\n")
# print(*piyoda)
