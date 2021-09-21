#mainigais saraksts jeb list
# []

#mainigais var saturet dažadus datu tipus
my_list = ['teksts',1, 2]
print(my_list)

#Elmentu skaits mainigaja

print("Saraksta my_lists elementu skaits: ", len(my_list))

#index metode


print(my_list[1])
print(my_list[0:])

#elemenra maiņa

my_list[0] = 'sveiki'
print(my_list)

#elementa pievienošana

print(my_list + ["čau"])
my_list = my_list + ["suns"]
print(my_list)

my_list.append('kaķis')
print(my_list)

#pop

my_list.pop(0)
print(my_list)
