class Alien:
    telo = 0

    def __init__(self, param_nama, param_umur):
        self.nama = param_nama
        self.umur = param_umur
        Alien.telo = 3434

    def greet(self):
        print(f"Hello, my name is {self.nama} and I am {self.umur} years old.")


# Membuat objek dari kelas Person
person1 = Alien("Alice", 30)
person2 = Alien("komen", 3434)

# Memanggil metode greet() pada objek person1
person1.greet()
person1.telo = 2323

person2.telo = 1221111

print(Alien.telo)
print(person1.telo)
print(person2.telo)
print(Alien.telo)
