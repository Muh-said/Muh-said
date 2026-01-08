#37-das padeshka

# class Car:
#     """(self,make,model,year,km=0,price=None)"""
#     def __init__(self,make,model,year,km=0,price=None):
#         self.make = make
#         self.model = model
#         self.year = year
#         self.price = price
#         self.__km = km

#     def set_price(self,price):
#         self.price = price

#     def add_km(self,km):
#         """Mashinaning km ga yana km qo'shish"""
#         if km>=0:
#             self.__km += km
#         else:
#             raise ValueError("km manfiy bo'lishi mumkin emas")

#     def get_info(self):
#         info = f"{self.make.upper()} {self.model.title()}, "
#         info += f"{self.year}-yil, {self.__km}km yurgan."
#         if self.price:
#             info += f" Narhi: {self.price}"
#         return info

#     def get_km(self):
#         return self.__km












# def get_full_name(ism,familiya,otasi=''):
#   if otasi:
#    return f"{ism} {otasi} {familiya}".title()
#   else:
#     return f"{ism} {familiya}".title()
# komp_son = random.randint(0, 10)
# urinish = 0
# while True:
#      foy_son = int(input("0 dan 10 gacha son kiriting: "))
#      urinish += 1
#      if foy_son < komp_son:
#          print("Kattaroq son kiriting")
#      elif foy_son > komp_son:
#          print("Kichikroq son kiriting")
#      else:
#          print(f"Siz topdingiz! {urinish} ta urinishda 👌")
#          break
# past = 0
# yuqori = 10
# urinish = 0
# print("0 dan 10 gacha son o'ylang. Men topaman 😉")
# while True:
#      taxmin = (past + yuqori) // 2
#      urinish += 1
#      javob = input(f"Siz o'ylagan son {taxmin} mi? (+ / - / =): ")
#      if javob == "+":
#          past = taxmin + 1
#      elif javob == "-":
#          yuqori = taxmin - 1
#      elif javob == "=":
#          print(f"Men topdim! {urinish} ta urinishda 😎")
#          break
#      else:
#          print("Faqat +, - yoki = yoz")


# import avto_info_mod
# avto1=avto_info_mod.avto_info("GM","Malibu","qora","aftomat",2020,40000)
# avto_info_mod.info_print(avto1)
# import avto_info_mod as aim
# avto1=aim.avto_info("GM","Malibu","qora","aftomat",2020,40000)
# aim.info_print(avto1)
# from avto_info_mod import avto_info,info_print
# avto1=avto_info("GM","Malibu","qora","aftomat",2020,40000)
# info_print(avto1)
# from avto_info_mod import avto_info as ainfo, info_print as iprint
# avto1=ainfo("GM","Malibu","qora","aftomat",2020,40000)
# iprint(avto1)





# import random as r
# son = r.randint(0,12)
# print(son)

# ismlar =['olim','anvar','hasan','husan']
# ism = r.choice(ismlar)
# print(ism)

# print(r.choice(ism))#bunda ro'yhatdagi qiymati bitasini olib bita elementini kiritadi.
# x=list(range(11))
# print(x)
# r.shuffle(x)
# print(x)
