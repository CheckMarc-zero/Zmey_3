n = int(input('Введите целое десятичное число: '))
vspom_list = []
while n != 0:
    vspom_list.append(n%2)
    n = n//2
vspom_list.reverse()
print(f'В двоичном виде: {"".join(map(str,vspom_list))}')    
