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

# Bilangan (Numbers)

# Python Decimal
'''

Ada kalanya perhitungan menggunakan float di Python membuat kita terkejut. 
Kita tahu bahwa 1.1 ditambah 2.2 hasilnya adalah 3.3. 
Tapi pada saat kita lakukan dengan Python, maka hasilnya berbeda.

>>> (1.1 + 2.2 ) == 3.3
False
>>> 1.1 + 2.2
3.3000000000000003

'''
import decimal

#output: 0.1
print(0.1)

#output: Decimal('0.1000000000000000055511151231257827021181583404541015625')
print(decimal.Decimal(0.1))

# Contoh Lainnya
from decimal import Decimal as D
#output: Decimal('3.3')
print(D('1.1') + D('2.2'))

#output: Decimal('3.000')
print(D('1.2') * D('2.50'))


# Kapan Saatnya Menggunakan Decimal Dibanding Float?
'''

Kita lebih baik menggunakan Decimal dalam kasus:

Saat kita ingin membuat aplikasi keuangan yang membutuhkan presisi desimal yang pasti
Saat kita ingin mengontrol tingkat presisi yang diperlukan
Saat kita ingin menerapkan perkiraan berapa digit decimal yang signifikan
Saat kita ingin melakukan operasi perhitungan sama persis dengan yang kita lakukan di sekolah

'''

# Bilangan Pecahan
'''

Python menyediakan modul fractions untuk mengoperasikan bilangan pecahan. 
Pecahan adalah bilangan yang memiliki pembilang dan penyebut, misalnya 3/2. 

Perhatikan contoh berikut:

'''
import fractions 

#output: 3/2 
print(fractions.Fraction(1.5)) 

#output: 1/3 
print(fractions.Fraction(1,3))

# Contoh Lainnya
from fractions import Fraction as F 

# Output: 2/3 
print(F(1,3) + F(1,3)) 

# Output: 6/5 
print(1 / F(5,6)) 

# Output True 
print(F(-3,10) < 0) 


# Matematika Dengan Python
'''

Python menyediakan modul math melakukan hal yang berbau matematis seperti 
trigonometri, logaritma, probabilitas, statistik, dan lain – lain.

'''
import math 

# Output: 3.141592653589793 
print(math.pi) 

# Output: -1.0 
print(math.cos(math.pi)) 

# Output: 148.4131591025766 
print(math.exp(5)) 

# Output: 2.0 
print(math.log10(100)) 

# Output: 120 
print(math.factorial(5)) 




















