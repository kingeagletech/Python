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

# Variable & Tipe Data Python

# Memberi Nilai Variabel
panjang = 100 # tipe data integer
lebar = 21.5 # tipe data float
nama = "Umar" # tipe string
print(panjang)
print(lebar)
print(nama)

'''

Catatan: Istilah menugaskan, menyimpan, dan memberi nilai ke variabel adalah
sama. Secara teknis, sebenarnya variabel adalah nama yang diberikan untuk
menunjuk ke lokasi memori yang menyimpan suatu objek atau data.

'''

# Multi penugasan

# Kita bisa memberi nilai ke beberapa variabel secara bersamaan seperti berikut.
x = y = z = 3

'''
Pada contoh di atas, kita menciptakan sebuah objek integer, yaitu 
bilangan 3, dan kemudian kita menugaskan ketiga variabel untuk menunjuk ke 
lokasi yang sama yang berisi 3.
'''

a, b, c = 1, 3.4, "Umar" # Contoh lainnya

# Tipe Data Python
'''

Python memiliki enam tipe data standar atau paling sering digunakan, yaitu:

1. Bilangan (Number)
2. String
3. List
4. Tuple
5 Set
6. Dictionary

'''

# Bilangan (Number)
''' Kita bisa menggunakan fungsi type() untuk mengetahui tipe data suatu objek di python. '''
x = 5 
print(x, "tipenya adalah ", type(x))
x = 2.0
print(x, "tipenya adalah ", type(x))
x = 1+2j
print(x, "tipenya adalah ",type(x))

# String
''' String adalah tipe data yang anggotanya berurut dan memiliki indeks.
Indeks dimulai dari angka 0 bila dimulai dari depan dan -1 bila diindeks dari 
belakang dan di apit oleh tanda kutip. '''

text = "King Eagle Tech"

print(text)      # print string lengkap
print(text[0])   # print karakter pertama
print(text[-1])  # print karakter terakhir
print(text[4:7]) # print dari indeks 4 - 6
print(text[:4])  # print dari indeks 0 - 3

'''

Maka Hasilnya akan mengeluarkan nilai seperti berikut;

King Eagle Tech
K
h
 Ea
King

'''

# List
'''
List adalah tipe data yang berisi item yang berurut.
List bisa berisi anggota dengan tipe yang sama maupun berbeda. 
Untuk mendeklarasikan list, digunakan tanda kurung [ ] dan masing-masing 
anggotanya dipisahkan oleh tanda koma.
'''

lst = [1, 'dua', 3.0]
'''
Untuk mengakses item dari list caranya adalah dengan memanggil nama list
diikuti indeks dari item yang bersangkutan, yaitu dengan format 
namalist[index]
'''

a = [5,10,15,20,25,30,35,40]

# a[2] = 15
print("a[2] = ", a[2])

# a[0:3] = [5, 10, 15]
print("a[0:3] = ", a[0:3])

# a[5:] = [30, 35, 40]
print("a[5:] = ", a[5:]) 

# Tuple
'''
Tuple adalah jenis data lain yang mirip dengan list. Perbedaannya dengan
list adalah anggotanya tidak bisa diubah (immutable). List bersifat mutable, 
sedangkan tuple bersifat immutable. Sekali tuple dibuat, maka isinya tidak 
bisa dimodifikasi lagi.

Tuple dideklarasikan dengan menggunakan tanda kurung ( ). dan anggotanya 
dipisahkan oleh tanda koma. Tuple berguna untuk data yang dimaksudkan tidak 
diubah isinya. Misalnya tuple komposisi warna untuk putih adalah (255,255,255).

Seperti halnya list, kita bisa mengakses anggota tuple dengan menggunakan indeksnya.
'''
white = (255,255, 255)
red = (255,0,0)
print(white)
print(red[0])
print(red[1])

# akan menghasilkan error
# tuple bersifat immutable
red[0] = 128

# Set
'''
Set dibuat dengan meletakkan anggota – anggotanya di dalam tanda kurung 
kurawal { }, dipisahkan menggunakan tanda koma. Kita juga bisa membuat set 
dari list dengan memasukkan list ke dalam fungsi set().

Set bisa berisi data campuran, baik integer, float, string, dan lain sebagainya.
Akan tetapi set tidak bisa berisi list, set, dan dictionary.
'''
# set integer 
my_set = {1,2,3} 
print(my_set) 

# set dengan menggunakan fungsi set() 
my_set = set([1,2,3]) 
print(my_set) 

# set data campuran 
my_set = {1, 2.0, "Python", (3,4,5)} 
print(my_set) 

# bila kita mengisi duplikasi, set akan menghilangkan salah satu 
# output: {1,2,3} 
my_set = {1,2,2,3,3,3} 
print(my_set) 

# set tidak bisa berisi anggota list 
# contoh berikut akan muncul error TypeError 
my_set = {1,2,[3,4,5]} 

# Dictionary
'''
Dictionary adalah tipe data yang tiap anggotanya terdiri dari pasangan kunci-nilai (key-value).

Dictionary dideklarasikan dengan menggunakan tanda kurung kurawal { }, dimana 
anggotanya memiliki bentuk kunci:nilai atau key:value dan tiap anggota dipisah 
tanda koma. Kunci dan nilainya bisa memiliki tipe sembarang.

Untuk mengakses nilai dari anggota dictionary, kita menggunakan key-nya.
'''
d = {
    1:'satu', 
    2:'dua', 
    'tiga':3
    
}
print(type(d))
print("d[1] = ", d[1])
print("d['tiga'] = ", d['tiga'])
# Error
print("d[3] = ", d[3])

'''

Beberapa Catatan …

> Tipe data sering disebut objek. Pada dasarnya semua hal di python adalah objek.
Ada tipe data lain yang umumnya dimiliki oleh bahasa Python, yaitu tipe None.

> Tipe None adalah sebuah tipe data spesial yang menunjukkan bahwa nilai/data 
suatu variabel itu belum/tidak ada (bukan nol, tapi tidak ada). 
Pada bahasa pemrograman lain seperti C, atau PHP, tipe data ini disebut null.

> Tipe data string, tuple, dan list masuk ke dalam tipe data yang disebut tipe 
data berurut / ordered atau sekuensial / sequence. Tipe data dictionary disebut 
data tidak berurut / unordered.

'''