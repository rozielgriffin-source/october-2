input("Parity will make even numbers end in 0 and odd numbers end in 1, press enter.")
for n in [2, 3, 4, 5, 8, 9]:
    if n & 1:
        print("odd number: ", n)
    else:
        print("Even number: ", n)

n = int(input("Enter a number like 13 or 7: "))
input("Count the 1s as bits drop off, press enter. ")
temp = n
while temp > 0:
    print("Binary: ", bin(temp)[2:], "Last bit: ", temp & 1)
    temp >>= 1
print("total 1s in the binary number: ", n, "=", bin(n).count('1'))