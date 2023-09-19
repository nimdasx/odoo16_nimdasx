# filter(function, iterable)
# function: Ini adalah fungsi yang digunakan untuk menentukan kondisi filter.
# Fungsi ini harus mengembalikan True atau False (atau nilai yang dapat dievaluasi sebagai True atau False)
# tergantung pada apakah elemen dalam iterable harus disertakan dalam hasil filter atau tidak.
# iterable: Ini adalah iterable yang akan difilter.

# Definisikan fungsi filter
def is_even(x):
    return x % 2 == 0


# Buat list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers)

# Gunakan filter() untuk menyaring bilangan genap
even_numbers = filter(is_even, numbers)
print(even_numbers)

# Konversi hasil filter menjadi list
even_numbers_list = list(even_numbers)
print(even_numbers_list)

# Hasilnya adalah list bilangan genap: [2, 4, 6, 8, 10]
