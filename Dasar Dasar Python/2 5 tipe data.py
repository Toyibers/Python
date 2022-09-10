# a = 10, a adalah variabel dengan nilai 10

print("===INTEGER===")

# Tipe data : angka satuan (integer)
data_integer = 1
print("- data    : ",data_integer)
print("- bertipe : ", type(data_integer))

print("===FLOAT===")

# Tipe data : angka dengan koma (float)
data_float = 1.5
print("- data    : ",data_float)
print("- bertipe : ", type(data_float))

print("===STRING===")

# Tipe data : kumpulan karakter (string) 
data_string = "ucup 123"
print("- data    : ",data_string)
print("- bertipe : ", type(data_string))

print("===BOOLEAN===")

# Tipe data : biner true/false (boolean)
data_bool = True
print("- data    : ",data_bool)
print("- bertipe : ", type(data_bool))

#TIPE DATA KHUSUS

print("===COMPLEX===")

# Tipe data :bilangn komples
data_complex = complex(5,6)
print("- data    : ",data_complex)
print("- bertipe : ", type(data_complex))

print("===BAHASA C===")

# Tipe data : tipe data dari bahasa C
from ctypes import c_double
data_c_double = (10,5)
print("- data    : ",data_c_double)
print("- bertipe : ", type(data_c_double))