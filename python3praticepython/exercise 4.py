num = int(input("Número: "))
list_range = list(range(1,num+1))

divisor_list = []

for number in list_range:
    if num % number == 0:
        divisor_list.append(number)
print(divisor_list)

#não consegui fazer esse exercício. Esse é o gabarito.