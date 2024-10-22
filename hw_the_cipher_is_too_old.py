def password (n):
    result = ''
    for f_num in range(1, n):
        for s_num in range(f_num, n):
            multi = f_num + s_num
            if n % multi == 0:
                if f_num == s_num:
                    continue
                else:
                 result += str(f_num) + str(s_num)
    return result
first_insert = 0
while first_insert != 'end':
    print('--------------------------------------')
    first_insert = input('Введите число с первой вставки (от 3 до 20), или end для завершения программы: ')
    if first_insert == 'end':
        break
    else:
        first_insert = int(first_insert)
    answer = password(first_insert)
    print('Пароль: ' + answer)
    print('\n')
