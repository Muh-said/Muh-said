# # reduce() NIMA?
# # reduce() — hammasini olib, bitta qiymat qiladi.
# # 📌 reduce() funksiya emas, uni chaqirish kerak:
# from functools import reduce

# sonlar = [1, 2, 3, 4]
# sonlar=[4,5,6,7,8]
# natija = reduce(lambda a, b: a + b, sonlar)
# print(natija)


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


# parol = "1707"
# user_input = input("Parolni kiriting: ")
# while user_input != parol:
#      print("Parol noto'g'ri")
#      user_input = input("Parolni kiriting: ")
# print("Kirish ruxsat etildi keling bila o'yin o'ynimiz")

# import random

# # 1️⃣ Kompyuter son o‘ylaydi, foydalanuvchi topadi
# def computer_thinks_user_guesses(x=10):
#     yashirin_son = random.randint(0, x)
#     urinishlar = 0

#     while True:
#         taxmin = int(input(f"0 dan {x}gacha son kiriting: "))
#         urinishlar += 1

#         if taxmin < yashirin_son:
#             print("Katta son kiriting")
#         elif taxmin > yashirin_son:
#             print("Kichik son kiriting")
#         else:
#             print(f"✅ Siz topdingiz! {urinishlar} ta urinishda")
#             return urinishlar


# # 2️⃣ Foydalanuvchi son o‘ylaydi, kompyuter topadi
# def user_thinks_computer_guesses(x=10):
#     print(f"0 dan {x} gacha son o‘ylang (ichingizda)")
#     input("Tayyor bo‘lsangiz Enter bosing...")

#     past = 0
#     yuqori = 10
#     urinishlar = 0

#     while True:
#         taxmin = (past + yuqori)//2
#         urinishlar += 1

#         javob = input(f"Siz o‘ylagan son {taxmin} mi? (+, -, t) :")

#         if javob == "+":
#             past = taxmin + 1
#         elif javob == "-":
#             yuqori = taxmin - 1
#         elif javob == "t":
#             print(f"🤖 Kompyuter topdi! {urinishlar} ta urinishda")
#             return urinishlar


# # 3️⃣ O‘yinni boshlash va g‘olibni aniqlash
# user_urinish = computer_thinks_user_guesses()
# computer_urinish = user_thinks_computer_guesses()

# print("\n📊 NATIJA:")
# print(f"Siz: {user_urinish} ta urinish")
# print(f"Kompyuter: {computer_urinish} ta urinish")

# if user_urinish < computer_urinish:
#     print("🏆 SIZ YUTDINGIZ!")
# elif user_urinish > computer_urinish:
#     print("🤖 KOMPYUTER YUTDI!")
# else:
#     print("🤝 DURRANG!")




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




# for son in range(1, 11):
#      if son % 2 == 0:
#          print(son, "— juft")
#      else:
#          print(son, "— toq")





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
