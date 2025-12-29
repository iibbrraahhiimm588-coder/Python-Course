while True:  # repeat as long as user wants
    x = int(input("Enter number: "))
    
    for i in range(1, 11):  # generate table
        print(f'{x} x {i} = {x * i}')
    
    again = input("Generate again? (yes/no): ").lower()
    if again != 'yes':
        break
