#1. Buat List dengan cara biasa
namaBuah = ["rambutan", "imbe", "delima","apel"]
print(namaBuah)

#2. List dengan fungsi Range
'List bilangan ganjil antara 10-30'
bil_ganjil = range(11,30,2)
list_ganjil = list(bil_ganjil)
print(list_ganjil)


#3. List dengan fungsi For Loop
'Tampilkan simbol bintang sebanyak lima kali dalam sebuah list'
i = '*'
bintang = [i for a in range(1,6)]
print(bintang)