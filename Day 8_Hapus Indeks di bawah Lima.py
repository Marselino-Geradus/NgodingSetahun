"""
==> Hapus indeks yang nilainya lebih kecil dari 5 
menggunakan fungsi FOR dan Method <==
"""
def hapus_elemen(angka):
    for i in range(len(angka) - 1, -1, -1):
        if angka[i] < 5:
            del angka[i]

def main():
    angka = range(1,11)
    a = list(angka)
    print(f'List Awal : {a}')
    hapus_elemen(a)
    print(f"List sesudah penyisihan : {a}")


main()