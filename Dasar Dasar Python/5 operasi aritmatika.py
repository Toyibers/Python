# Oeprasi Aritmatka

a=10
b=3

#Operasi tambah +
hasil= a + b
print(a,'+',b,'=',hasil)

#Operasi pengurangan -
hasil= a - b
print(a,'-',b,'=',hasil)

#Operasi perkalian *
hasil= a * b
print(a,'x',b,'=',hasil)

#Operasi pembagian :
hasil= a / b
print(a,':',b,'=',hasil)

#Operasi eksponen (pangkat) **
hasil= a ** b
print(a,'**',b,'=',hasil)

#Operasi modulus (sis bagi) %
hasil= a % b
print(a,'%',b,'=',hasil)

#Operasi floor division (pembulatan) //
hasil= a // b
print(a,'//',b,'=',hasil)

# prioritas operasi, opertional precedence

'''
    1. ()
    2. eksponen **
    3. perkalian dan teman teman * / ** % //
    4. pertambahan dan pengurangan + -
'''

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x,'**', y,'x', z, '+', x, ':', y, '-', y, '%' ,z, '//', x,'=',hasil)

hasil = x + y * z
print(x, '+', y, 'x', z, '=', hasil)

