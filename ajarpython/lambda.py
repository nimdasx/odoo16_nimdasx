# gak pakai lambda
def f_kuadrat(angka):
    return angka ** 2


print(f_kuadrat(3))
print(f"hasil fungsi kuadrat = {f_kuadrat(3)}")

# pakai lambda
l_kuadrat = lambda telo: telo ** 2

print(l_kuadrat(3))
print(f"hasil lambda kuadrat = {l_kuadrat(3)}")

l_pangkat = lambda number, power: number ** power
print(f"hasil lambda pangkat = {l_pangkat(4, 2)}")

# sorting
data_list = ["Otong", "Ucup", "dudung"]
data_list.sort()
print(f"sorted list = {data_list}")

# sorting by panjang
data_list.sort(key=len)
print(f"soretd list by len/panjang = {data_list}")


# sorting by panjang pakai fungsi custom
def f_panjang_nama(nama):
    return len(nama)


data_list.sort(key=f_panjang_nama)
print(f"sorted list by leng/panjang fungsi custom ={data_list}")

# sorting by lambda
data_list.sort(key=lambda nama: len(nama))
print(f"sorted list by len/panjang pakai lamda = {data_list}")

# filter
data_angka = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(f"data angka = {data_angka}")


# pakai fungsi biasa
def f_kurang_dari_lima(angka):
    # print(angka < 5)
    # return True
    return angka < 5


data_angka_baru = list(filter(f_kurang_dari_lima, data_angka))
print(f"data angka kurang dari lima pakai fungsi = {data_angka_baru}")

# pakai lambda
data_angka_baru = list(filter(lambda x: x < 5, data_angka))
print(f"data angka kurang dari lima pakai lambda = {data_angka_baru}")

# kasus genap
data_angka_genap = list(filter(lambda sapi: sapi % 2 == 0, data_angka))
print(f"data angka genap pakai lambda = {data_angka_genap}")

# kelipatan tiga
data_angka_kelipatan3 = list(filter(lambda sapi: sapi % 3 == 0, data_angka))
print(f"data angka kelipatan 3 = {data_angka_kelipatan3}")


def f_kelipatan_tiga(angka):
    telo = angka % 3 == 0
    print(f"angka {angka} kelipatan tiga? {telo}")
    return telo


data_angka_kelipatan3_pakai_fungsi = list(filter(f_kelipatan_tiga, data_angka))
print(f"data angka kelipatan tiga pakai fungsi = {data_angka_kelipatan3_pakai_fungsi}")
