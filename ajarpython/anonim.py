# anonumous function
# currying <- haskell curry

# biasa tanpa annm function
def f_pangkat(angka, n):
    hasil = angka ** n
    return hasil


data_hasil = f_pangkat(5, 2)
print(f"fungsi biasa = {data_hasil}")


# dengan curryting menjadi

def f_pangkat_lambda(n):
    return lambda angka: angka ** n


pangkat_dua_dari = f_pangkat_lambda(2)
print(f"pangkat dua dari 4 = {pangkat_dua_dari(4)}")

lima_pangkat_dua = pangkat_dua_dari(5)
print(f"pangkat dua dari 5 = {lima_pangkat_dua}")

enam_pangkat_tiga = f_pangkat_lambda(3)(6)
print(f"enam pangkat tiga = {enam_pangkat_tiga}")
