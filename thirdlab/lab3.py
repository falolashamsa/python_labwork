sum = 0

while True:
    num = int(input("Enter a number, and a negative number to stop this: "))
    if num < 0:
        break
    sum += num

print("The sum of all entered numbers is: ", sum)



while True:
    name = input("Enter a name and type 'END' to stop this: ")
    if name == "END":
        break
    print(name)

print("I am done.")


n = int(input("Enter a number to find its first 10 multiples: "))

for x in range(1, 11):
    print(f"{n} x {x} = {n * x}")
