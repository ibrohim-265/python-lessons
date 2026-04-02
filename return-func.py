#QIYMAT QAYTARUVCHI FUNKSIYA
# def add_1(a, b):
#     print(a + b)

# add_1(4, 5)

# def add_2(a, b):
#     return a + b

# print(add_2(3, 4))
# value = add_2(5,8)
# print(value)

# from unittest import result


# def toliq_ism_yasa(ism, familiy):
#    """Toliq isma qaytaruvchi funksiy"""
#    toliq_ism = f"{ism} {familiy}"
#    return toliq_ism # qiymat qaytarish uchun return operatorini ishlattamiz

# # print(toliq_ism)
# """NemeError: neme 'toliq_ism' is not defined- toliq_ism o'zgaruvchisi funksiyaning ichida yaratilgan va faqat funksiya ichida mavjud"""

# print("a" * 3) # a harfini 3  marta takrorlaydi => "aaa"
# print("abc" * 5) # abc matnini 5 marta takrorlaydi => "abcabcabcabcabc"
# # print("abc" + 2) # TypeError: can only concatenate str (not "int") to str - string va integer turdagi qiymatlarni qo'shish mumkin emas, stringни integerga yoki integerni stringga o'zgartirish kerak
# print("abc" / 5)
 
# def is_even(number):
#       if number % 2 == 0:
#           return "Juft " 
#       else:
#             return "Toq"

# print(is_even(4)) # Juft      
# result = is_even(7) 
# print(result) # Toq
# print(is_even()) # Juft

# ternary operator yordamida yuqoridagi if/else constructionni qisqartirish mumkin
# syntax:

# vowels = ["a", "o", "i", "u", "e"]
# def count_vowels(text):
#      count = 0
#      for char in text:
#           if char in vowels:
#                 count += 1
#      return count
# input_text = "Salom, dunyo!"
# vowel_count = count_vowels(input_text)


# # string boyicha for loop ishlatish
# # text = "hello"
# # for char in text:
# #     print(char)