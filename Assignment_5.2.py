largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == 'done':
        break
    try:
        value = int(num)
    except:
        print("Invalid input")
        continue

#can't use for statement because value and num is only one number
#value is not a list of numbers
    if smallest is None:
            smallest = value
    elif value < smallest:
            smallest = value

    if largest is None:
            largest = value
    elif value > largest:
            largest = value

print("Maximum is", largest)
print("Minimum is", smallest)
