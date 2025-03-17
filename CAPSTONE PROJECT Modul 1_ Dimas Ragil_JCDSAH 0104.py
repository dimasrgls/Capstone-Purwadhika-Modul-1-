#Nama   : DIMAS RAGIL SAMPOERNA 
#Kelas  : JCDSAH 0104
#KAMPUS : JAKARTA

#data set
daftar_mobil = [{'mobil' :'TOYOTA LAND CRUISER',
                 'jumlah_kursi' : 7,
                'bbm' : 'BENSIN',
                'harga' : 800000,
                'warna_kendaraan' : 'HITAM',
                'nopolisi': 'B 1234 KJL'
                },

                {'mobil':'TOYOTA FORTUNER',
                'jumlah_kursi' : 7,
                'bbm': 'SOLAR',
                 'harga' : 500000,
                 'warna_kendaraan' : 'PUTIH',
                 'nopolisi': 'B 1122 KFR'
                 },

                 {'mobil': 'MITSUBHISI PAJERO',
                  'jumlah_kursi' : 7,
                  'bbm' : 'BENSIN',
                  'harga' : 500000,
                  'warna_kendaraan' : 'PUTIH',
                  'nopolisi': 'B 1456 BJD'
                 },

                {'mobil': 'TOYOTA KIJANG INNOVA',
                 'jumlah_kursi' : 7,
                 'bbm': 'SOLAR',
                 'harga': 300000,
                 'warna_kendaraan': 'SILVER',
                 'nopolisi' : 'B 3322 PLJ'
                }
               ]
curt=[]


def PriceList():
     print('\n ======================== Daftar dan Price list Rental Mobil========================')
     print('Indeks\t| Mobil         \t| Seat \t| Bahan Bakar \t| Harga \t| Warna \t| No. Polisi')
     for i in range(len(daftar_mobil)):
            print('{}\t| {} \t| {} \t| {} \t| {} \t| {} \t| {}'.format(i,daftar_mobil[i]['mobil'],daftar_mobil[i]['jumlah_kursi'],
                daftar_mobil[i]['bbm'],daftar_mobil[i]['warna_kendaraan'],daftar_mobil[i]['harga'],daftar_mobil[i]['nopolisi']))

#code untuk read data
def tampilkanData():
    while True :
        tampilkanData = input('''\n
        ======================== Menu Daftar dan Pricelist Rental Mobil Andalan ========================
                            
         Pilihan Menu :
                    1. Tampilkan Seluruh Pricelist Rental Mobil Andalan
                    2. Tampilkan Pricelist Jenis Mobil Tertentu
                    3. Kembali Ke Main Menu
                              
                    Masukan Masukan Angka Menu Yang Anda Ingin jalankan (1-3):''' )
        if (tampilkanData == '1') :
            if (len(daftar_mobil) <= 0):
                print('\n ---------- Mobil Yang Anda Cari Tidak Ada ----------')
            else :
                PriceList()
        elif (tampilkanData == '2') :
            if (len(daftar_mobil) <= 0):
                print('\n ---------- Mobil Yang Anda Cari Tidak Ada ----------')
            else:
                Tampilkan = int(input('Masukan Indeks Mobil Yang Ingin Di Tampilkan: '))
                if (Tampilkan < len(daftar_mobil)):
                    print('Mobil Dengan Indeks {}'.format(Tampilkan))
                    print('Indeks\t| Mobil         \t| Seat \t| Bahan Bakar \t| Harga \t| Warna \t| No. Polisi')
                    print('{}\t| {} \t| {} \t| {} \t| {} \t| {} \t| {}'.format(Tampilkan,daftar_mobil[Tampilkan]['mobil'],daftar_mobil[Tampilkan]['jumlah_kursi'],
                    daftar_mobil[Tampilkan]['bbm'],daftar_mobil[Tampilkan]['warna_kendaraan'],daftar_mobil[Tampilkan]['harga'],daftar_mobil[Tampilkan]['nopolisi']))
                else:
                    print('Mobil Dengan Indeks {}'.format(Tampilkan))  
                    print('\n ---------- Mobil Yang Anda Cari Tidak Ada ---------- ')
        elif (tampilkanData == '3') :
            break
        else:
                print('\n ########## Pilihan yang Anda masukkan salah ##########')

# code untuk tambah data
def MenambahMobil():
    while True:
        nambah_mobil = input('''\n
        ======================== Menu Tambah Data Rental Mobil Andalan ========================
                             
         Pilihan Menu :
                    1. Menambah Pricelist Rental Mobil Andalan
                    2. Kembali Ke Main Menu
                              
                    Masukan Masukan Angka Menu Yang Anda Ingin jalankan (1-2):''' ) 
        if (nambah_mobil == '1'):
            while True:
                input_nopolisi = input('Masukan No Polisi Kendaraan: ').upper()
                validasi_Nopolisi = False
                for dataRental in daftar_mobil:
                    if dataRental ['nopolisi'] == input_nopolisi:
                        validasi_Nopolisi = True
                        print('\n ---------- Data mobil sudah ada ----------')
                        break
                if validasi_Nopolisi == False:
                    print('\n ---------- Data mobil tidak ada, silahkan input data ----------')
                    namaMobil = input('Masukan Nama Mobil:  ').upper()
                    jumlahKursi = int(input('Masukan Jumlah Kuris: '))
                    bahanbakar = input('Masukan Jenis Bahan Bakar:  ').upper()
                    warna = input('Masukan Warna Kendaraan:  ').upper()
                    hargaSewa = int(input('Masukan Harga Sewa Kendaraan: '))
                    no_polisi= input_nopolisi
                    cek = input('Apakah Anda Yakin Untuk Menyimpan Data Mobil ? (Y/N)= ').upper()
                    if (cek == 'Y'):
                        daftar_mobil.append({
                            'mobil' : namaMobil,
                            'jumlah_kursi' : jumlahKursi,
                            'bbm' : bahanbakar,
                            'warna_kendaraan' : warna,
                            'harga' : hargaSewa,
                            'nopolisi' : no_polisi })       
                        print('\n ########## Sukses Menyimpan Data ##########')
                        PriceList()
                        break
                    elif(cek == 'N'):
                         print('\n ########## Proses tambah data di batalkan ##########')
                         break
        elif (nambah_mobil == '2'):
            break
        else:
            print('\n ########## Pilihan yang Anda masukkan salah ##########')

#code untuk update data
def update_mobil():
     while True:
        Update = input('''\n
        ======================== Menu Update Data Rental Mobil Andalan ========================               
                
                Pilihan Menu:
                          
                1. Update Data Mobil
                2. Kembali Ke Main Menu
                
                Masukan Masukan Angka Menu Yang Anda Ingin jalankan (1-2): ''')
        if (Update == '1') :
            PriceList()
            while True:
                input_nopolisi = input('Masukan No Polisi Kendaraan: ').upper()
                validasi_Nopolisi = False
                for dataRental in daftar_mobil:
                    if dataRental ['nopolisi'] == input_nopolisi:
                        validasi_Nopolisi = True
                        print(' **** Data Mobil Rental  ****  ')
                        print('----------------------------------')
                        print(f"[1] Mobil                   : {dataRental['mobil']}")
                        print(f"[2] Jumlah Kursi            : {dataRental['jumlah_kursi']}")
                        print(f"[3] Bahan Bakar             : {dataRental['bbm']}")
                        print(f"[4] Harga                   : {dataRental['harga']}")
                        print(f"[5] Warna                   : {dataRental['warna_kendaraan']}")
                        print(f"[6] No Polisi               : {dataRental['nopolisi']}")
                        print('----------------------------------')
                        while True:
                            input_kolom = int(input('Pilih kolom yang ingin diubah (1-6): '))
                            if (input_kolom == 1):
                                mobilLama = dataRental['mobil']
                                mobilBaru = input('Masukan Mobil: ').upper()
                                dataRental['mobil'] = mobilBaru
                                print(f'Nama mobil sudah diubah dari {mobilLama} menjadi {mobilBaru}')
                                cek_Update()
                                break
                            elif (input_kolom == 2):
                                jumlah_lama = dataRental['jumlah_kursi']
                                jumlah_baru = int(input('Masukan Jumlah Kursi Kendaraan: '))
                                dataRental['jumlah_kursi'] = jumlah_baru
                                print(f'Jumlah kursi sudah diubah dari {jumlah_lama} menjadi {jumlah_baru}')
                                cek_Update()
                                break
                            elif (input_kolom == 3):
                                bbm_lama = dataRental['bbm']
                                bbm_baru = input('Masukan Jenis Bahan Bakar: ').upper()
                                dataRental['bbm'] = bbm_baru
                                print(f'Jenis bahan bakar sudah diubah dari {bbm_lama} menjadi {bbm_baru}')
                                cek_Update()
                                break
                            elif (input_kolom == 4):
                                harga_lama = dataRental['harga']
                                harga_baru = int(input('Masukan Harga Kendaraan: '))
                                dataRental['harga'] = harga_baru
                                print(f'Harga sewa kendaraan sudah diubah dari {harga_lama} menjadi {harga_baru}')
                                cek_Update()
                                break
                            elif (input_kolom == 5):
                                warna_lama = dataRental['warna_kendaraan']
                                warna_baru = input('Masukan Warna Kendaraan: ').upper()
                                dataRental['warna_kendaraan'] = warna_baru
                                print(f'Warna kendaraan sudah diubah dari {warna_lama} menjadi {warna_baru}')
                                cek_Update()
                                break
                            elif (input_kolom == 6):
                                plat_lama = dataRental['nopolisi']
                                plat_baru = input('Masukan No. Polisi kendaraan: ').upper()
                                dataRental['nopolisi'] = plat_baru
                                print(f'No. Polisi kendaraan sudah diubah dari {plat_lama} menjadi {plat_baru}')
                                cek_Update()
                                break
                            else:
                                print('\n ---------- Angka yang anda masukan tidak sesuai ---------- ')
                                break
                if validasi_Nopolisi == False:
                    print('\n ---------- Data tidak ditemukan, silahkan coba lagi ----------')
                else:
                    break
        elif(Update == '2'):
            break
        else:
            print('\t\t\t ########## Pilihan yang Anda masukkan salah ##########')

def cek_Update():        
    while True:
        cek_update = input('Apakah Anda Yakin Untuk Menyimpan Data Mobil ? (Y/N)= ').upper()
        if(cek_update == 'Y'):
            print('\n ---------- Data mobil berhasil di update ----------')
            PriceList()
        else:
            print('\n ---------- Data mobil batal di update ----------')
        break


#code untuk menghapus data
def menghapusMobil():
    PriceList()
    while True:
        hapusData = input('''\n
        ========================= Menu Hapus Data Rental Mobil Andalan ========================               
                
                Pilihan Menu:
                          
                1. Hapus Data Mobil
                2. Kembali Ke Main Menu
                
                Masukan Masukan Angka Menu Yang Anda Ingin jalankan (1-2): ''')
        if (hapusData == '1') :
            PriceList()
            inputHapus = int(input('Masukan Indeks Data Mobil Yang ingin Di Hapus:  '))
            if (inputHapus >= len(daftar_mobil)):
                print('\t      Data Yang Anda Cari Tidak Ada')
            else:
                while True:
                    cek_2 = input('Apakah Anda Yakin Ingin Menghapus Data Mobil ? (Y/N)= ').upper()
                    if(cek_2 == 'Y'):
                        daftar_mobil.remove(daftar_mobil[input])
                        print('\n ---------- Data Sudah Terhapus ----------')
                        break
                    elif(cek_2 == 'N'):
                        print('\n ---------- Data Sudah Tidak Terhapus ----------')
                        break
        elif(hapusData == '2'):
            break
        else:
            print('\n ########## Pilihan yang Anda masukkan salah ##########')


# code untuk main menu               
while True:
    Menu = input('''   
                 ======================== Main Menu Rental Mobil Andalan ========================
                 
                 Main Menu:
                 1. Daftar dan Price list Mobil
                 2. Menanbah Data Mobil 
                 3. Update Data
                 4. Menghapus Data 
                 5. Exit
                 Masukan Angka Menu Yang Anda Pilih (1-5) :''')
    if(Menu == '1'):
        tampilkanData()
    elif(Menu == '2'):
        MenambahMobil()
    elif(Menu == '3'):
        update_mobil()
    elif(Menu== '4'):
        menghapusMobil() 
    elif(Menu== '5'):
        break
    else:
        print('\n ########## Pilihan yang Anda masukkan salah ##########')