class Pegawai:
    nama = 'sotong'
    __nilai = 0

    def set_gaji(dagelan, value):
        dagelan.gaji = value

    def set_tunjangan(bakyak):
        print("opo yo")

    def bekerja(asdassfsaf, belajarnya_gimana):
        print(f"{asdassfsaf.nama} belajar {belajarnya_gimana}")

    def set_nilai(awet, value):
        awet.__nilai = value

    def get_nilai(aamiin):
        return aamiin.__nilai


fatih = Pegawai()
fatih.nama = 'surotong'
fatih.set_gaji(234234)
print(fatih.gaji)
fatih.set_tunjangan()
print(fatih.nama)
fatih.bekerja("dengan giat")
fatih.set_nilai(343)
print(fatih.get_nilai())
print(fatih.__dict__)
print(fatih)
