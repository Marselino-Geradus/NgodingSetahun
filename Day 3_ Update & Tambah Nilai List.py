hari = ['senin','selasa','rabi','kamis','jumat']
print(f'Nama2 hari = {hari}')
print(f'Jumlah hari yang tercatat = {len(hari)}') #len() untuk menghitung panjang/jumlah data
print('='*5)

# 1. Update Nilai
hari[2] = 'rabu'
print(f'Nilai indeks ke-2 setelah update = {hari}')
print('='*5)

# 2. Tambah Nilai
'a. Append(nilai) = nilai ditambahkan pada indeks terakhir'
print(hari)
hari.append('minggu')
print(f'Nama2 hari setelah penambahan (append) = {hari}')
print('='*5)

'b. Insert(indeks,nilai) = penempatan nilai yg ditambahkan sudah terencana (mau diletakkan di mana)'
print(hari)
hari.insert(4,'sabtu')
print(f'Nama2 hari setelah penambahan (insert) = {hari}')
print('='*5)