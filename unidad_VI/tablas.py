i = 1
max_num = 10

while i <= max_num:
    j = 1
    while j <= max_num:
        print(f'{i * j:2}, ', end = '')
        j += 1
    print()
    i += 1
print('Fin')