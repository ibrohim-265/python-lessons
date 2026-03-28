#  # Function - ma'lum vazifani bajaruchi kod bloklari
#  # Funksiya yaratish uchun def kalit so'zidan foydalanamiz
# # print("Hello, World!")
#  # Funksiyani e'lon qilish(declaration)
# # def salom_ber():
# #     print("Salom, Dunyo!")

#  # Funksiyani chaqirish (call)
# # salom_ber() # Natija: Salom, Dunyo!

#  # Funksiya parametrlar , argumentlar 
# # def salom_ber(ism):
# #     print(f"Salom, {ism}!")

# # salom_ber("Ali") 
# # salom_ber("Vali")
# # salom_ber("Olim")   
# # salom_ber(" Gulbahor ammam")

# # def yigindi(a, b):
# #     print(a + b)

# # yigindi(7, 8) # Natija: 15
# # yigindi(10, 20)  # Natija: 30

# # def calculate_age(birth_year=1995, name= "Sobirjon"):
# #     age = 2026 - birth_year
# #     print(f"{name}ning yoshi: {age}")

# # calculate_age(2005, "Sobirjon")    
# # calculate_age(2007, "Sulaymon")
# #calculate_age()

# # def yosh_hisobla(joriy_yil, joriy_yil=2020): # joriy yil uchun st.qiymat 2020
# #     print(f"siz {joriy_yil-tugilgan_yil} yoshdasiz")

# # yosh_hisobla(1995, 2020)

#  # 1. amaliyot
# def toliq_ism(name):
#     print(f"Foydalanuvchi ismi: {name.title()}")

# toliq_ism('Sulaymon Rustamov')
# tugilgan_yil = "18.04.2007"
# yosh = 20
# oyda = "ikkinchi farzand"

# if yosh > 18:
#     foydalanuvchi_malumoti = f"Foydalanuvchi {oyda}, yosh {yosh} da"
# else:
#     foydalanuvchi_malumoti = "Foydalanuvchi hali kattalar yoshiga yetmagan"

# print(foydalanuvchi_malumoti)

# # 4. amaliyot
# def solishtirish(a, b):
#     if a > b:
#         print(f"{a} katta {b} dan")
#     elif a < b:
#         print(f"{a} kichik {b} dan")
#     else:
#         print(f"{a} va {b} teng" )

# solishtirish(10, 20)
# solishtirish(3, 7)
# solishtirish(4, 4)
# # 2.
# def kvadrat_va_kub(son):
#     kvadrat = son ** 2
#     kub = son ** 3
#     print(f"{son} sonining kvadrati: {kvadrat}, kubi: {kub}")
# kvadrat_va_kub(3)

# # 3.
# def juft_yoki_toq(son):
#     if son % 2 == 0:
#         print(f"{son} juft son")
#     else:
#         print(f"{son} toq son")

# juft_yoki_toq(4)
# juft_yoki_toq(7)

# # 5. amaliyot
# def kattaroq_son(a, b):
#     if a > b:
#         print(f"{a} katta {b} dan")
#     elif a < b:
#         print(f"{b} katta {a} dan")
#     else:
#         print(f"{a} va {b} teng")   
# kattaroq_son(15, 10)    
# kattaroq_son(5, 20)
# kattaroq_son(7, 7)

#7.
def bolinish(son)
    for i in range(2, 11)
    if son % i == 0:
        print(f"{son} {i} ga qoldiqsiz bolinadi")

a = int(input("Xoxlagan son kiriting: "))
bolinish(a)        