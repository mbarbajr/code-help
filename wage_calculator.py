salaryRate = 500
hourlyRate = 15
overTimeRate = 20
weeklyPay = 0

category = input("Is the employee hourly or salary")

if category == 'hourly':
    hours = int(input("How many hours were worked"))
    if hours <= 40:
        weeklyPay = 40*hourlyRate
        print(weeklyPay)
    else:
        weeklyPay = 40*hourlyRate + (hours - 40)*overTimeRate
        print(weeklyPay)
else:
    print('else')
