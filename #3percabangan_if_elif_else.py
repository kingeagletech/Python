'''

Welcome to King Eagle Technology.
King Eagle Tech is one of the Website and Mobile App based Online & Offline
course platform, which focuses on our Learning & Teaching as Instructors
to our potential users.

+++++++++++++++++++++++++++++++++++++++++++++++++++
+    Website: https://kingeagle.tech/             +
+    Github: https://github.com/kingeagle/        +
+    Instagram: https://instagram.com/kingeagle/  +
+    Twitter: https://twitter.com/kingeagle/      +
+++++++++++++++++++++++++++++++++++++++++++++++++++

'''

# PERCABANGAN IF | IF ... ELSE | IF ELIF ELSE

# Pernyataan IF
'''

Pernyataan if menguji satu buah kondisi. Bila hasilnya benar maka pernyataan 
di dalam blok if tersebut dieksekusi. Bila salah, maka pernyataan tidak 
dieksekusi. 

Sintaksnya adalah seperti berikut:

if tes kondisi:
   blok pernyataan if
   
'''

# Bila bilangan positif, tampilkan pesan

angka = 5
if angka > 0:
    print(angka, "adalah bilangan positif.")

angka = -1
# yang berikut akan bernilai False sehingga tidak dieksekusi
if angka > 0:
    print(angka, "adalah bilangan positif.")
    
# Pernyataan IF .... ELSE
'''

Pernyataan if…else menguji 2 kondisi. Kondisi pertama kalau benar, dan kondisi 
kedua kalau salah. 

Sintaksnya adalah seperti berikut:

if tes kondisi:
    blok pernyataan if
else:
    blok pernyataan else

'''

# Program menguji apakah sebuah bilangan positif atau negatif
# dan menampilkan pesan ke monitor

bilangan = 5

# coba juga mengubah bilangan menjadi bilangan = -1
# dan perhatikan hasilnya

if bilangan >= 0:
    print("Positif atau Nol")
else:
    print("Bilangan negatif")
    
# Pernyataan IF ELIF ELSE
'''

Pernyataan if…elif…else digunakan untuk menguji lebih dari 2 kondisi. 
Bila kondisi pada if benar, maka pernyataan di dalamnya yang dieksekusi. 
Bila salah, maka masuk ke pengujian kondisi elif. Terakhir bila tidak ada 
if atau elif yang benar, maka yang dijalankan adalah yang di blok else. 

Sintaksnya adalah seperti berikut:

if tes kondisi:
    blok pernyataan if
elif tes kondisi:
    blok pernyataan elif
else:
    blok pernyataan else

'''

# Di sini kita menguji apakah sebuah bilangan
# adalah bilangan positif, nol, atau negatif
# dan menampilkan hasilnya ke layar

bilangan = 5.5

# Coba juga mengganti bilangan jadi
# bilangan = 0
# bilangan = -5.5

if bilangan > 0:
    print("Bilangan positif")
elif bilangan == 0:
    print("Nol")
else:
    print("Bilangan negatif")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    