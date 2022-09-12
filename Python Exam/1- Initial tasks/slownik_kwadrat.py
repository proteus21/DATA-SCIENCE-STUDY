"""
     Napisz program, który pobiera od użytkownika liczbę N,
     następnie tworzy słownik z kluczami od 1 do N z wartościami,
     które są kwadratami kluczy.
"""
my_dict={}
number= int(input("Give the number:"))
for i in range(0,number):
    my_dict[i]=i**2
print(my_dict)

for key, value in my_dict.items():
    print("Square the number {} is {}".format(key, value))