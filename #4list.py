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

# list
'''

Membuat List

List adalah tipe data yang berisi satu atau beberapa nilai di dalamnya. 
Nilai – nilai ini sering juga disebut item, elemen, atau anggota list. 
List dibuat dengan menempatkan  semua item di dalam tanda kurung [ ], 
dipisahkan oleh tanda koma. Anggota list bisa berisi satu tipe data, atau campuran.


# list kosong
my_list = []

# list berisi integer
my_list = [1,2,3,4,5]

# list berisi tipe campuran
my_list = [1, 3.5, "Hello"]

List juga bisa berisi list lain. Ini disebut list bersarang

# list bersarang
my_list = ["hello", [2,4,6], ['a','b']]

'''

# Mengakses Anggota List
'''

Kita bisa mengakses anggota list dengan menggunakan indeksnya dengan format 
namalist[indeks]. Indeks list dimulai dari 0. List yang memiliki 5 anggota 
akan memiliki indeks mulai dari 0 s/d 4.

'''
my_list = ["I", "love","python","programming",2017] 
# output: I 
my_list[0] 

#output: python 
my_list[2]
 
# list dalam list 
your_list = ["hello", [1,2,3], "python"] 

# output 1 
print(your_list[1][0]) 

# output 3 
print(your_list[1][2]) 

# IndexError 
my_list[6]

# List Dengan Indeks Negatif
'''

Python mendukung indeks negatif, yaitu urutan dimulai dari anggota terakhir. 
Indeks anggota paling belakang adalah -1, kemudian -2, dan seterusnya.

'''
my_list = ['p','y','t','h','o','n'] 

# output: n 
my_list[-1] 

# output: h 
my_list[-3] 

# Slicing [Memotong List]
'''

Kita bisa mengakses anggota list dari range tertentu dengan menggunakan operator slicing titik dua ( : ).

Slicing akan lebih mudah bila kita memahami indeks dengan baik.

'''
my_list = ['p','y','t','h','o','n','i','n','d','o'] 

# anggota list dari 3 s/d 5 (dari h s/d n) 
print(my_list[3:6]) 

# anggota list dari 4 s/d yang terakhir 
print(my_list[4:]) 

# anggota list dari 0 s/d 4 
print(my_list[:5]) 

# indeks dari belakang dari -1 s/d -4 
print(my_list[-1:-5]) 

# Mengubah Anggota List
'''

List adalah tipe data yang bersifat mutable, artinya anggotanya bisa diubah. 
Ini berbeda dengan string dan tuple yang bersifat immutable.

'''
# misal ada nilai yang salah 
ganjil = [1,3,4,7,9] 

# ubah item ke 3 (indeks ke 2) 
ganjil[2] = 5 print(ganjil) 

# mengubah sekali banyak 
ganjil[2:5] = [11,13,15] 
print(ganjil) 

# Metode List
'''

List memiliki banyak metode untuk operasi seperti menambahkan anggota, 
menghapus, menyisipkan, menyortir, dan lain sebagainya. Mereka bisa diakses 
menggunakan format list.metode().

'''

# Menambahkan Anggota List
'''

Fungsi append() berguna untuk menambahkan anggota ke dalam list. Selain itu, ada metode extend() untuk menambahkan anggota list ke dalam list.

>>> ganjil = [1,3,5,7]

ganjil.append(9)
print(ganjil)
[1,3,5,7,9]

ganjil.extend([11,13,15])
print(ganjil)
[1,3,5,7,9,11,13,15]
Kita juga bisa menggunakan operator + untuk menggabungkan dua list, dan operator * untuk melipatgandakan list.

genap = [2, 4, 6]
print(genap + [8, 10, 12])
[2, 4, 6, 8, 10, 12]

print(['p','y'] * 2)
['p','y','p','y]

'''

# Menyisipkan Anggota List
'''

Fungsi insert() berfungsi untuk menyisipkan anggota list pada indeks tertentu.

ganjil = [5,7,11,13,15]

# kita akan menyisipkan 9 setelah angka 7
ganjil.insert(2,9)
print(ganjil)
[5,7,9,11,13,15]

'''

# Menghapus Anggota List
'''

Kita bisa menggunakan metode remove(), pop(), atau kata kunci del 
untuk menghapus anggota list. Selain itu kita bisa menggunakan clear() 
untuk mengosongkan list.

Fungsi pop() selain menghapus anggota list, juga mengembalikan nilai 
indeks anggota tersebut. Hal ini berguna bila kita ingin memanfaatkan indeks 
dari anggota yang terhapus untuk digunakan kemudian.

'''
my_list = ['p', 'y', 't', 'h', 'o', 'n'] 
my_list.remove('p') 

# output ['y', 't', 'h', 'o', 'n'] 
print(my_list) 

my_list.remove('n') 
# remove hanya menghapus elemen pertama yang dijumpai 
# output: ['p', 'y', 't', 'h', 'o']

# Output 'y'
print(my_list.pop(1))

del my_list[2]
print(my_list)

my_list.clear()
# Output []
print(my_list)

# Mengurutkan Anggota List
'''

Pada saat kita perlu mengurutkan atau menyortir anggota list, kita bisa menggunakan metode sort(). Untuk membalik dengan urutan sebaliknya bisa dengan menggunakan argumen reverse=True.

alfabet = ['a','b','d','f','e','c','h','g','j','i']
alfabet.sort()
print(alfabet)
['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

alfabet.sort(reverse=True)
print(alfabet)
['j', 'i', 'h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']

'''

# Membalik Urutan List
'''
Selain mengurutkan, kita juga bisa membalikkan urutan list dengan menggunakan metode reverse().

alfabet = ['a','c','d','e','b']
alfabet.reverse()
print(alfabet)

'''









