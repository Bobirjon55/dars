import os
os.system("cls")
# #-----------------------1--------------------------------------------------
# class Kitob:
#     def __init__(self,name:str,aftor:str,price:float,press:str):
#         self.nomi=name
#         self.muallif=aftor
#         self.narxi=price
#         self.nashriyot=press
#         self.tekshir()
#     def tekshir(self):
#         if self.nashriyot[0].lower()>="a" and self.nashriyot[0].lower()<="h":
#             self.malumot()
#     def malumot(self):
#         print( f"""nomi: {self.nomi}
# muallif: {self.muallif}
# narxi: {self.narxi}
# nashriyot:{self.nashriyot}
# """)

# kitob1=Kitob("Sehrli Qalpoqcha","xudoyberdi Toxtaboyev",30_000.0,"asaxiy")
# kitob2=Kitob("Boburnoma","Bobur",20_000,"Hilol nashr")
# kitob3=Kitob("uchinchi","Bobirjon",100_000,"Nashriyot")
# kitob4=Kitob("To'rtinchi","Adham aka",200_000,"Bobir nashr")
# kitob5=Kitob("beshinchi","nomalum",10_000,"Darakchi")
# #--------------------------------------------------------------------------
# #--------------------2---------------------------------------------------
# class Kompyuter:
#     def __init__(self,name:str,RAM:int,price:float,prosses:str):
#         self.nomi=name
#         self.RAM=RAM
#         self.narxi=price
#         self.pro=prosses
#         self.tekshir()
#     def tekshir(self):
#         if self.RAM>=4 and self.RAM<=16:
#             self.malumot()
#     def malumot(self):
#         print( f"""nomi: {self.nomi}
# RAM: {self.RAM}
# narxi: {self.narxi}
# protsessor:{self.pro}
# """)

# laptop1=Kompyuter("Dell",4,500,"AMD ryson 7")
# laptop2=Kompyuter("HP",8,400,"intel core I5")
# laptop3=Kompyuter("Asus",16,900,"intel core I9")
# laptop2=Kompyuter("lenovo",3,300,"pentum 4")
# #--------------3-------------------------------------------------------
# class User:
#     def __init__(self):
#         self.NickName=""
#         self.name=""
#         self.surname=""
#         self.email=""
#         self.get_info()
#     def get_info(self):
#         self.NickName=input("nick name: ")
#         self.name=input("ism: ")
#         self.surname=input("familiya: ")
#         self.email=input("@email: ")
#         self.malumot()
#     def malumot(self):
#         print( f"""Foydalanuvchi: {self.NickName}
# ismi: {self.name} {self.surname}
# @email: {self.email}
# """)

# foydalanuvchi=User()

# #-------------4----------------------------------------
# class SpaceAircraft:
#     def __init__(self,name:str,height:int,fuel:float):
#         self.nomi=name
#         self.baladlik=height
#         print(f"""nomi {self.nomi}
# balandlik {self.baladlik} m
# """)
#         self.yoqilgi=fuel
#     def launch(self,masofa):
#         if 0>self.yoqilgi-masofa/10:
#             print("yoqilgi yetmaydi")
#             self.yoqilgi=self.yoqilgi-masofa/10
#             return 0
#         else:
#             print(f"uchishga sarflangangan yoqilgi {masofa/10}")
#             self.yoqilgi=self.yoqilgi-masofa/10
#             self.land(masofa)
#     def land(self,masofa):
#         if self.yoqilgi>=masofa/20:
#             print("Succsesfully land")
#             self.yoqilgi=self.yoqilgi-masofa/20
#         else:
#             print("No fuel")
#             print(f"qonish uchun {masofa/20} l yoqigi kerak")

# print("""Raketa  uchish uchun 100/10 yoqilgi sarflaydi
# qo'nish uchun esa 100/5 sarflaydi""")

# n=float(input("qancha yoqigi: "))

# rocket=SpaceAircraft("Patfainder",30,n)

# a=float(input("qancha balandlikka uchmoqchisiz: "))
# rocket.launch(a)
# if rocket.yoqilgi>=0:
#     print(f"qolgani {rocket.yoqilgi}")
# #---------------------5---------------------------------

# class MinuteConvertor:
#     def __init__(self,minut:int) -> None:
#         self.minut=minut
#     def toHours(self):
#         print(self.minut//60,"soat")
#     def toSeconds(self):
#         print(self.minut*60,"sekund")
#     def toDays(self):
#         print(self.minut//60//24,"kun")



# n=int(input("minut kiriting: "))
# vaqt=MinuteConvertor(n)

# vaqt.toHours()
# vaqt.toSeconds()
# vaqt.toDays()




























#--------------------------------------------------------------------------------------------------
# class Kitob():
#     def __init__(self,nomi,  mualifi,  narxi,   nashiryoti):
#         self.nomi = nomi
#         self.muallifi = mualifi
#         self.narxi = narxi
#         self.nashriyot = nashiryoti
  
#     def malumot(self):
#        print(f"""Kitob  Nomi: {self.nomi}
# Kitob  Nomi: {self.muallifi}
# Kitob  Nomi: {self.narxi}
# Kitob  Nomi: {self.nashriyot}""")

# k = Kitob(input("Nomi "), input("Egasi "),input("Narxi  "),  input("Nashiryoti "))
# k.malumot()

