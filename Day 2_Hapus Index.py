#1. Buat List
'Angka ganjil 10 buah'
ganjil = range(1,20,2)
l_ganjil = list(ganjil)
print('Indeks awal = ',l_ganjil)
print('='*5)

#2. Akses Indeks
'Indeks 1, 7, dan terakhir'
print('=> Indeks 1, 7, dan terakhir diakses <=')
print(l_ganjil[1],l_ganjil[7],l_ganjil[-1])
print('='*5)

#3. Hapus Indeks
'Indeks 4 & 8'
del l_ganjil[4] 
print('=> Indeks ke-4 (9) dihapus <=')
print(l_ganjil)
del l_ganjil[8]
print('Indeks ke-8 (19) dihapus <=')
print(l_ganjil)
print('='*5)