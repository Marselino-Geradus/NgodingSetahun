#inisiasi list
a = range(2,11,2)
genap = list(a)
print('=>>> List bilangan genap antara 2-10 = ',genap)
print('='*5)

#inisiasi variabel bilangan genap terbesar
angka_terbesar = genap[0]

#buat fungsi For
for nilai in genap:
    if nilai > angka_terbesar:
        angka_terbesar = nilai

print('=>>> Bilangan genap terbesar dalam list = ',angka_terbesar)