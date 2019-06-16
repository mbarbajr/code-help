def main():
    salaryRate = 500
    hourlyRate = 15
    overTimeRate = 20
    weeklyPay = 0

    # Run loop to get user initial input
    while True:
        # Get user initial input, must be either 'hourly' or salary'
        category = input("Is the employee hourly or salary:\t")

        # Checks if input is a string
        if category.isalpha():
            if 'salary' in category.lower():
                print(salaryRate)
                break
            elif 'hourly' in category.lower():
                hours = int(input('How many hours were worked:\t'))
                if hours <= 40:
                    weeklyPay = 40 * hourlyRate
                    print(weeklyPay)
                else:
                    weeklyPay = 40 * hourlyRate + (hours - 40) * overTimeRate
                    print(weeklyPay)
                break
            else:
                print('Invalid input please try again.')
        else:
            print(r'Please type either salary or hourly.')


if __name__ == '__main__':
    main()
