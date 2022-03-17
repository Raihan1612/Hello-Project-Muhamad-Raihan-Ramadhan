# kapasitas motor
kap_motor = 1
# inputkan kapasitas masing-masing kendaraan lainnya
kap_mobil = int(input("Kapasitas Mobil (2-5): "))
kap_minibus = int(input("Kapasitas Minibus (8-20): "))
kap_bus = int(input("Kapasitas Bus (40-100): "))

###{Soal-1} print kapasitas tiap kendaraan dengan rapi seperti di bawah ini, NAMUN dengan hanya 1 baris kode python saja.
# Kapasitas Motor 	    = 1
# Kapasitas Mobil 	    = 2
# Kapasitas Minibus 	= 10
# Kapasitas Bus 		= 80
print("Kapasitas Motor         =",kap_motor,"\nKapasitas Mobil         =",kap_mobil,"\nKapasitas Minibus       =",kap_minibus,"\nKapasitas Bus           =",kap_bus)

###{Soal-2} meminta inputan jumlah penumpang dari user, asumsi user akan menginputkan integer
p = int(input("Masukkan total jumlah penumpang: ")) # ganti 0 dengan kode anda

# Menghitung jumlah kebutuhan setiap jenis kendaraan. Setiap kendaraan harus full penumpang baru bisa digunakan
###{Soal-3} hitung jumlah bus yang dibutuhkan. 
jumlah_bus = (p//kap_bus) # ganti 0 dengan kode anda
###{Soal-4} hitung jumlah penumpang yang tidak bisa tertampung oleh bus. 
sisa = (p%kap_bus) # ganti 0 dengan kode anda
###{Soal-5} hitung jumlah minibus yang dibutuhkan. 
jumlah_minibus = (sisa//kap_minibus) # ganti 0 dengan kode anda
###{Soal-6} hitung jumlah penumpang yang tidak bisa tertampung oleh minibus. 
sisa = (sisa%kap_minibus) # ganti 0 dengan kode anda
###{Soal-7} hitung jumlah mobil yang dibutuhkan. 
jumlah_mobil = (sisa//kap_mobil) # ganti 0 dengan kode anda
###{Soal-8} hitung jumlah penumpang yang tidak bisa tertampung oleh mobil. 
sisa = (sisa%kap_mobil) # ganti 0 dengan kode anda
###{Soal-9} hitung jumlah motor yang dibutuhkan. 
jumlah_motor = (sisa//kap_motor) # ganti 0 dengan kode anda

###{Soal-10} print kebutuhan tiap kendaraan dengan rapi seperti di bawah ini, NAMUN dengan hanya 1 baris kode python saja.
# Jumlah Motor 	    = 0
# Jumlah mobil 	    = 0
# Jumlah minibus 	= 4
# Jumlah bus 	    = 2
print("Jumlah Motor    =",jumlah_motor,"\nJumlah mobil    =",jumlah_mobil,"\nJumlah minibus  =",jumlah_minibus,"\nJumlah bus      =",jumlah_bus)