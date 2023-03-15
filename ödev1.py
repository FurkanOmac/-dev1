Ogrenciler = ["Furkan Omaç","Emre Vurmaz","Onur Kiliç","Emre Demir","Yusuf Kaya"]


# Öğrenci listeleme 

for i in range(len(Ogrenciler)): 
    print(Ogrenciler[i])



# Öğrenci ekleme

Ogrenci_ekleme = input("Öğrenci adi ve soyadini giriniz:")
Ogrenciler.append(Ogrenci_ekleme)
print("Öğrenci listeye eklendi.")
print(Ogrenciler)



# Öğrenci silme

Ogrenci_silme = input("Silmek istediğiniz öğrenci adi ve soyadini giriniz:")
for i in range(len(Ogrenciler)):
    if(Ogrenciler[i] == Ogrenci_silme):
        Ogrenciler.pop(i)
        print("Öğrenci silindi.")
        break 
print(Ogrenciler)

for i in range(len(Ogrenciler)):
    print(Ogrenciler[i])



# Öğrenci numarası öğrenme

Ogrenci = input("Numarasini öğrenmek istediğiniz öğrencinin adini ve soyadini giriniz:")
for i in range(len(Ogrenciler)):
    if(Ogrenci == Ogrenciler[i]):
        print("Öğrencinin numarasi:" + str(i))



# Birden fazla öğrenciyi silme 

sayiadeti = input("Kaç öğrenci silmek istersiniz*")
i=0 
while i<int(sayiadeti):
    Ogrenciler.remove(Ogrenciler[i])
    i+=1 
print(Ogrenciler)



# Birden fazla öğrenci ekleme

sayiadeti= input("Kaç öğrenci eklemek istersiniz?")
i=0 
while i<int(sayiadeti):
    Ogrenciler_ekle = input("Arada boşluk birakarak ad ve soyad giriniz:")
    Ogrenciler.append(Ogrenciler_ekle)
    i+=1
print(Ogrenciler)