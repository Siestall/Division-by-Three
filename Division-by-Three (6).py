try:
    num = int(input('Enter the number: '))
    if num % 3 == 0:
        print(f'Yes, answer - {num//3}, remainder is {num%3}')
    else:
        print(f'No, answer - {num/3}')
except:
    print('Enter integer')