print('Введите через пробел элементы списка:')
input_list = input().split()
drob_list = []
for i in input_list:
    drob_list.append(round(float(i)%1,6))
print(*drob_list,sep=" ")    
print(f'Разница между максимальной и минимальной дробными частями: {round(max(drob_list)-min(drob_list),6)}')
