n = int(input("Enter a number (try 12 or 5): "))

guess = input("Guess the binary number: ")

input("Binary. Press enter to run")
print("decimal: ", n, "-> binary: ", bin(n)[2:])
print(" your guess:", guess)

input("AND - both bits must be 1, press enter to continue. ")
print("binary of 12 is: ", bin(12)[2:])
print("binary of 10 is: ", bin(10)[2:])
print("binary of 12 & 10 :", 12 & 10)

input("OR - atleast 1 bit must be 1, press enter to continue.")
print("12 or 10 =", 12 | 10)