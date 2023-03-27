#!/usr/bin/env python
# coding: utf-8

# In[14]:


print("Selamat datang di kalkulator luas/volume!")
print("Pilih opsi yang anda inginkkan")
print("1. Menghitung luas 2 dimensi")
print("2. Menghitung volume 3 dimensi")

pilihan = input("Masukan pilihan Anda (1 atau 2):")

if pilihan == "1":
    print("Pilihan bentuk 2 dimensi yang ingin dihitung:")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Lingkaran")
    print("5. Jajar genjang")
    print("6. Trapesium")
    
    bentuk = input("Masukan pilhan Anda (1-6):")
    
    if bentuk == "1":
        sisi = float(input("Masukan panjang sisi: "))
        luas = sisi * sisi
        print("Luas persegi adalah:", luas)
        
    elif bentuk == "2":
        panjang = float(input("Masukan panjang: "))
        lebar = float(input("Masukan lebar: "))
        luas = panjang * lebar
        print("Luas persegi panjang adalah:", luas)
    
    elif bentuk == "3":
        alas = float(input("Masukan panjang alas: "))
        tinggi = float(input("Masukan tinggi: "))
        luas = 0.5 * alas * tinggi
        
    elif bentuk == "4":
        jari_jari = float(input("Masukan jari-jari: "))
        luas = 3.14 * jari_jari**2
        print("Luas lingkaran adalah: ", luas)
    
    elif bentuk == "5":
        alas = float(input("Masukan alas: "))
        tinggi = float(input("Masukan tinggi: "))
        luas = alat * tinggi
        print("Luas jajar genjang adalah:", luas)
    
    elif bentuk == "6":
        sisi_a = float(input("Masukan sisi A: "))
        sisi_b = float(input("Masukan sisi B: "))
        tinggi = float(input("Masukan tinggi: "))
        luas = 0.5 * (sisi_a + sisi_b) * tinggi
        print ("Luas jajar genjang adalah: ", luas)
    
    else:
        print("Maaf, bentuk tidak dikenal.")
        
elif pilihan == "2":
    print("Pilihan bentuk 3 dimensi yang ingin dihitung:")
    print("1. Kubus")
    print("2. Balok")
    print("3. Tabung")
    print("4. Kerucut")
    print("5. Limas")
    print("6. Prisma")
    
    bentuk = input("Masukan pilhan anda (1-6):")

    if bentuk == "1":
        sisi = float(input("Masukan panjang sisi: "))
        volume = sisi**3
        print("Volume kubus adalah: ", volume)
    elif bentuk == "2":
        panjang =float(input("Masukan panjang balok: "))
        lebar =float(input("Masukan lebar balok: "))
        tinggi =float(input("Masukan tinggi balok: "))
        volume = panjang * lebar * tinggi
        print("Volume balok dengan panjang", panjang, ",lebar", lebar, ", dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "3":
        jari_jari =float(input("Masukan jari-jari tabung: "))
        tinggi = float(input("Masukan tinggi tabung: "))
        volume = math.pi * jari_jari * tinggi
        print("Volume tabung dengan jari-jari", jari-jari, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "4":
        jari_jari =float(input("Masukan jari-jari kerucut: "))
        tinggi =float(input("Masukan tinggi kerucut: "))
        volume = 1/3 * math.pi * jari_jari **2 * tinggi
        print("Volume kerucut dengan jari-jari", jari-jari, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "5":
        alas =float(input("Masukan alas limas: "))
        tinggi =float(input("Masukan tinggi limas: "))
        volume = 1/3 * alas * tinggi
        print("Volume limas dengan luas alas", alas, "dan tinggi", tinggi, "adalah", volume)
    elif bentuk == "6":
        alas =float(input("Masukan alas segitiga prisma: "))
        tinggi =float(input("Masukan tinggi segita prisma: "))
        tinggi_prisma =float(input("Masukan tinggi prisma: "))
        volume = 1/2 * alas * tinggi * tinggi_prisma
        print("Volume prisma segita dengan alas", alas, ", tinggi", ", dan tinggi prisma", tinggi_prisma, "adalah", volume)
else:
    print("Bentuk tidak dikenali.")


# In[ ]:




