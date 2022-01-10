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

# String
'''

String adalah tipe data yang paling sering digunakan di Python. 
Kita bisa membuat string dengan meletakkan karakter di dalam tanda kutip. 
Tanda kutipnya bisa kutip tunggal maupun kutip ganda. 

Contohnya adalah sebagai berikut:


var1 = 'Hello Python'
var2 = 'Programming with Python'

'''

# Mengakses Nilai String

# Untuk mengakses nilai atau substring dari string, kita menggunakan indeks dalam tanda [ ].
var1 = 'Hello Python!' 
var2 = "I love Python" 
print("var1[0]", var1[0]) 
print("var2[2:6]:",var2[2:6])

# Mengupdate String
'''

String adalah tipe data immutable, artinya tidak bisa diubah. 
Untuk mengupdate string, kita perlu memberikan nilai variabel string lama 
ke string yang baru. Nilai yang baru adalah nilai string lama yang sudah diupdate.

'''
var1 = 'Hello Python!' 
var2 = var1[:6] 
print("String Update: - ", var1[:6] + 'World') 

# Menggabung String
'''

Kita bisa menggabungkan dua atau lebih string menjadi satu dengan menggunakan 
operator +. Selain itu kita juga bisa melipatgandakan string 
menggunakan operator *.

'''
str1 = 'Hello' 
str2 = 'Python' 

# menggunakan + 
print('str1 + str2 =', str1 + str2) 

# menggunakan * 
print('str1 * 3 =', str1 * 3)

## Menguji Keanggotaan Karakter Dalam String
'''

Kita bisa menguji apakah sebuah substring ada terdapat di dalam suatu string atau tidak. Caranya adalah dengan menggunakan kata kunci in

'a' in 'Programming'
True
'at' not in 'battle'
False

'''

# Mengetahui Panjang String
'''

Untuk mengetahui panjang dari string, kita bisa menggunakan fungsi len().

>>> string = 'I love Python'
>>> len(string)
18

'''


# Karakter Escape
'''

Kalau kita hendak mencetak string: He said, "What's there?" 
kita tidak bisa menggunakan tanda kutip tunggal maupun ganda. 
Bila kita melakukannya, akan muncul pesan error SyntaxError karena teks 
berisi kutip tunggal dan ganda.

Karakter escape dimulai dengan tanda backslash \. Interpreter akan 
menerjemahkannya dengan cara berbeda dengan string biasa. 

Solusi untuk error di atas adalah sebagai berikut:

'''
# menggunakan kutip tiga
print('''He said, "What's there?"''')

# menggunakan karakter escape untuk tanda kutip tunggal
print('He said, "What\'s there?"')

# menggunakan karakter escape untuk tanda kutip ganda
print("He said, \"What's there?\"")

'''

Berikut adalah daftar karakter escape yang didukung oleh Python.

Karakter Escape	Deskripsi
\newline	Backslash dan newline diabaikan
\\	Backslash
\’	Kutip tunggal
\”	Kutip ganda
\a	ASCII bel
\b	ASCII backscape
\f	ASCII formfeed
\n	ASCII linefeed
\r	ASCII carriage return
\t	ASCII tab horizontal
\v	ASCII tab horizontal
\ooo	karakter dengan nilai oktal oo
\xHH	karakter dengan nilai heksadesimal HH

'''
# menggunakan posisi default 
default_order = "{}, {} dan {}".format("Budi", "Galih","Ratna") 
print('\n--- Urutan default ---') 
print(default_order) 

# menggunakan argument posisi 
positional_order = "{1}, {0} dan {2}".format("Budi", "Galih","Ratna") 
print('\n--- Urutan berdasarkan posisi ---') 
print(positional_order) 

# menggunakan argumen kata kunci 
keyword_order = "{r}, {b} dan {g}".format("Budi", "Galih","Ratna") 
print('\n--- Urutan berdasarkan kata kunci ---') 
print(keyword_order) 


# Format Cara Lama Dengan %
'''

Kita bisa menggunakan operator % untuk melakukan format string.

nama = 'Budi'
print('Nama saya %s' %s)

Nama saya Budi
x = 12.3456789
print('Nilai x = %3.2f' %x)

Nilai x = 12.35
print('Nilai x = %3.4f' %x)

Nilai x = 12.3456

'''

# Metode / Fungsi Bawaan String
'''

String memiliki banyak fungsi bawaan. format() yang kita bahas di atas hanya salah satu darinya. 
Fungsi atau metode lainnya yang sering dipakai adalah join(), lower(), upper(), split(), startswith(), 
endswith(), replace() dan lain sebagainya.

>>> "KingEagleTech".lower()
'kingeagletech'
>>> "kingeagletech".upper()
'KINGEAGLETECH'
>>> "I love programming in Python".split()
['I', 'love', 'programming', 'in', 'Python']
>>> "I love Python".startswith("I")
True
>>> "Saya belajar Python".endswith("on")
True
>>> ' - '.join(['I', 'love', 'you'])
I - love - you
>>> "Belajar Java di KingEagleTech".replace('Java', 'Python')
'Belajar Python di Pythonindo

Selain itu masih banyak metode lain yang dimiliki python. Kita akan bahas di artikel lain.

'''