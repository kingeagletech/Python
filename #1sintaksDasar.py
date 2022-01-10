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

# Sintaks Dasar Python

# Statement Multibaris
a = panjang1 + panjang2 + \
    panjang3 + \
    panjang4
    
# Statement yang ada di dalam tanda kurung [ ], { }, dan ( ) tidak memerlukan tanda \. 
# Contohnya:

nama_bulan = ['Januari', 'Maret', 'Juni', 'September']

# Baris dan Indentasi
if nilai <= 5:
   print("Nilai merah")
   print("Tidak lulus")
else:
   print("Nilai biru")
   print("Lulus")
   
# Bila indentasi dalam satu grup kode tidak sama, python akan menampilkan sintaks error.
if True:
 print ("Jawab")
  print ("Benar")

else:
 print ("Jawab")
 print ("Salah")

# Tanda Kutip di Python
# Python menggunakan tanda kutip tunggal (‘), ganda (“), maupun triple (”’ atau “””) untuk menandai string, sepanjang stringnya diawali oleh tanda kutip yang sama di awal dan akhir string.

# Tanda kutip tiga digunakan untuk string multibaris. Ketiga contoh berikut, semuanya adalah benar,

kata = 'kata'
kalimat = "Ini adalah kalimat"
paragraf = """Ini adalah paragraf. Paragraf
      terdiri dari beberapa baris."""

# Komentar di Python
# Tanda pagar ( # ) digunakan untuk menandai komentar di python. Komentar tidak akan diproses oleh interpreter Python. Komentar hanya berguna untuk programmer untuk memudahkan memahami maksud dari kode.

# Komentar pertama
print("Hello World!") # Komentar kedua

#Kode di atas akan menghasilan keluaran:
# Hello World!


# Python tidak memiliki fitur komentar multibaris. Kita harus mengomentari satu persatu baris seperti berikut:

# Ini komentar
# Ini juga adalah komentar
# Ini juga masih komentar

# Bonus komentar di Python
# Komentar pertama bisa menggunakan tanda kutip single ataupun duoble ('' & "")
'''
    Dengan menggunakan komentar tanda kutip single / duoble 3 diatas & 3 dibawah merupakan komentar multibaris,
    yang maknanya sepanjang apapun kita memberikan Teks didalam tanda kutip 3 diatas & 3 dibawah maka teks kita,
    tidak akan di proses / di eksekusi oleh python itu sendiri
'''