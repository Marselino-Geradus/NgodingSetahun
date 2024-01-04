'''Hitunglah jumlah bilangan ganjil dalam sebuah list!'''
#Buat list bilangan 1-10
bil = range(1,10+1)
print(list(bil))
print('='*5)

#inisiasi variabel jumlah bilangan ganjil
jumlah_ganjil = 0

#perulangan FOR untuk menghitung
for jumlah in list(bil):
    if jumlah % 2 == 1:
        jumlah_ganjil += 1

print(f'Jumlah bilangan ganjil dalam list = {jumlah_ganjil}')
print('='*5)
