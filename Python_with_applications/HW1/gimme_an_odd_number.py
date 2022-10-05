def gimme_an_odd_number():
    numbers = []
    while True:
        number = int(input('Please enter an integer.'))
        numbers.append(number)
        if number % 2 == 0:
            continue
        else:
            print(numbers)
        break


gimme_an_odd_number()
