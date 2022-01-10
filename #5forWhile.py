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

# Perulangan
'''

Di python, perulangan bisa dilakukan dengan dua cara atau metode, yaitu:

1. Menggunakan for
2. Menggunakan while

'''

# Perulangan Dengan Menggunakan For
'''

Perulangan dengan menggunakan for memiliki sintaks seperti berikut:

for var in sequence:
    body of for

var adalah variabel yang digunakan untuk penampung sementara nilai dari 
sequence pada saat terjadi perulangan. Sequence adalah tipe data berurut 
seperti string, list, dan tuple.

Perulangan terjadi sampai looping mencapai elemen atau anggota terakhir dari 
sequence. Bila loop sudah sampai ke elemen terakhir dari sequence, maka 
program akan keluar dari looping.

'''

# Program untuk menemukan jumlah bilangan dalam satu list

# List number
numbers = [7, 5, 9, 8, 4, 2, 6, 4, 1]

# variablel untuk menyimpan jumlah

sum = 0

# iterasi
for each in numbers:
    sum = sum + each

# Output: Jumlah semuanya: 46
print("Jumlah semuanya:", sum)

# Fungsi range()
'''

Fungsi range() dapat digunakan untuk menghasilkan deret bilangan. 
range(10) akan menghasilkan bilangan dari 0 sampai dengan 9 (10 bilangan).

Kita juga bisa menentukan batas bawah, batas atas, dan interval dengan format 
range(batas bawah, batas atas, interval).Bila interval dikosongkan, maka 
nilai default 1 yang akan digunakan.

Kita bisa menggunakan fungsi range() dalam perulangan menggunakan for untuk 
iterasi bilangan berurut. Hal ini dengan cara mengkombinasikan fungsi range() 
dengan fungsi len() . Fungsi len() berfungsi untuk mendapatkan panjang atau 
jumlah elemen suatu data sekuensial atau berurut.

'''

# Program untuk iterasi list menggunakan pengindeksan

mapel = ['matematika', 'fisika', 'kimia']

# iterasi list menggunakan indeks
for i in range(len(mapel)):
    print("Saya suka", mapel[i])

# Perulangan Menggunakan while
'''

Perulangan menggunakan while akan menjalankan blok pernyataan terus menerus 
selama kondisi bernilai benar.

Adapun sintaks dari perulangan menggunakan while adalah:

while expression:
    statement (s)

'''

# Perhatikan bahwa bila kondisi yang diuji bernilai salah, maka loop tidak akan pernah dieksekusi.
count = 0
while (count < 5):
    print('The count is:', count)
    count = count + 1
print('Good bye!')

# Infinite Loop
'''

Sebuah kondisi dimana loop selalu benar dan tidak pernah salah disebut loop 
tidak terbatas (infinite loop). Terkadang hal ini menjadi masalah. 
Tapi sering juga infinite loop berguna, misalnya untuk program client/server 
dimana server perlu menjaga komunikasi tetap hidup dan tidak terputus.

Kita perlu menekan CTRL+C untuk menghentikan program ketika mengalami looping
secara terus menerus tanpa henti.

'''

# Kendali Looping
'''

Looping umumnya akan berhenti bila kondisi sudah bernilai salah. Akan tetapi, 
seringkali kita perlu keluar dari looping di tengah jalan tergantung keperluan. 
Hal ini bisa kita lakukan dengan menggunakan kata kunci break dan continue.

Statement break memaksa program keluar dari blok looping di tengah jalan. 
Sedangkan statement continue menyebabkan program langsung melanjut ke 
step / interval berikutnya dan mengabaikan (skip) baris kode di bawahnya 
(yang satu blok). 

Jelasnya perhatikan contoh berikut:

'''

# contoh penggunaan statement break
for letter in "Programming":
    if letter == "g":
        break
    print("Huruf sekarang:", letter)
print("Good bye")

# while else
'''

Python mendukung penggunaan else sebagai pasangan dari while. 
Blok pernyataan else hanya akan dieksekusi bila kondisi while bernilai salah.

'''
count = 0
while (count < 5):
    print(count, "kurang dari 5")
    count = count + 1
else:
    print(count, "tidak kurang dari 5")

















