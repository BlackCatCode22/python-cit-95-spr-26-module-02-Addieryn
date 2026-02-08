try:
    first = int(input('Enter first number: '))
    second = int(input('Enter second number: '))
    third = int(input('Enter third number: '))


    if first == second and first > third:
        print(f'The first and second number, ({first}), are both the largest')
    elif first == third and first > second:
        print(f'The first and third number, ({first}), are both the largest')
    elif second == third and second > first:
        print(f'The first and third number, ({second}), are both the largest')
    elif second == third and second == first:
        print(f'They are all the same number! They are all the largest!')
    elif first > second and first > third:
        print(f'The first number, ({first}) is the largest number')
    elif second > first and second > third:
        print(f'The second number, ({second}) is the largest number')
    else:
        print(f'The third number, ({third}) is the largest number')

except ValueError:
    print('Please enter a number')