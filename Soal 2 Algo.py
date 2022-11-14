sapi = ['1.Sapi Warrior : 690 hari','2.Sapi Mage : 420 hari','3.Sapi Assasin : 530 hari','4.Sapi Nolep : 330 hari']
warrior = 690
mage = 420
assasin = 530
nolep = 330
total_hari = 0

print('-'*5,'PERHITUNGAN WAKTU YANG DIPERLUKAN SAPI UNTUK DEWASA','-'*5)
print('Rinciannya sebagai berikut:')
for i in sapi:
    print(i)

while True:
    kode = int(input('\nEntrikan kode sapi: [1][2][3][4] '))
    if kode == 1 or kode == 2 or kode == 3 or kode == 4:
        pass
    else:
        continue
    jumlah = int(input('Berapa jumlah sapi yg ingin dimasukkan: '))
    if kode == 1:
       total_hari += warrior*jumlah
    elif kode == 2:
        total_hari += mage*jumlah
    elif kode == 3:
        total_hari += assasin*jumlah
    elif kode == 4:
        total_hari += nolep*jumlah
    
    ask = input('\nAdakah sapi yang ingin dimasukkan lagi: [Y][T]')
    if ask == 'Y' or ask == 'y':
        continue
    elif ask == 'T' or ask == 't':
        break
    
tahun = int(total_hari/365)
bulan = int((total_hari%365)/30)
hari = (total_hari%365)%30
print(f'\nJumlah hari yang diperlukan adalah: {tahun} tahun {bulan} bulan {hari} hari')