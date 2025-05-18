price = 1000000
budget = float(input("Enter your budgeted amount: "))

if budget < 500000 and budget > 300000:
    down_payment = (10 / 100) * price
    print(down_payment)

elif budget > 500000:
    down_payment = (20 / 100) * price
    print(down_payment)