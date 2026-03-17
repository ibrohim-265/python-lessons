# Dictionary elementlari bilan ishlash
phone = {
    'brand': "Iphone",
    'model': "iPhone 17 Pro Max",
    'year': 2025,
    'color': "Silver",
    'price': 1500
}
# 1. get metodi -kalit orqali qiymatni olish
print(phone.get('model')) # iPhone 17 Pro Max
print(phone.get('price', "Narx topilmadi")) # 1500
print(phone.get('battery')) # None (kalit mavjud emas)
print(phone.get('battery', "Kalit topilmadi")) # Kalit topilmadi

# 2. items() metodi - lug'at  elementlarini (kalit, qiymat) juftlari ko'rinishida qaytaradi
print(phone.items()) # dict_items([('brand', 'Iphone'), ('model', 'iPhone 17 Pro Max'), ('year', 2025), ('color', 'Silver'), ('price', 1500)])
for key, value in phone.items():
    print(f"{key}: {value}")     
telefonlar = {
    'ali': "Iphone X",
    'vali': "galaxy s9",
    'olim': "mi 10 pro",
    'orif': "nokia 3310"
}
for k,q in telefonlar.items():
    print(f"{k.title()}ning telefoni {q}")

# 3.keys() metodi - lug'atdagi barcha kalitlarni qaytaradi  
print(phone.keys()) # dict_keys(['brand', 'model', 'year', 'color', 'price'])
print(telefonlar.keys()) # dict_keys(['ali', 'vali', 'olim', 'orif'])

mahsulotlar = {
    'olma': 10000,
    'anor': 20000,
    'uzum': 40000,
    'anjir': 25000,
    'shaftoli': 30000
}
print('Do\'kondagi mahsulotlar:')
for mahsulot in mahsulotlar.keys():
    print(mahsulot.title())

# 4. in operatori
# 1. listda in operatori element mavjutligini tekshiradi
fruist = ['olma', 'anor', 'uzum', 'anjir', 'shaftoli']
print('olma' in fruist) # True
print('tarvuz' in fruist) # False

fruit = input("Qaysi meva yoqadi? ")
if fruit in fruist:
    print(f"{fruit.title()} do'konimizda bor")
else:
    print(f"{fruit.title()} do'konimizda yo'q")

bozorlik = ['anor','uzum','non','baliq']
for mahsulot in mahsulotlar:
    print(mahsulot) # lug'atning kalitlari bo'ladi    
# mahsulotlar - lug'at, bozorlik - ro'yxat, mahsulot - lug'atning  kaliti
for mahsulot in mahsulotlar:
    if mahsulot in bozorlik:
        print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")