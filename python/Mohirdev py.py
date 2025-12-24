#24- lombta

from math import sqrt #sqrt - kvadrat ildiz
sonlar = list(range(11))#0 dan 10 gacha sonlar ro'yhat
ildizlar =list(map(sqrt,sonlar))#map bu ildiz
# print(ildizlar)

def daraja2(x):
  """Berilgan sonning kvadratini qaytaruvchi funksiya"""
  return x*x
print(list(map(daraja2,sonlar)))

# import math

# def daraja(n):
#   return lambda x :x**n
# kvadrat =daraja(2)
# kub = daraja(3)
# print(f"3-ning kavdrati {kvadrat(3)} ga,"
#       f"kubi{kub(3)} gat eng")

# uzunlik=lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))
# kvadrat =lambda x, y : x ** y
# print(kvadrat(3,2))
#22-dars Moslashuvchan Funksiyalar
#uy ishi

# def ism_toliq(ism, familiya,**yana):
#      """Funksiya ism va familiyani jamlab chiqaradi"""
#      yana['ism']=ism
#      yana['familiya']=familiya
#      return yana
# ism1=ism_toliq('muhammad','said', yosh=[15] )
# ims2=ism_toliq('abduloh','kabirov')
# print(ism1)
# print(ims2)

# def kopaytir(*sonlar):
#     natija = 1
#     for son in sonlar:
#         natija *= son
#     return natija

# print(kopaytir(2, 3))        # 6
# print(kopaytir(2, 3, 4))     # 24

# def avto_info(kompaniya,model,**malumotlar):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
# avto1 = avto_info("GM", "malibu", rang='qora', yil=2018)
# avto2 = avto_info("Kia", "K5", rang='qizil', narh=35000)
# print(avto1)
# print(avto2)

# def summa(*sonlar):
#   """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#   return sum(sonlar)

# print(summa(2))
# print(summa(1,2,3,4,5,6))
# print(summa(4,5,6,7,8,9))


# def summa(*sonlar):
#     """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
#     yigindi = 0
#     for son in sonlar:
#         yigindi += son
#     return yigindi

# print(summa(1,2,3,4,5,6,7,8,9))
# print(summa(2,2))


#21-dars Funksiya va ro'yhat
#uy ishi
#3

# talabalar = ['ali', 'vali', 'hasan', 'husan']
#
# def bahola(ismlar):
    # baholar = {}
    # for ism in ismlar:
        # baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
        # baholar[ism]=baho
    # return baholar
#
# baholar = bahola(talabalar)
# print(baholar)
# print(talabalar)
#

#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning bahosini kiriting:")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['ali','vali','hasan','husan']
# baholar=bahola(talabalar[:]) #bunda copya qilvoti [:] bu cod orqali
# print(baholar)
# print(talabalar)
#2
# def katta_harf(matnlar):
#     matnlar = matnlar[:]
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()
#     return matnlar

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# yangi_ismlar = katta_harf(ismlar)
# print(ismlar)
# print(yangi_ismlar)
#1
# def katta_harf(matnlar):
#     for i in range(len(matnlar)):
#         matnlar[i]=matnlar[i].title()

# ismlar = ['ali', 'vali', 'hasan', 'husan']
# katta_harf(ismlar)
# print(ismlar)

# def bahola(ismlar):
#     baholar={}
#     while ismlar:
#         ism=ismlar.pop()
#         baho = input(f"Talaba {ism.title()} ning bahosini kiriting:")
#         baholar[ism]=int(baho)
#     return baholar
# talabalar=['ali','vali','hasan','husan']
# baholar=bahola(talabalar[:]) #bunda copya qilvoti [:] bu cod orqali
# print(baholar)
# print(talabalar)



#20-dars qiymat qaytaruvchi
# funksiyalar:
#uy ishi:
# ...existing code...
#uy ishi:
# (import email o'chirildi)

# def ismi_toliq(ism, familiya, tugilgan_yil, tugilgan_joy, email, tel=None, yosh=None):
    # """Foydalanuvchidan ism, familiya, tug'ilgan yil, telefon raqami, email va (ixtiyoriy) yosh olib lug'at ko'rinishida qaytaruvchi funksiya.

    # Agar `yosh` qiymati berilmagan bo'lsa va `tugilgan_yil` butun son bo'lsa, yosh 2025 - tugilgan_yil orqali hisoblanadi."""
    # Agar foydalanuvchi yosh kiritmagan bo'lsa, tug'ilgan yildan hisoblashga harakat qilamiz
    # if yosh is None and isinstance(tugilgan_yil, int):
    #    yosh = 2025 - tugilgan_yil

    # ismt = {
        # 'ism': ism,
        # 'familiya': familiya,
        # 'tugilgan_yil': tugilgan_yil,
        # 'tugilgan_joy': tugilgan_joy,
        # 'email': email,
        # 'tel': tel,
        # 'yosh': yosh   }
    # return ismt

# print("Foydalanuvchi haqida ma'lumotlarni kiriting.")
# foydalanuvchilar = {}
# while True:
    # print("\nQuyidagi ma'lumotlarni kiriting")
    # ism = input("Ismingiz: ").strip()
    # familiya = input("Familiyangiz: ").strip()

    # tugilgan_yil_input = input("Tug'ilgan yilingiz: ").strip()
    # try:# XATO LIGINI BILIB TURIB BITA TEKSHIR VOR DEGANI
        # tugilgan_yil = int(tugilgan_yil_input)
    # except ValueError:# agar raqamga aylantirib bo'lmasa
        # tugilgan_yil = tugilgan_yil_input  # agar raqam emas bo'lsa satr saqlanadi

    # tugilgan_joy = input("Tug'ilgan joyingiz: ").strip()
    # email = input("Email manzilingiz: ").strip()
    # telefonni int ga aylantirish (bo'sh qoldirilsa None)
    # while True:
        # tel_input = input("Telefon raqamingiz (faqat raqamlar, bo'sh qoldirish mumkin): ").strip()
        # if tel_input == '':
            # tel = None
            # break
        # try:# telefon raqamini int ga aylantirishga harakat qilamiz
            # tel = int(tel_input)
            # break
        # except ValueError:
            # print("Iltimos, telefon raqamni faqat raqamlar bilan kiriting (masalan: 123456789).")

    # foydalanuvchilar[ism] = ismi_toliq(ism, familiya, tugilgan_yil, tugilgan_joy, email, tel)
    # javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ").strip().lower()
    # if javob in ('no', 'n'):
        # break

# print("\nFoydalanuvchilar ro'yxati:")
# for ism, info in foydalanuvchilar.items():
    # tel = info.get('tel')
    # tel_display = str(tel) if tel is not None else "Noma'lum"
    # tug_yil = str(info.get('tugilgan_yil'))
    # yosh = info.get('yosh')
    # yosh_display = str(yosh) if yosh is not None else "Noma'lum"
    # print(f"{info['ism'].title()}, {info['familiya'].title()}, {tug_yil}, {info['tugilgan_joy'].title()}, yosh: {yosh_display}, Tel: {tel_display}. Email: {info['email']}")
# ...existing code...






# import email


# def ismi_toliq(ism, familiya, tugilgan_yil, tugilgan_joy, email, tel=None):
#     """Foydalanuvchidan ism, familiya, tug'ilgan yil, telefon raqami va email olib lug'at ko'rinishida qaytaruvchi funksiya"""
#     ismt = {'ism': ism,
#               'familiya': familiya,
#               'tugilgan_yil': tugilgan_yil,
#               'tugilgan_joy': tugilgan_joy,
#               'email': email,
#               'tel': tel}
#     return ismt
# print("Foydalanuvchi haqida ma'lumotlarni kiriting.")
# foydalanuvchilar = {} # bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting", end='')
#     ism = input("Ismingiz: ")
#     familiya = input("Familiyangiz: ")
#     tugilgan_yil = input("Tug'ilgan yilingiz: ")
#     tugilgan_joy = input("Tug'ilgan joyingiz: ")
#     email = input("Email manzilingiz: ")
#     tel = input("Telefon raqamingiz: ")
#     foydalanuvchilar[ism] = ismi_toliq(ism, familiya, tugilgan_yil, tugilgan_joy, email, tel)
#     javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ")
#     if javob == 'no':
#         break
# print("\nFoydalanuvchilar ro'yxati:")
# for ism in foydalanuvchilar:
#     if     # ...existing code...
#     #uy ishi:
#     # (import email o'chirildi)
#     def ismi_toliq(ism, familiya, tugilgan_yil, tugilgan_joy, email, tel=None):
#         """Foydalanuvchidan ism, familiya, tug'ilgan yil, telefon raqami va email olib lug'at ko'rinishida qaytaruvchi funksiya"""
#         ismt = {
#             'ism': ism,
#             'familiya': familiya,
#             'tugilgan_yil': tugilgan_yil,
#             'tugilgan_joy': tugilgan_joy,
#             'email': email,
#             'tel': tel
#         }
#         return ismt

#     print("Foydalanuvchi haqida ma'lumotlarni kiriting.")
#     foydalanuvchilar = {}
#     while True:
#         print("\nQuyidagi ma'lumotlarni kiriting")
#         ism = input("Ismingiz: ").strip()
#         familiya = input("Familiyangiz: ").strip()

#         tugilgan_yil_input = input("Tug'ilgan yilingiz: ").strip()
#         try:
#             tugilgan_yil = int(tugilgan_yil_input)
#         except ValueError:
#             tugilgan_yil = tugilgan_yil_input  # agar raqam emas bo'lsa satr saqlanadi

#         tugilgan_joy = input("Tug'ilgan joyingiz: ").strip()
#         email = input("Email manzilingiz: ").strip()

#         # telefonni int ga aylantirish (bo'sh qoldirilsa None)
#         while True:
#             tel_input = input("Telefon raqamingiz (faqat raqamlar, bo'sh qoldirish mumkin): ").strip()
#             if tel_input == '':
#                 tel = None
#                 break
#             try:
#                 tel = int(tel_input)
#                 break
#             except ValueError:
#                 print("Iltimos, telefon raqamni faqat raqamlar bilan kiriting (masalan: 998901234567).")

#         foydalanuvchilar[ism] = ismi_toliq(ism, familiya, tugilgan_yil, tugilgan_joy, email, tel)
#         javob = input("Yana ma'lumot qo'shasizmi? (yes/no): ").strip().lower()
#         if javob in ('no', 'n'):
#             break

#     print("\nFoydalanuvchilar ro'yxati:")
#     for ism, info in foydalanuvchilar.items():
#         tel = info.get('tel')
#         tel_display = str(tel) if tel is not None else "Noma'lum"
#         tug_yil = str(info.get('tugilgan_yil'))
#         print(f"{info['ism'].title()}, {info['familiya'].title()}, {tug_yil}, {info['tugilgan_joy'].title()}, Tel: {tel_display}. Email: {info['email']}")
#     # ...existing code...ism[tel]:
#         tel = ism[tel]
#     else:
#         tel = "Noma'lum"
#     print(f"{ism['ism'].title()}, {ism['familiya'].title()},{ism['tugilgan_yil'].title()},{ism['tugilgan_joy'].title()}, {tel}. Email: {ism['email'].title()}")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {karobka} korobka. Narh: {narh}$")




# def avto_info(kompaniya, model, rang, karobka, yil, narh=None):
#     """Avto haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
#     avto = {'kompaniya': kompaniya,
#             'model': model,
#             'rang': rang,
#             'karobka': karobka,
#             'yil': yil,
#             'narh': narh}
#     return avto
# print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
# avtolar=[] #salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya = input("Ishlab chiqaruvchi: ")
#     model = input("Modeli: ")
#     rang = input("Rangi: ")
#     karobka = input("Karobka: ")
#     yil = input("Ishlab chiqarilgan yili: ")
#     narh = input("Narh: ")
#     avtolar.append(avto_info(kompaniya, model, rang, karobka, yil, narh))
#     javob = input("Yana avto qo'shasizmi? (yes/no): ")
#     if javob=='no':
#        break
# print("\nSalonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang'].title()} {avto['model'].title()}, {karobka} korobka. Narh: {narh}$")



# def oraliq(min,max,qadam=1): #bunda qadam qiymati 1 ga teng deb olinadi yoki foydalanuvchi qiymat kiritmasa ham bo'ladi
#     """min dan max gacha bo'lgan sonlar yig'indisini hisoblaydigan funksiya"""
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam #bunda min qiymatiga qadam qiymati qo'shiladi
#     return sonlar

# print(oraliq(1,10,2))
# print(oraliq(5,15,2))
# print(oraliq(10,16))





# def avto_info(kompaniya, model, rang, karobka, yil, narh=None):
  #  avto = {'kompaniya': kompaniya,
          #  'model': model,
          #  'rang': rang,
          #  'karobka': karobka,
          #  'yil': yil,
          #  'narh': narh}
  #  return avto


# avto1 = avto_info('gm','Malibu','qora','avto',2020)
# avto2 = avto_info('GM ','Gentira','ko\'k','mexanika',2010,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avto ro\'yhati:')
# for avto in avtolar:
    # if avto['narh']:
    #  narh = avto['narh']
    # else:
    #  narh = "Noma'lum"
    #  print(f"{avto['model']},{avto['yil']}-yil. Narhi: {narh}")

# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):#bunda ihtiyori foydalanuvchi otasini ismini kiritma sa ham bo'ladi
#     """Foydalanuvchidan ism, familiya va otasining ismini olib to'liq ism qaytaruvchi funksiya"""
#     if otasining_ismi:  # agar otasining_ismi kiritilgan bo'lsa
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"
#     else:# aks holda
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()
# talaba1=toliq_ism_yasa('muhammad', 'shukurullayev', 'abdukarimovich')
# talaba2=toliq_ism_yasa('abuduloh','kahabirov')
# print(f"{talaba1} {talaba2} salom darsga hush kelibsizlar!")

# def ism_familiya(ism, familiya):
#     """Funksiya ism va familiyani jamlab chiqaradi"""
#     ism_familiya =f"{ism} {familiya}"
#     return ism_familiya.title()#return bu qiymat qaytaradi degani
# talaba1=ism_familiya('muhammad','said')
# talaba2=ism_familiya('abdu','karimov')
# print(talaba1)
# print(talaba2)


# def ism_toliq(ism, familiya):
#     """Funksiya ism va familiyani jamlab chiqaradi"""
#     ism_familiya =f"{ism} {familiya}"
#     print(ism_familiya.title())
# ism_toliq('muhammad','said')
# ism_toliq('abduloh','kabirov')

#19-funksiya:
#uy ishi:
#4
# def kota_kichkina(matin):
#     """Foydalanuvchidan matn olib uni katta va kichik harifda chiqaradigan funiksiya"""
#     print(matin.upper())
#     print(matin.lower())
# kota_kichkina("Salom Dunyo")
# kota_kichkina("Python dasturlash tili")


#3
# def juft_toq(son):
#     """Foydalanuvchidan son olib juft yoki toqligini aniqlaydigan funiksiya"""
#     if son % 2==0:#bu shart son juft ekanligini tekshiradi % bu qo'ldiqchiqadimi yomi deydi  == bu tengmi degani
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")
# juft_toq(7)
# juft_toq(8)



#2
# def kvadrat_kub(son):
#    """Foydalanuvchidan son olib uning kvadrati va kubini hisoblaydigan funiksiya"""
#    print(f"{son} ning kvadrati {son**2} ga teng \n"
#           f"{son}ning kubi {son**3} ga teng")
# kvadrat_kub(3)
# kvadrat_kub(9)




# 1
# def ism_yil(ism,tyil):
#   """Foydalanuvchidan ism va tug'ilgan yilini olib yoshini hisoblaydigan funiksiya"""
#   print(f"Salom {ism} siz {2025-tyil} yoshdasiz")
# ism_yil('Muhammad Said',2010)


# def ism_yil(ism,tyil):
#   """Foydalanuvchidan ism va tug'ilgan yilini olib yoshini hisoblaydigan funiksiya"""
#   print(f"Salom {ism} siz {2025-tyil} yoshdasiz")
# ism_yil('Muhammad Said',2010)

# ism_yil(2010,'Abdulloh')   #bunda xatolik beradi chunki qiymatlar joyi almashtirilgan


# def ism_yil(ism,tyil):
#   """Foydalanuvchidan ism va tug'ilgan yilini olib yoshini hisoblaydigan funiksiya"""
#   print(f"Salom {ism} siz {2025-tyil} yoshdasiz")
# ism_yil(tyil=2010,ism='Abdulloh')  #bunda qiymatlar joyi almashtirilgan bo'lsa ham to'g'ri ishlaydi



# def ism_familiya(ism,familiya):
#   """Foydalanuvchidan ism va familyani olib birlastirib chiqaradigan funiksiya"""
#   print(f"salom {ism} ismli shahs {familiya} familiyasi bilan tanishganimdan hursandman")
# ism_familiya('Muhammad Said','shukurullayev')
# ism_familiya('Abdulloh','Karimov')


# def salom_ber():
#     """Salom beradigan funiksiya"""
#     print("Assalomu alaykum!")

# salom_ber()




# #18-dars:while sikli:
# talabalar = ['hasan', 'husan', 'olim', 'botir']
# baholangan_talabalar = {}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting: ")
#     print(f"{talaba.title()} baholandi")
#     baholangan_talabalar[talaba] = baho


# cars = ['toyota', 'kia','mazda', 'kia','hyundai', 'gm', 'kia']
# while 'kia' in cars:
#   cars.remove('kia')
#   print(cars)
# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh) # ism kalit, yosh qiymat

#     javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
#     if javob == "yo'q":
#         ishora = False

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# #
# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# ismlar=[]
# n=1
# while True:
    # savol=f"{n}-do'stingizning ismini kiriting:"
    # ism=input(savol)
    # ismlar.append(ism)
    # takrorlash=input("Yana ism qo'shasizmi? (ha/yo'q):")
    # n+=1
    # if takrorlash !='ha':
        # break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
    # print(ism.title())




#17-While sikli:

#uy ishi:
#2


# savol = "Yoshingizni kiriting: "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)

#     if yosh<7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else: narh = 0

#     if narh==0:
#         print("Sizga chipta bepul")
#     else:
#         print(f"Chipta {narh} so'm")



# 1

# parol = "0717"
# kiritma = ""

# while kiritma != parol:
#     kiritma = input("Parolni kiriting: ")

# print("Kirish ruxsat etildi")

# print("Siz yoqtirgan kitobingizni kiring:")
# kitoblar = "(dasturni toxtatish uchun'stop'deb yozing)"
# kitoblar += "\nKitob nomi kiriting:"
# kitoblar=' '
# while True:
#     kitob=input(kitoblar)
#     if kitob=='stop':
#         break
#     else:
#         print(f"{kitob} zo'r yanabormi kitobingiz!")


#continue va while operatori misoli
# son = 0
# while son<10:
#   son+=1
#   if son%2!=0:
#         continue
#   print(son)#bunda faqat juft sonlar chiqadi





#continue  va for operatori misoli
#
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son==5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")


#break va for operatori misoli

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son==7:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")



#wihile va break operatori misoli

# print("Kiritilgan sonning kvadratini hisoblaydigan dastur.")
# savol = "Son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit'deb yozing):"
# while True: # abadiy sikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # siklni to'xtatish
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi, foydalanganingiz uchun rahmat!")


#wihile va ishora operatori misoli

# print ("Kirirtilgan sonning kvadratini hisoblaydigan dastur.")
# savol = "Son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit'deb yozing):"
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora =False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi, foydalanganingiz uchun rahmat!")



#wihile va input operatori misoli

# print("Kiritligansoningizni kvadratini hisoblaydigan dastur.")
# savol = "Son kiriting"
# savol += "(dasturni to'xtatish uchun 'exit'deb yozing):"
# qiymat = ' '
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi, foydalanganingiz uchun rahmat!")


# son = 1
# while son<=5:
#     print(son, end=' ')
#     son+=1
# print("\nDastur tugadi")

# ism=input("Ismingiz nima?...")
# savol=f"Salom {ism.title()} Yoshingiz nechida?..."
# yosh=int(input(savol))
# print(f"Salom {ism.title()}siz {yosh} yoshda ekansiz!")

#16-dars:Nesting:

 #uy ishi:

# abu={
#  'ism':['Abu Abdulloh Muhammad ibn Ismiol'],
#  'yoshi':['810-yilda Buxoroda tavallud topgan'],
#  'umirk':['60-yil umr ko\'rgan'],
# }
# abdu={
# 'ism':['Abdulla Qodiriy'],
# 'yoshi':['1894-yilda Toshkentda tavallud topgan'],
# 'umirk':['44-yil umr ko\'rgan'],
# }
# navoiy={
# 'ism':['Alisher Navoiy'],
# 'yoshi':['1441-yilda Hirotda tavallud topgan'],
# 'umirk':['60-yil umr ko\'rgan'],
# }
# erkin={
#   'ism':['Erkin Vohidov'],
#   'yoshi':['1936-yilda Farg\'onada tavallud topgan'],
#   'umirk':['80-yil umr ko\'rgan']
# }
# shahs=[abu,abdu,navoiy,erkin]
# for sh in shahs:
#   for k,q in sh.items():
#     print(f"{k}:{', '.join(q)}")
#   print( end=' ')

# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()}, "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}. \n"
#           "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())

# dasturchilar = {
#   'ali':['paython', 'c++'],
#   'vali':['html','css','js'],
#   'husan':['php','sql'],
#   'maryam':['java','c#']
# }
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
#     for til in tillar:
#         print(f"{til.upper()}",end=' ')

# malibus=[]
# for n in range(10):
#     new_car = {
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narh':None,
#         'km':0,
#         'korobka':'afto'
#         }
#     malibus.append(new_car)

# # for malibu in malibus:
# #     print(malibu)
# for malibu in malibus[:3]:
#     malibu['rang']='ko\'k'

# for malibu in malibus[3:6]:
#     malibu['rang']='qizil'

# for malibu in malibus[6:]:
#     malibu['rang']='oq'
#     malibu['korobka']='mexanika'

# for malibu in malibus:
#     if malibu['korobka']=='afto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=35000

# for malibu in malibus:
#      print(malibu)

# car0 = {
#     'model':'malibu ',
#     'rang':'qora',
#     'yil':2020,
#     'narh':40000,
# }

# car1 = {
#     'model':'nexia 3',
#     'rang':'oq',
#     'yil':2019,
#     'narh':15000,
# }
# car2 = {
#     'model':'gentra',
#     'rang':'qizil',
#     'yil':2018,
#     'narh':17000,
# }
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()},"
#           f"{car['rang']} rang,"
#           f"{car['yil']}-yil,"
#           f"{car['narh']}$")

# print(f"{cars[0]['model'].title()}"
#       f"{cars[0]['rang']}"
#       )
# 15-lug'at bilan ishlash:
#uy ish
# python = {'upper':'harif kota',
#         'title':'so\'z harifini kota qiladi',
#         'integer':'butunson',
#         'float':'o\'nlikson',
#         'del':'qiymat o\'chiradi',
#         'sorted':'alifbo ketmaketligida qo\'yadi',
#         'for':'bir amalni qayta-qayta bajarish tsikl',
#         }
# for key, value in sorted(python.items()):
#     print (f"{key.title()} -{value}")

# bozor = {'mac':1,'acer':11,'mac':3}
# for k in bozor.keys():
#  savat=['mac','acer','lenova','core i-9']
# for mac in bozor:
  # if mac in savat:
    # print(f"Bor {mac.title()} bor ekan oka😊")
# for buyum in savat:
  # if buyum not in bozor:
    # print(f"Bunday notbuklar  yo'q! {buyum.title()} uzur😉")
# mevalar = {
#      'olma':10000,
#      'banan':20000,
#      'uzum':300000,
#      'nok':40000,
# }
# print(mevalar.keys())
# for meva in mevalar.keys():
    # print(f"{meva.title()}")

# bozorlik=['banan','uzum','non','shaftoli']
# for meva in mevalar:
#   if meva in bozorlik:
#     print(f"mahsultlar bori {meva.title()} {mevalar[meva]}")
#     for buyum in bozorlik:
#       if buyum not in mevalar:
#         print(f"Iltimos do'konin gizga {buyum} olib keling")
# telefonlar = {
#      'ali': ' iphone',
#      'vali':' geleksi',
#      'olim':' mi 10 pro',
#      'orif':' noika 11/11'
# }
# for k, q in telefonlar.items():
#     print( f"{k.title()}ning telfoni{q}")

# talaba_0 = {
#     'ism':'Behruz',
#     'shahar':'toshkent',
#     'yosh':20
#     }

# print(talaba_0.items())


# 14-lug'at:
#uy ishi
# otam={'ism':' Said ','tyil':' 2000 ','shahar':' toshkent '}
# tyil=otam['tyil']
# shah=otam['shahar']
# print(f"Saidni Ismlari{otam['ism'].title()}{tyil} tug'ilg'ilganlar shaharlari{shah.title()}")
# tavomlar={
#   'ali':'osh',
#   'Said':' honim',
#   'ibo':'somsa'
# }
# taom=tavomlar['Said']
# print(f"Saidni sevimli tovomi{taom.title()}")


# python_izohli_lugati = {
#     'upper':"Hamma harifni kotta qiladi",
#     'integer':"Butun son",
#     'float':"O'nlik son",
#     'string':"Matn",
#     'list':"Ro'yxat",
#     'tuple':"O'zgarmas ro'yxat"}
# # print(python_izohli_lugati['tuple'])

# kalit = input("Kalit so'z kiriting:").lower()
# print(python_izohli_lugati.get(kalit,"Bunday so'z mavjud emas"))

# kalit = input("Kalit so'z kiriting:").lower()
# tarjima = python_izohli_lugati.get(kalit)
# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")


# not_7={
#    'mac':'3',
#    'ism':'Muhammad said',
#    'yosh':'15',
#    'yoqadi':'mac-3'
#    }
# del not_7['ism']
# print(not_7)
# bor=not_7.get('windows','Bunday qiymatmavjud emas' )
# print(bor)
# talaba_0 ={'ism':'sunatila','yoshi':'25','t_yil':'2000'}
# print(talaba_0['ism'])


# en_uz={'aple':'olma','banana':'banan','laptop':'notbuk'}
# print(en_uz['banana']+" yeb")
# print(en_uz['laptop']+" pythondan dars qilgigim kevoti!!!")
# print(en_uz['laptop']+" pythondan dars qilgigim kevoti!!!")

# car_0 ={'madel':'ferrari','rang':'qizil'}
# print(car_0['madel'])
# print(car_0['rang'])
#12-xatolar bilan ishlash

#11-dars:if/else/else shart operatori
#uy-ishi
#4


#3

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#   print(f"Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


#2
# blet = int(input('yoshingiz nechida?>>>'))
# if blet<=5 or blet>=60:
  #  print('narh=0')
# elif blet<=18:
  #  print('narh=8000')
# elif blet>=20:
  #  print('10000')
# else:
#  print('yoshingizni kiriting!')


#1
# juft_son = int(input("Juft sonlar kiriting:\n>>>"))
# if juft_son % 2:
#   print("Bu son juft emas.")
# else:
#   print("to'g'ri son")
# toq_son = int(input("Toqson kiriting: \n>>>"))
# if toq_son % 1:
#  print("Bu son toq mas.")

# else:
#   print("to'g'ri son")
# #and-operatori misoli
# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = 1
# salat = 1
# non = 1
# kompot = 0
# assorti = 1
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
# if choy:   # agar choy olsa
#  print("Mijoz choy oldi.")
#  narh = narh + 3000
# if salat:  # agar salat olsa
#  print("Mijoz salat oldi.")
#  narh = narh + 5000
#  if non:    # agar non olsa
  # print("Mijoz non oldi.")
#  narh = narh + 2000
# if kompot: # agar kompot olsa
  # print("Mijoz kompot oldi.")
    # narh = narh + 5000
# if assorti: # agar assorti olsa
    # print("Mijoz assorti oldi.")
    # narh = narh + 15000
#
# print(f"Jami {narh} so'm")
#or-operatori misoli
# kun = input('Bugun nima kun?>>>')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#   print('Bugundam olish kuni!')
# else:
#   print('Bugun ish kuni!')

# yosh = int(input("Yoshingiz nechida? \n>>>"))
# if yosh<=4:
#   narh = 0
# elif yosh<=12:
#   narh = 5000
# elif yosh<=18:
#   narh = 8000
# else:
#   narh = 1000
#   print(f"salom sizga kirish{narh}so\'m.")
#10-dars:if/else shart operatori:
# sallat =input("sallat yeysizmi? (ha/yo'q) \n>>>")
# if sallat.lower() == 'ha':
#   print("Sizga alaviya tavsiya qilaman.")
# elif sallat.lower() =='yo\'q':
#   print("Unda sizga ritsepidagi boshqa salatlarni tav siya qilaman.")
# else:
#   print("Iltimos, ha yoki yo'q deb javob bering.")

# yosh = input("Yoshingiz nechida? \n>>>")
# if int(yosh) <=18:
#   print("Kirish mumkin emas.")
# else:
#   print("Xush kelib siiz!")


# ism = input("Ismingiz nima? \n>>>")
# if ism.lower() != 'said':
    # print(f"Uzr, {ism.title()} biz Saidni kutyapmiz.")
# else:
    # print("Salom, Said!")



# 09-dars:for sikli data:09/12/2025

# dostlar =[]
# print("5 ta eng yaqin do'stingiz kimlar?")
# for n in range(5):
#   dostlar.append(input(f"{n+1} do'stingizning ismini kiriting: "))
#   print(dostlar)

# mehmonlar =['Said','Mirzoxit','Yusuf','Behzod','Ibrohim']
# for mehmon in mehmonlar:
#    print(f"Hurmatli {mehmon}, 20-dekabrda bo'lib o'tadiga to'yimga taklif qilaman.")
#    print(f" Hurmatli {mehmon},palonchinov lar oilasi.\n")

# mehmonlar =['Said','Mirzoxit','Yusuf','Behzod','Ibrohim']
# for mehmon in mehmonlar:
  # print("Salom", mehmon,)
  # print("Hayr",mehmon, )



# 08-dars: Ro'yxatlar bilan ishlash davom
# cars=['bmw', 'audi', 'toyota', 'hyundai', 'kia', 'chevrolet', 'ferrari', 'lamborghini', 'porsche', 'volkswagen', 'nissan', 'mazda', 'mercedes-benz']
# cars.sort()
# print(cars)
# cars.sort(reverse=True)
# print(cars)

# #07-dars: Ro'yxatlar bilan ishlash
# mevalar = ['olma', 'anor', 'banan', 'shaftoli', 'o\'rik']
# narxlar = (12000, 15000, 8000, 10000, 9000)
# narxlar=list(narxlar)
# narxlar.append(11000)
# print(narxlar)
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon mahsulot narxi:", arzon, "so'm")
# print("Eng qimmat mahsulot narxi:", qimmat, "so'm")
# print("Jami narxlar:", jami, "so'm")
# print(cars[0:3])
# mevalar.append('gilos')#bunda qiymat ohiriga qo'shiladi
# mevalar.insert(1,'nok')#bunda qiymat etgan qatorga qo'shiladi
# mevalar.insert(0, 'banan')  #bunda qiymat etgan qatorga qo'shiladi
# del mevalar[4]#bunda qiymat o'chiriladi
# mevalar.remove('shaftoli')#bunda qiymat o'chiriladi
# narxlar.remove(12000)#bunda qiymat o'chiriladi
# narxlar[0] =narxlar[0] + 20000#bunda qiymat o'zgartiriladi
# print(narxlar)
# print(mevalar)

# meva=mevalar.pop(0)
# print(meva)

# print(mevalar)


# t_yil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh = 2025 - t_yil
# print("Siz", yosh, "yoshda ekansiz.")
# ism= input("Ismingiz nima? ")
# print("Assalomu alaykum", ism,)
# ALL=(77+22)
# print("Hello, world!")
# a=5
# b=17
# c=a+b
#  print(c)
# print("Assalomu alaykum dunyo!", 3+3, "BILASANMI?")
# print(2+3)
# print(2**4)
# print(5/2)
# print(5//2)
# print(5%2)
# ism= "Muhammad"
# yosh = 15
# print(ism, "\n", yosh)
#Radiusi 5 ga teng bo'lgan aylananing uzunligi quyidagicha hisoblanadi
# print(2*5*3.14159)
# print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")

# radius = 5
# pi = 3.14159
# aylana_yuzi = pi * radius**2
# print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)
# ism = "Ali"
# print("salom "+ ism)