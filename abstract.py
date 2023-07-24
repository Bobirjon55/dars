from abc import ABC, abstractmethod
import os 
os.system("cls")
class Asosiy:
    @abstractmethod
    def plus(self,son):
        pass
class Calculator(Asosiy):
    def __init__(self,son):
         self.son=son
  

n=float(input("son kiriting: "))
misol=Calculator(n)

misol.plus(5)
print(misol.son)

# from abc import ABC, abstractmethod
# from os import system
# system("cls")


# class SeniorCar(ABC):
#     def __init__(self):
#         pass

#     @abstractmethod
#     def qayrilish(self):
#         print("seriyor qayrildi")

#     @abstractmethod
#     def yurish(self):
#         pass



# class JuniorCar(SeniorCar):
#     def qayrilish(self):
#         super().qayrilish()

#     def yurish(self):
#         print("Yurdim")


# jc = JuniorCar()
# jc.qayrilish()