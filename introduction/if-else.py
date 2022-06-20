n = int(input().strip())

# Checking if the input is odd or not
if n%2 != 0:
    print("Weird")

# Checking if n is even and is within the range of 2,5
elif n%2 == 0 and n in range(2,5):
    print("Not Weird")

# Checking if n is even and is within the range of 6,20
elif n%2 == 0 and n in range(6,20):
    print("Weird")

# Checking if n is even and greater than 20
elif n%2 == 0 and n >20:
    print("Not Weird")

else:
    print("Error")