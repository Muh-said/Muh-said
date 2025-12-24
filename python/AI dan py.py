# import random  # Pythonning ichki kutubxonasi, tasodifiy son yoki qiymat tanlaydi

# choices = ["tosh", "qaychi", "qogoz"]
# # Bu list — ma'lumot to‘plami. Uchta variantni ichiga saqlayapmiz.

# user = input("Tanlang (tosh/qaychi/qogoz): ")
# # input() - foydalanuvchidan ma'lumot olish. Terminalga yozganing shu yerga kiradi.

# bot = random.choice(choices)
# # random.choice() - ro‘yxatdan tasodifiy bittasini tanlaydi. Botning tanlovi.

# print("Bot:", bot)
# # Bot nimani tanlaganini chiqarib ko‘rsatadi.

# if user == bot:
#     print("Durrang")
# # Agar suz bilan bot bir xil bo'lsa — durang.

# elif (user == "tosh" and bot == "qaychi") or \
#      (user == "qaychi" and bot == "qogoz") or \
#      (user == "qogoz" and bot == "tosh"):
#     print("Yutding!")
# # Bu qism — yutish shartlari.
# # "and" — ikki shart ham to‘g‘ri bo‘lsa,
# # "or" — bir shart to‘g‘ri bo‘lsa ham bo‘ladi.

# else:
#     print("Yutqazding!")
# # Qolgan barcha holatlar — user yutqazgan.


# yosh = int(input("Yoshingni yoz: "))

# if yosh >= 18:
#     print("Siz katta yoshdasiz")
# else:
#     print("Siz hali kichiksiz")

# parol = "1234"
# user_input = input("Parolni kiriting: ")

# if user_input == parol:
#     print("Kirish ruxsat etildi")
#     for i in range(3):
#      print("Salom")

# else:
#     print("Parol noto‘g‘ri")
# for son in range(1, 11):
#     if son % 2 == 0:
#         print(son, "— juft")
#     else:
#         print(son, "— toq")
# parol = "1234"
# kiritma = ""

# while kiritma != parol:
#     kiritma = input("Parolni kiriting: ")

# print("Kirish ruxsat etildi")


# import random

# maxfiy_son = random.randint(1, 10)
# topildi = False

# while not topildi:
#     taxmin = int(input("1 dan 10 gacha son top: "))

#     if taxmin == maxfiy_son:
#         print("Topding!")
#         topildi = True
#     else:
#         print("Xato, yana urin")




# import random

# def oyin():
#     maxfiy = random.randint(1, 5)

#     taxmin = int(input("1-5 orasida son top: "))

#     if taxmin == maxfiy:
#         print("Topding!")
#     else:
#         print("Xato, to‘g‘risi:", maxfiy)

# oyin()
# def salom():
#     print("Boshladik!")

# def oyin():
#     salom()
#     print("O‘yin ketdi")

# oyin()


# def eng_katta(a, b, c):
#     if a >= b and a >= c:
#         return a
#     elif b >= a and b >= c:
#         return b
#     else:
#         return c
# print(eng_katta(2,4,2))


# a=10
# b=2
# c=a/b
# print(c)
