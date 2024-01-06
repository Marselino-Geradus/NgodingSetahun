a = range(10,20)
print('Deretan bilangan = ',list(a))
print('='*5)

jumlah_prima = 0
def prima(a):
    if a <= 1:
        return False
    for i in range(2,int(a**0.5)+1):
        if a % i == 0:
            return False
    return True
    
#hitung bil prima
for angka in list(a):
    if prima(angka):
        jumlah_prima += 1
print(jumlah_prima)