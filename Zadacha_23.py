print('Введите через пробел элементы списка:')
input_list = input().split()
i = 0
while i <= len(input_list)-i-1 :
    print(f'Произведение {i+1} и {len(input_list)-i} элементов: {int(input_list[i])*int(input_list[len(input_list)-i-1])}')
    i +=1
