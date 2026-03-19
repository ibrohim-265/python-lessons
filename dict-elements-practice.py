# Amaliyot
# 1. 
python_dict = {
    'integer': "butun son",
    'float': "o'nlik son",
    'string': "matn",
    'boolean': "mantiqiy qiymat",
    'list': "ro'yxat",
    'tuple': "o'zgarmas ro'yxat",
    'input' : "foydalanuvchidan kiritgan ma'lumot",
    "print" : "ekran chiqarish funksiyasi",
    "if" : "shart operatori",
    "for" : "tsikl operatori",  
    "while" : "tsikl operatori"    
}
for key, value in sorted(python_dict.items()):
    print(f"{key.title()}: {value}")

# 2.
davlatlar = {
    "o'zbekiston": "toshkent",
    "rossiya": "moskva",
    "aqsh": "vashington",
    "italiya": "rim",
    "fransiya": "parij",
    "ispaniya": "madrid",
    "germaniya": "berlin",
    "braziliya": "brazilia",
    "hindiston": "dehli",
    "xitoy": "pekin"    
}
print("Davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(davlat.title())   
print("\nPoytaxtlar:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())    
# 3.
davlatlar = {
    'ozbekiston': 'toshkent',
    'rossiya': 'moskva',
    'aqsh': 'washington',
    'yaponiya': 'tokio',
    'brazilya': 'brazilya',
    'xitoy': 'pekin',
    'hindiston': 'dehli',
    'germaniya': 'berlin',
    'fransiya': 'parij',
    'italiya': 'rim',
    'ispanija': 'madrid',
    'turkiya': 'anqara',
    'koreya': 'seul',
    'avstraliya': 'kanberra',
    'kanada': 'ottawa',
    'mexika': 'mehiko',
    'misr': 'qohira',
    'saudiya arabistoni': 'ar-riyod',
    'indoneziya': 'jakarta',
    'pokiston': 'islamobod'
}

print("🌍 DUNYO DAVLATLARI VA POYTAXTLARI LUG'ATI")
print("=" * 50)
print(f"Jami {len(davlatlar)} ta davlat haqida ma'lumot mavjud\n")

print("📋 Lug'atdagi davlatlar:")
for davlat in sorted(davlatlar.keys()):
    print(f"  • {davlat.title()}")

print(f"\n🏛 Lug'atdagi poytaxtlar:")
for poytaxt in sorted(davlatlar.values()):
    print(f"  • {poytaxt.title()}")

print("\n" + "=" * 50)

while True:
    davlat = input("\nDavlat nomini kiriting (chiqish uchun 'exit' yozing): ").lower().strip()

    if davlat == 'exit':
        print("Dasturdan chiqildi. Xayr!")
        break

    if not davlat:
        print("❌ Davlat nomi bo'sh bo'lishi mumkin emas!")
        continue

    poytaxt = davlatlar.get(davlat)

    if poytaxt:
        print(f"✅ {davlat.title()}ning poytaxti: {poytaxt.title()}")
    else:
        print("❌ Bizda bunday ma'lumot yo'q")

    print("-" * 30)

    