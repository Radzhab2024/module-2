def get_password(n):
    password = ''
    for i in range(1, n):
        for j in range(1, n+1):
            if i< j and n % (i+j) == 0:
                password += str(i) + str(j)
                continue
    return(password)
n = int(input('Введите первое число (от 3 до 20):'))
result = get_password(n)
print('Пароль:', result)



