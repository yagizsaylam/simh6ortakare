

sayi = 2596
m = 10

print("Ortak Kare Yöntemi ile üretilen sayılar:")
for i in range(m):
    kare = sayi ** 2
    kare_str = str(kare).zfill(8)

    ortasayi = int(kare_str[2:6])
    print(f"{i+1}. sayı: {ortasayi}")
    sayi = ortasayi
