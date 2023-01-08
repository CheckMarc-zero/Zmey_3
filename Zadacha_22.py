print('Введите через пробел элементы списка:')
input_list = input().split()
sum = 0
for i in range(1,(len(input_list)+1),2):
    sum += int(input_list[i])
print(f'Сумма элементов на нечетных позициях: {sum}')    
